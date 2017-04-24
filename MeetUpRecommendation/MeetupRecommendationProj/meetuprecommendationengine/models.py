from django.db import models
from py2neo import Graph,Node
import json
import ipdb


# Create your models here.
categories_url="https://api.meetup.com/2/categories?offset=0&format=json&photo-host=public&page=20&order=shortname&desc=false&sig_id=225559964&sig=1efa3f6254d446aa80e717d413db9ad50916e9cb"
graph = Graph("http://neo4j:neo@localhost:7474/db/data/")
class NeoDatabaseHelper(models.Model):
    questions = ["What’s the most popular topic?",
                 "Which group was created most recently?",
                 "How many groups have been running for at least 4 years?"
                 ]
    # def loadGroups(self):
    #     graph.delete_all()
        # praveen=Node("Person", name="Praveen")
        # graph.create(praveen)
        # return "Success"
    # def createCategories(self,response):
    #     check= response.read().decode('utf-8')
    #     # with open('D:/data.json', 'w') as f:
    #     #         json.loads(check, f,indent=4)
    #
    #     # temp=json.loads(json.loads(check))
    #     with open('D:/data.json', mode='w', encoding='utf-8') as f:
    #         f.write(check)
    #     query="""
    #     CALL apoc.load.json("file:/D:/data.json") YIELD value
    #     with value.results as categories
    #     foreach (category in categories| create(cat:Category{name:category.name}))
    #     """
    #     query_select = """
    #             MATCH (cat:Category) RETURN {Name:cat.name} as category
    #             """
    #     graph.run(query)
    #     res= graph.run(query_select)
    #     col=res._source.buffer
    #     result=[]
    #     for record in col:
    #         result.append(record[0])
    #
    #     # ipdb.set_trace()
    #     categoriesStr=json.dumps(result)
    #     return categoriesStr

    def loadGroupsAndTopics(self):
        loadGroupQuery='''LOAD CSV WITH HEADERS
            FROM "https://raw.githubusercontent.com/neo4j-meetups/modeling-worked-example/master/data/groups.csv"
            AS row
            MERGE (group:Group { id:row.id })
            ON CREATE SET
            group.name = row.name,
            group.urlname = row.urlname,
            group.rating = toInt(row.rating),
            group.created = toInt(row.created)'''
        loadTopicsQuery='''LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/neo4j-meetups/modeling-worked-example/master/data/groups_topics.csv"  AS row
            MERGE (topic:Topic {id: row.id})
            ON CREATE SET topic.name = row.name, topic.urlkey = row.urlkey'''
        createindexForGroupId='''CREATE INDEX ON :Group(id)
        '''
        createindexForTopicId = '''CREATE INDEX ON :Topic(id)
                '''
        connectTopicsAndGroups='''LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/neo4j-meetups/modeling-worked-example/master/data/groups_topics.csv"  AS row
            MATCH (topic:Topic {id: row.id})
            MATCH (group:Group {id: row.groupId})
            MERGE (group)-[:HAS_TOPIC]->(topic)'''
        createGroupIndexForName='''CREATE INDEX ON :Group(name)'''
        createTopicIndexForName = '''CREATE INDEX ON :Topic(name)'''
        graph.run(loadGroupQuery)
        graph.run(loadTopicsQuery)
        graph.run(createindexForGroupId)
        graph.run(createindexForTopicId)
        graph.run(connectTopicsAndGroups)
        graph.run(createGroupIndexForName)
        graph.run(createTopicIndexForName)

    def loadDefaultQuestions(self):
        return json.dumps(self.questions)
    def sendQueryOnSearchSelect(self,str):
        return self.getresponseOnQueryChange(str)

    def getresponseOnQueryChange(self,query):
        return self.callPopularTopics(query)

    def callPopularTopics(self,query):
        res_type=""
        res_query=""
        if self.questions[0] == query:
            res_query = '''
                 MATCH (t:Topic)<-[:HAS_TOPIC]-()
                 RETURN t.name, COUNT(*) AS count
                 ORDER BY count DESC
                 '''
            res_type=0
        if self.questions[1] == query:
            res_query = '''
                            MATCH (g:Group)
                RETURN g
            ORDER BY g.created DESC
                    LIMIT 1
                             '''
            res_type = 1
        if self.questions[2] == query:
            res_query ='''WITH(4 * 365 * 24 * 60 * 60 * 1000)
            AS
            fourYears
            MATCH(g: Group)
            WHERE
            g.created < timestamp() - fourYears
            RETURN
            g'''
            res_type = 2
        res=graph.run(res_query)
        col = res._source.buffer
        result=[]
        for record in col:
           result.append(record[0])
        data={}
        data['contents']=result
        data['res_type']=res_type
        jsonData=json.dumps(data)
        return jsonData



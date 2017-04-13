from django.db import models
from py2neo import Graph,Node
import json
from django.http import JsonResponse
from django.http import HttpResponse
# Create your models here.
categories_url="https://api.meetup.com/2/categories?offset=0&format=json&photo-host=public&page=20&order=shortname&desc=false&sig_id=225559964&sig=1efa3f6254d446aa80e717d413db9ad50916e9cb"
graph = Graph("http://neo4j:neo@localhost:7474/db/data/")
class NeoDatabaseHelper(models.Model):
    def loadGroups(self):
        graph.delete_all()
        praveen=Node("Person", name="Praveen")
        graph.create(praveen)
        return "Success"
    def createCategories(self,response):
        check= response.read().decode('utf-8')
        # with open('D:/data.json', 'w') as f:
        #         json.loads(check, f,indent=4)

        # temp=json.loads(json.loads(check))
        with open('D:/data.json', mode='w', encoding='utf-8') as f:
            f.write(check)
        query="""
        CALL apoc.load.json("file:/D:/data.json") YIELD value
        with value.results as categories
        foreach (category in categories| create(cat:Category{name:category.name}))
        """
        query_select = """
                MATCH (cat:Category) RETURN {cat.name,cat.id, cat.shortname}
                """
        graph.run(query)
        res= graph.run(query_select)
        return res


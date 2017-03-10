package com.example.praveenkn.cloudmanagementclient;

import android.os.AsyncTask;
import android.os.Handler;
import android.os.Message;
import android.support.annotation.NonNull;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONStringer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URLConnection;
import java.net.URL;
import java.io.InputStream;
import java.io.PrintWriter;

/**
 * Created by Praveen Kn on 27-10-2016.
 */
public class ServiceComponent extends AsyncTask<String, Void, JSONObject>{

    JSONObject adminTokenReqObj = null;
    URLConnection urlConnection;
    Handler handler;
    URL url;
    Boolean forAddService=false;
    public JSONObject authenticateAdmin(String adminName, String adminPass) {
        adminTokenReqObj = createAuthTokenJson(adminName, adminPass);
       return startServiceRequest();
    }

    public JSONObject createAuthTokenJson(String adminName, String adminPass) {

        JSONObject adminAuthRequest = null;
        try {
            adminAuthRequest = new JSONObject("{\n" +
                    "    \"auth\": {\n" +
                    "        \"identity\": {\n" +
                    "            \"methods\": [\n" +
                    "                \"password\"\n" +
                    "            ],\n" +
                    "            \"password\": {\n" +
                    "                \"user\": {\n" +
                    "                    \"name\":" + adminName + "," + "\n" +
                    "                    \"password\":" + adminPass + "," + "\n" +
                    "                    \"domain\": {\n" +
                    "                               \"name\":\"Default\"\n" +
                    "                            }\n" +
                    "\n" +
                    "                }\n" +
                    "            }\n" +
                    "        }\n" +
                    "    }\n" +
                    "}");

        } catch (JSONException js) {

        }
        return adminAuthRequest;
    }
public  void createServerObject(String name) throws JSONException {
    adminTokenReqObj=new JSONObject("{\n" +
            "\"server\":{\n" +
            "\t\"name\":\""+name+"\""+
            ","+"\n"+"\t\"flavorRef\":\"2\",\n" +
            "\t\"imageRef\":\"41124c1d-feaf-466c-9478-bf138da5f25c\"\n" +
            "}\n"+
            "}");

}
    public void createServerEdit(String name) throws JSONException {
        adminTokenReqObj=new JSONObject("{\n" +
                "    \"server\": {\n" +
                "        \"accessIPv4\": \"4.3.2.1\",\n" +
                "        \"accessIPv6\": \"80fe::\",\n" +
                "        \"OS-DCF:diskConfig\": \"AUTO\",\n" +
                "        \"name\" :\""+name+"\"\n" +
                "    }\n"+
                "}");
    }
    private JSONObject startServiceRequest(){
       return  adminTokenReqObj;

    }
   /* public JSONObject createGetRequest(){

    }*/

    @Override
    protected JSONObject doInBackground(String... params) {
       return sendRequest(params);

    }
private JSONObject sendRequest(String... params){
    JSONObject jsonObj=null;
    HttpURLConnection urlConnection = null;
    URL url;
    BufferedReader readerResponse=null;
    String jsonString;

    int responseCode=0;
    try {
        url = new URL(params[0]);
      //  UtilityCloud.XAuthToken="gAAAAABYQUV6qaFJ3u6OQVcXX7UAZTQVOuQurUq7okNx3HP-ZHHazF3pwLymL2VepHb9gto-GqmZmkQR2hCxPZYPUcK3iiJ17m-knHzq9nl-E4Q1VBjRmKGGFHzurz2kTRKPiwMawXIfF3D8IrQq0xR9nR6ripkoBp62KYwSDMOua_y5JC_toAQ";
        urlConnection = (HttpURLConnection) url.openConnection();
        urlConnection.setRequestMethod(params[1]);
        urlConnection.setRequestProperty("Content-Type","application/json");
        urlConnection.setRequestProperty("X-Auth-Token",UtilityCloud.XAuthToken);
        if(params[1].equals("POST") || params[1].equals("PUT")){
            OutputStream outputStream=urlConnection.getOutputStream();
            OutputStreamWriter osw = new OutputStreamWriter(outputStream, "UTF-8");
            osw.write(adminTokenReqObj.toString());
            osw.flush();
            osw.close();
        }
        urlConnection.connect();
        StringBuilder sb = new StringBuilder();
        int HttpResult = urlConnection.getResponseCode();
        jsonObj=new JSONObject();
        if(params[1].equals("POST")){
            if(HttpResult==202){
                jsonObj = getJsonObject(jsonObj, urlConnection, sb);
                jsonObj.put("error",false);
            }
            else if(HttpResult==201) {
                UtilityCloud.XAuthToken=urlConnection.getHeaderField("X-Subject-Token");
                jsonObj = getJsonObject(jsonObj, urlConnection, sb);
                jsonObj.put("error",false);
            }else {
                System.out.println(urlConnection.getResponseMessage());
                jsonObj.put("error",true);
            }
        }else if(params[1].equals("GET")){
            if (HttpResult == 200) {
                String line;
                readerResponse = new BufferedReader(new
                        InputStreamReader(urlConnection.getInputStream()));
                while ((line = readerResponse.readLine()) != null) {
                    sb.append(line + '\n');
                }
                jsonString = sb.toString();
                jsonObj=new JSONObject(jsonString);
                jsonObj.put("response",true);
                jsonObj.put("error",false);

            }else {
                jsonObj=new JSONObject();
                jsonObj.put("error",true);
            }
        }else if(params[1].equals("DELETE")){
            if(HttpResult==204){
                jsonObj.put("response",true);
            }
        }else if(params[1].equals("PUT")){
            if(HttpResult==200){
                jsonObj.put("error",false);
            }else {
                jsonObj.put("error",false);
            }
        }
        urlConnection.disconnect();
    }
    catch (JSONException ex){
        ex.printStackTrace();
    }
    catch (Exception e) {
        e.printStackTrace();
    }
    return jsonObj;
}

    @NonNull
    private JSONObject getJsonObject(JSONObject jsonObj, HttpURLConnection urlConnection, StringBuilder sb) throws IOException, JSONException {
        BufferedReader readerResponse;
        String jsonString;
        String line;
        readerResponse = new BufferedReader(new
                InputStreamReader(urlConnection.getInputStream()));
        while ((line = readerResponse.readLine()) != null) {
            sb.append(line + '\n');
        }
        jsonString = sb.toString();
        jsonObj=new JSONObject(jsonString);
        jsonObj.put("XAuth","created");
        jsonObj.put("error",false);
        return jsonObj;
    }

    @Override
    protected void onPostExecute(JSONObject jsonObject) {
        super.onPostExecute(jsonObject);
        Message msg=handler.obtainMessage();
        msg.obj=jsonObject;
        handler.sendMessage(msg);
    }

    public void setHandler(Handler handler){
        this.handler=handler;
    }
}

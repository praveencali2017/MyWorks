package com.example.praveenkn.cloudmanagementclient;

import android.content.Intent;
import android.os.Handler;
import android.os.Message;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import com.example.praveenkn.cloudmanagementclient.Models.Server;

import org.json.JSONException;
import org.json.JSONObject;

import java.text.ParseException;

public class ServerMetaActivity extends AppCompatActivity {

    Handler serverMetaHandler=new Handler(){

        @Override
        public void handleMessage(Message msg) {
            super.handleMessage(msg);
            JSONObject obj=(JSONObject) msg.obj;
            if(obj!=null){
                renderDetails(obj);
            }
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_server_meta);
       Bundle bundle= getIntent().getExtras();
       String uuid= bundle.getString("UUID");
        sendMetaRequest(uuid);
    }
    private void sendMetaRequest(String uuid){
        ServiceComponent serviceComponent=new ServiceComponent();
        serviceComponent.setHandler(serverMetaHandler);
        serviceComponent.execute(UtilityCloud.serversRequestUrl+"/"+uuid,"GET");
    }
    private  void renderDetails(JSONObject jsonObject){
        TextView serverName=(TextView) findViewById(R.id.table_name_value);
        TextView serverID=(TextView) findViewById(R.id.table_id_value);
        TextView serverInstanceName=(TextView) findViewById(R.id.table_instancename_value);
        TextView serverZoneName=(TextView) findViewById(R.id.table_availabilityzone_value);
        TextView serverCreated=(TextView) findViewById(R.id.table_createdOn_value);
        if(jsonObject!=null){

            try {
                jsonObject=jsonObject.getJSONObject("server");
                serverName.setText(jsonObject.getString("name"));
                serverID.setText(jsonObject.getString("id"));
                serverInstanceName.setText(jsonObject.getString("OS-EXT-SRV-ATTR:instance_name"));
                serverZoneName.setText(jsonObject.getString("OS-EXT-AZ:availability_zone"));
                java.text.SimpleDateFormat dateFormat= new java.text.SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSS'Z'");
                serverCreated.setText(dateFormat.parse(jsonObject.getString("created")).toString());
            } catch (JSONException e) {
                e.printStackTrace();
            }catch (ParseException e) {
                e.printStackTrace();
            }
        }
    }
}

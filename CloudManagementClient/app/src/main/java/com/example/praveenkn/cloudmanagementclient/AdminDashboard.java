package com.example.praveenkn.cloudmanagementclient;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.view.View;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;
import android.widget.Toast;
import com.example.praveenkn.cloudmanagementclient.Models.Project;
import com.example.praveenkn.cloudmanagementclient.ItemFragment_Projects.OnListFragmentInteractionListener;
import com.example.praveenkn.cloudmanagementclient.Models.Server;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class AdminDashboard extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener, OnListFragmentInteractionListener, ItemFragment_Servers.OnListFragmentServersInteractionListener{
        TextView adminNameDashboardTxt;
    JSONObject responseJson;
   public Handler loginHandler= new Handler(){
        public void handleMessage(Message msg) {
            super.handleMessage(msg);
            try {
                responseJson = (JSONObject) msg.obj;
                ItemFragment_Projects itemFragmentProjects = new ItemFragment_Projects();
                itemFragmentProjects.setListItems(constructProjects(responseJson));
                FragmentManager manager = getSupportFragmentManager();
                FragmentTransaction fragmentTransaction = manager.beginTransaction();
                if (manager.getBackStackEntryCount() >= 0) {
                    fragmentTransaction.replace(R.id.frameLayout, itemFragmentProjects).commit();
                } else {
                    fragmentTransaction.add(R.id.frameLayout, itemFragmentProjects).commit();
                }

            }catch (Exception e){
                e.printStackTrace();
            }
        }
    };
    public  Handler serverHandler= new Handler(){
        @Override
        public void handleMessage(Message msg) {
            super.handleMessage(msg);
            try {
            responseJson=(JSONObject) msg.obj;
            ItemFragment_Servers serverFragment =new ItemFragment_Servers();
            serverFragment.setListItemsServers(constructServers(responseJson));
            serverFragment.setDeleteBtnHandler(delResponseHandler);
            serverFragment.setAddBtnHandler(addResponseHandler);
            serverFragment.setEditBtnHandler(editResponseHandler);
            FragmentManager manager=getSupportFragmentManager();
            FragmentTransaction fragmentTransaction=manager.beginTransaction();
            if(manager.getBackStackEntryCount()>=0){
                fragmentTransaction.replace(R.id.frameLayout, serverFragment).commit();
            }else {
                fragmentTransaction.add(R.id.frameLayout, serverFragment).commit();
            }
            }catch (Exception e){
                e.printStackTrace();
            }


        }
    };
    public Handler delResponseHandler=new Handler(){
        @Override
        public void handleMessage(Message msg) {
            super.handleMessage(msg);
            try {
                responseJson=(JSONObject) msg.obj;
                if(responseJson.getBoolean("response")==true){
                    serversService();
                }
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
    };
    public Handler addResponseHandler=new Handler(){
        @Override
        public void handleMessage(Message msg) {
            super.handleMessage(msg);
            try {
                responseJson=(JSONObject) msg.obj;
                if(responseJson.getBoolean("error")!=true){
                    serversService();
                }
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
    };
    public Handler editResponseHandler=new Handler(){
        @Override
        public void handleMessage(Message msg) {
            super.handleMessage(msg);
            try {
                responseJson=(JSONObject) msg.obj;
                if(responseJson.getBoolean("error")!=true){
                    serversService();
                }
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
    };
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_admin_dashboard);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        projectsService();
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.setDrawerListener(toggle);
        toggle.syncState();
        View v= getLayoutInflater().inflate(R.layout.nav_header_admin_dashboard,null);
        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);
        navigationView.setCheckedItem(R.id.projectsSide);
        adminNameDashboardTxt=((TextView)navigationView.getHeaderView(0).findViewById(R.id.adminName_dashboard));
        adminNameDashboardTxt.setText(UtilityCloud.userName);
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.admin_dashboard, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
       /* int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }
*/
        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        if (id == R.id.projectsSide) {
           // Toast.makeText(AdminDashboard.this,"Will list projects",Toast.LENGTH_SHORT).show();
            projectsService();
        }else if(id==R.id.servers){
            serversService();
        }
        else if (id == R.id.logout_admin) {
            SharedPreferences sharedPreferences= getSharedPreferences(UtilityCloud.userPrefName,Context.MODE_PRIVATE);
            SharedPreferences.Editor editor = sharedPreferences.edit();
            editor.remove(UtilityCloud.userName);
            editor.remove(UtilityCloud.userName+"_key");
            editor.remove("user");
            editor.commit();
            finish();
        }
        return true;
    }
public void projectsService(){
    ServiceComponent serviceComponent=new ServiceComponent();
    serviceComponent.setHandler(loginHandler);
    serviceComponent.execute(UtilityCloud.projectsRequestUrl,"GET");
}
    public void serversService(){
        ServiceComponent serviceComponent=new ServiceComponent();
        serviceComponent.setHandler(serverHandler);
        serviceComponent.execute(UtilityCloud.serversRequestUrl,"GET");
    }
    public List<Project> constructProjects(JSONObject obj){
        List<Project> projects=new ArrayList<Project>();
        JSONArray jsonProjects=new JSONArray();
        try {
            if (!obj.getBoolean("error")) {
                jsonProjects=obj.getJSONArray("projects");
                for (int i=0;i<jsonProjects.length();i++){
                    Project project=new Project();
                    project.projectName=((JSONObject)jsonProjects.get(i)).getString("name");
                    project.description=((JSONObject)jsonProjects.get(i)).getString("description");
                    projects.add(project);
                }
            }else {
                Toast.makeText(this,"errroeeeeeeeeee",Toast.LENGTH_SHORT).show();
            }
        }catch (JSONException ex){

        }
        return projects;
    }
    public List<Server> constructServers(JSONObject obj){
        List<Server> servers=new ArrayList<Server>();
        JSONArray jsonServers=new JSONArray();
        try {
            if (!obj.getBoolean("error")) {
                jsonServers=obj.getJSONArray("servers");
                for (int i=0;i<jsonServers.length();i++){
                    Server server=new Server();
                    server.serverName=((JSONObject)jsonServers.get(i)).getString("name");
                    server.serverUUID=((JSONObject)jsonServers.get(i)).getString("id");
                    servers.add(server);
                }
            }else {
                Toast.makeText(this,"errroeeeeeeeeee",Toast.LENGTH_SHORT).show();
            }
        }catch (JSONException ex){

        }
        return  servers;
    }
    @Override
    public void onListFragmentInteraction(Project proj) {
        Toast.makeText(this,proj.projectName,Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onListFragmentInteraction(Server item) {
        //Toast.makeText(this,item.serverName,Toast.LENGTH_SHORT).show();
        Intent serverMeta=new Intent(AdminDashboard.this,ServerMetaActivity.class);
        serverMeta.putExtra("UUID",item.serverUUID);
        startActivity(serverMeta);
    }
}

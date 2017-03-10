package com.example.praveenkn.cloudmanagementclient;

/**
 * Created by Praveen Kn on 29-11-2016.
 */
public class UtilityCloud {
    public static String XAuthToken;
    public static String tokenRequestUrl="http://192.168.56.101:5000/v3/auth/tokens";
    public static String projectsRequestUrl="http://192.168.56.101:5000/v3/projects";
    public static String serversRequestUrl="http://192.168.56.101:8774/v2.1/servers";
    public static String userName="";
    public static final String userPrefName="user-info";
}

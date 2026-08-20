package com.simats.symptocareappfrontend.models;

import java.util.List;

public class Hospital {
    public String id;
    public String name;
    public String type;
    public double rating;
    public int review_count;
    public String phone;
    public String emergency_phone;
    public String address;
    public double lat;
    public double lng;
    public String city;
    public boolean emergency;
    public int beds;
    public List<Department> departments;
    public List<String> specialists;
    public String distance;
}

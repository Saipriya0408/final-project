package com.simats.symptocareappfrontend.models;

import java.util.List;

public class Doctor {
    public String id;
    public String name;
    public String specialist;
    public String hospital;
    public boolean available;
    public boolean available_today;
    public double rating;
    public int review_count;
    public int experience_years;
    public int consultation_fee;
    public List<String> time_slots;
    public String phone;
    public double lat;
    public double lng;
    public String qualification;
    public String address;
    public String city;
    public List<String> languages;
    public String distance;
}

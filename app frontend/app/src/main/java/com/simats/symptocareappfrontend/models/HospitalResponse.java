package com.simats.symptocareappfrontend.models;

import java.util.List;

public class HospitalResponse {
    public boolean success;
    public Data data;

    public static class Data {
        public int total;
        public List<Hospital> hospitals;
    }
}

package com.simats.symptocareappfrontend.models;

import java.util.List;

public class DoctorResponse {
    public boolean success;
    public Data data;

    public static class Data {
        public int total;
        public List<Doctor> doctors;
    }
}

package com.simats.symptocareappfrontend.models;

import java.util.List;

public class AnalysisResponse {
    public boolean success;
    public Data data;

    public static class Data {
        public String predictedDisease;
        public String recommendedSpecialist;
        public double confidence;
        public String diseaseDescription;
        public String severityLevel;
        public List<String> precautions;
        public List<String> normalizedSymptoms;
    }
}

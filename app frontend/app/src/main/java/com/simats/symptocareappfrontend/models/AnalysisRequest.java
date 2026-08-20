package com.simats.symptocareappfrontend.models;

import java.util.List;

public class AnalysisRequest {
    public String message;
    public List<String> symptoms;

    public AnalysisRequest(String message) {
        this.message = message;
    }

    public AnalysisRequest(List<String> symptoms) {
        this.symptoms = symptoms;
    }
}

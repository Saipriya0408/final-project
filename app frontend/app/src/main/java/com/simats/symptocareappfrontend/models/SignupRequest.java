package com.simats.symptocareappfrontend.models;

public class SignupRequest {
    private String name;
    private String phone;
    private String email;
    private String password;

    public SignupRequest(String name, String phone, String email, String password) {
        this.name = name;
        this.phone = phone;
        this.email = email;
        this.password = password;
    }
}

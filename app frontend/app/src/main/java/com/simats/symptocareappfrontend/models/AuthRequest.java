package com.simats.symptocareappfrontend.models;

public class AuthRequest {
    private String email_or_phone;
    private String password;

    public AuthRequest(String email_or_phone, String password) {
        this.email_or_phone = email_or_phone;
        this.password = password;
    }
}

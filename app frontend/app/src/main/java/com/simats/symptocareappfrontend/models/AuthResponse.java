package com.simats.symptocareappfrontend.models;

public class AuthResponse {
    private boolean success;
    private Data data;
    private Error error;

    public boolean isSuccess() { return success; }
    public Data getData() { return data; }
    public Error getError() { return error; }

    public static class Data {
        private User user;
        private String token;

        public User getUser() { return user; }
        public String getToken() { return token; }
    }

    public static class User {
        private int id;
        private String name;
        private String phone;
        private String email;

        public int getId() { return id; }
        public String getName() { return name; }
        public String getPhone() { return phone; }
        public String getEmail() { return email; }
    }

    public static class Error {
        private String message;
        public String getMessage() { return message; }
    }
}

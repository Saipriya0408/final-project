import os

base_path = r"C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\java\com\simats\symptocareappfrontend\models"
os.makedirs(base_path, exist_ok=True)

doctor_java = """package com.simats.symptocareappfrontend.models;

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
}
"""

doctor_response_java = """package com.simats.symptocareappfrontend.models;

import java.util.List;

public class DoctorResponse {
    public String status;
    public Data data;

    public static class Data {
        public int total;
        public List<Doctor> doctors;
    }
}
"""

hospital_java = """package com.simats.symptocareappfrontend.models;

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
}
"""

department_java = """package com.simats.symptocareappfrontend.models;

public class Department {
    public String name;
    public boolean available;
}
"""

hospital_response_java = """package com.simats.symptocareappfrontend.models;

import java.util.List;

public class HospitalResponse {
    public String status;
    public Data data;

    public static class Data {
        public int total;
        public List<Hospital> hospitals;
    }
}
"""

files = {
    "Doctor.java": doctor_java,
    "DoctorResponse.java": doctor_response_java,
    "Hospital.java": hospital_java,
    "Department.java": department_java,
    "HospitalResponse.java": hospital_response_java
}

for filename, content in files.items():
    with open(os.path.join(base_path, filename), "w") as f:
        f.write(content)

print("Java model classes created successfully.")

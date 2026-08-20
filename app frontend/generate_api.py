import os

base_path = r"C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\java\com\simats\symptocareappfrontend\api"
os.makedirs(base_path, exist_ok=True)

apiclient_java = """package com.simats.symptocareappfrontend.api;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class ApiClient {
    private static final String BASE_URL = "http://192.168.1.4:5000/api/";
    private static Retrofit retrofit = null;

    public static Retrofit getClient() {
        if (retrofit == null) {
            retrofit = new Retrofit.Builder()
                    .baseUrl(BASE_URL)
                    .addConverterFactory(GsonConverterFactory.create())
                    .build();
        }
        return retrofit;
    }
}
"""

apiservice_java = """package com.simats.symptocareappfrontend.api;

import com.simats.symptocareappfrontend.models.DoctorResponse;
import com.simats.symptocareappfrontend.models.HospitalResponse;

import retrofit2.Call;
import retrofit2.http.GET;

public interface ApiService {
    @GET("doctors")
    Call<DoctorResponse> getDoctors();

    @GET("hospitals")
    Call<HospitalResponse> getHospitals();
}
"""

files = {
    "ApiClient.java": apiclient_java,
    "ApiService.java": apiservice_java
}

for filename, content in files.items():
    with open(os.path.join(base_path, filename), "w") as f:
        f.write(content)

print("Network API classes created successfully.")

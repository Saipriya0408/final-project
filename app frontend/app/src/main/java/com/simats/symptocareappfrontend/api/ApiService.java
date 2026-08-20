package com.simats.symptocareappfrontend.api;

import com.simats.symptocareappfrontend.models.DoctorResponse;
import com.simats.symptocareappfrontend.models.HospitalResponse;

import com.simats.symptocareappfrontend.models.AnalysisRequest;
import com.simats.symptocareappfrontend.models.AnalysisResponse;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;

import retrofit2.http.Query;

import com.simats.symptocareappfrontend.models.AuthRequest;
import com.simats.symptocareappfrontend.models.AuthResponse;
import com.simats.symptocareappfrontend.models.SignupRequest;

public interface ApiService {
    @GET("doctors")
    Call<DoctorResponse> getDoctors(
            @Query("specialist") String specialist,
            @Query("lat") Double lat,
            @Query("lng") Double lng,
            @Query("offset") Integer offset,
            @Query("limit") Integer limit
    );

    @GET("hospitals")
    Call<HospitalResponse> getHospitals(
            @Query("lat") Double lat,
            @Query("lng") Double lng
    );

    @POST("analyze-symptoms")
    Call<AnalysisResponse> analyzeSymptoms(@Body AnalysisRequest request);

    @POST("auth/signup")
    Call<AuthResponse> signup(@Body SignupRequest request);

    @POST("auth/login")
    Call<AuthResponse> login(@Body AuthRequest request);
}

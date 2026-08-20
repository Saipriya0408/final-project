import os

base_pkg = r"C:\Users\srike\Desktop\WORK\CODE CURRENT\projects\Sympto Care\app frontend\app\src\main\java\com\simats\symptocareappfrontend"
adapters_path = os.path.join(base_pkg, "adapters")
os.makedirs(adapters_path, exist_ok=True)

doctor_adapter_java = """package com.simats.symptocareappfrontend.adapters;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import com.simats.symptocareappfrontend.R;
import com.simats.symptocareappfrontend.models.Doctor;
import java.util.ArrayList;
import java.util.List;

public class DoctorAdapter extends RecyclerView.Adapter<DoctorAdapter.DoctorViewHolder> {

    private List<Doctor> doctors = new ArrayList<>();

    public void setDoctors(List<Doctor> doctors) {
        this.doctors = doctors;
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public DoctorViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_doctor, parent, false);
        return new DoctorViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull DoctorViewHolder holder, int position) {
        Doctor doc = doctors.get(position);
        holder.tvDrName.setText(doc.name);
        holder.tvDrSpec.setText(doc.specialist);
        holder.tvRating.setText("⭐ " + doc.rating + " (" + doc.review_count + ")");
        holder.tvExperience.setText(doc.experience_years + " years");
        holder.tvFee.setText("Rs." + doc.consultation_fee);
        
        // Handle avatar initials
        if(doc.name != null && doc.name.length() > 0) {
            String[] parts = doc.name.replace("Dr. ", "").split(" ");
            StringBuilder initials = new StringBuilder();
            for(String p : parts) {
                if(p.length() > 0) initials.append(p.charAt(0));
            }
            holder.ivAvatar.setText(initials.toString().toUpperCase());
        }

        holder.tvAvailableBadge.setVisibility(doc.available ? View.VISIBLE : View.GONE);
        holder.tvAvailableToday.setVisibility(doc.available_today ? View.VISIBLE : View.GONE);

        // Map timeslots dynamically if they exist
        holder.tvTime1.setVisibility(View.GONE);
        holder.tvTime2.setVisibility(View.GONE);
        holder.tvTime3.setVisibility(View.GONE);
        if(doc.time_slots != null) {
            if(doc.time_slots.size() > 0) { holder.tvTime1.setText(doc.time_slots.get(0)); holder.tvTime1.setVisibility(View.VISIBLE); }
            if(doc.time_slots.size() > 1) { holder.tvTime2.setText(doc.time_slots.get(1)); holder.tvTime2.setVisibility(View.VISIBLE); }
            if(doc.time_slots.size() > 2) { holder.tvTime3.setText(doc.time_slots.get(2)); holder.tvTime3.setVisibility(View.VISIBLE); }
        }
    }

    @Override
    public int getItemCount() {
        return doctors != null ? doctors.size() : 0;
    }

    static class DoctorViewHolder extends RecyclerView.ViewHolder {
        TextView tvDrName, tvDrSpec, tvRating, tvExperience, tvFee, ivAvatar, tvAvailableBadge, tvAvailableToday;
        TextView tvTime1, tvTime2, tvTime3;

        public DoctorViewHolder(@NonNull View itemView) {
            super(itemView);
            tvDrName = itemView.findViewById(R.id.tvDrName);
            tvDrSpec = itemView.findViewById(R.id.tvDrSpec);
            tvRating = itemView.findViewById(R.id.tvRating);
            tvExperience = itemView.findViewById(R.id.tvExperience);
            tvFee = itemView.findViewById(R.id.tvFee);
            ivAvatar = itemView.findViewById(R.id.ivAvatar);
            tvAvailableBadge = itemView.findViewById(R.id.tvAvailableBadge);
            tvAvailableToday = itemView.findViewById(R.id.tvAvailableToday);
            tvTime1 = itemView.findViewById(R.id.tvTime1);
            tvTime2 = itemView.findViewById(R.id.tvTime2);
            tvTime3 = itemView.findViewById(R.id.tvTime3);
        }
    }
}
"""

hospital_adapter_java = """package com.simats.symptocareappfrontend.adapters;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import com.simats.symptocareappfrontend.R;
import com.simats.symptocareappfrontend.models.Hospital;
import java.util.ArrayList;
import java.util.List;

public class HospitalAdapter extends RecyclerView.Adapter<HospitalAdapter.HospitalViewHolder> {

    private List<Hospital> hospitals = new ArrayList<>();

    public void setHospitals(List<Hospital> hospitals) {
        this.hospitals = hospitals;
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public HospitalViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_hospital, parent, false);
        return new HospitalViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull HospitalViewHolder holder, int position) {
        Hospital hosp = hospitals.get(position);
        holder.tvHospName.setText(hosp.name);
        holder.tvHospAddress.setText(hosp.address);
        holder.tvHospRating.setText("⭐ " + hosp.rating + " (" + hosp.review_count + ")");
        
        holder.tvEmergencyBadge.setVisibility(hosp.emergency ? View.VISIBLE : View.GONE);
        
        // Handle departments
        holder.tvDept1.setVisibility(View.GONE);
        holder.tvDept2.setVisibility(View.GONE);
        holder.tvDept3.setVisibility(View.GONE);
        holder.tvDeptMore.setVisibility(View.GONE);
        
        if (hosp.departments != null) {
            if(hosp.departments.size() > 0) { holder.tvDept1.setText(hosp.departments.get(0).name); holder.tvDept1.setVisibility(View.VISIBLE); }
            if(hosp.departments.size() > 1) { holder.tvDept2.setText(hosp.departments.get(1).name); holder.tvDept2.setVisibility(View.VISIBLE); }
            if(hosp.departments.size() > 2) { holder.tvDept3.setText(hosp.departments.get(2).name); holder.tvDept3.setVisibility(View.VISIBLE); }
            if(hosp.departments.size() > 3) {
                holder.tvDeptMore.setText("+" + (hosp.departments.size() - 3) + " more");
                holder.tvDeptMore.setVisibility(View.VISIBLE);
            }
        }
    }

    @Override
    public int getItemCount() {
        return hospitals != null ? hospitals.size() : 0;
    }

    static class HospitalViewHolder extends RecyclerView.ViewHolder {
        TextView tvHospName, tvHospAddress, tvHospRating, tvEmergencyBadge;
        TextView tvDept1, tvDept2, tvDept3, tvDeptMore;

        public HospitalViewHolder(@NonNull View itemView) {
            super(itemView);
            tvHospName = itemView.findViewById(R.id.tvHospName);
            tvHospAddress = itemView.findViewById(R.id.tvHospAddress);
            tvHospRating = itemView.findViewById(R.id.tvHospRating);
            tvEmergencyBadge = itemView.findViewById(R.id.tvEmergencyBadge);
            tvDept1 = itemView.findViewById(R.id.tvDept1);
            tvDept2 = itemView.findViewById(R.id.tvDept2);
            tvDept3 = itemView.findViewById(R.id.tvDept3);
            tvDeptMore = itemView.findViewById(R.id.tvDeptMore);
        }
    }
}
"""

doctors_fragment_java = """package com.simats.symptocareappfrontend;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.simats.symptocareappfrontend.adapters.DoctorAdapter;
import com.simats.symptocareappfrontend.api.ApiClient;
import com.simats.symptocareappfrontend.api.ApiService;
import com.simats.symptocareappfrontend.models.DoctorResponse;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class DoctorsFragment extends Fragment {

    private RecyclerView rvDoctors;
    private DoctorAdapter adapter;
    private TextView tvDoctorsFound;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_doctors, container, false);
        
        rvDoctors = view.findViewById(R.id.rvDoctors);
        tvDoctorsFound = view.findViewById(R.id.tvDoctorsFound);
        
        rvDoctors.setLayoutManager(new LinearLayoutManager(getContext()));
        adapter = new DoctorAdapter();
        rvDoctors.setAdapter(adapter);

        fetchDoctors();

        return view;
    }

    private void fetchDoctors() {
        ApiService apiService = ApiClient.getClient().create(ApiService.class);
        apiService.getDoctors().enqueue(new Callback<DoctorResponse>() {
            @Override
            public void onResponse(Call<DoctorResponse> call, Response<DoctorResponse> response) {
                if (response.isSuccessful() && response.body() != null) {
                    if ("success".equals(response.body().status)) {
                        adapter.setDoctors(response.body().data.doctors);
                        tvDoctorsFound.setText(response.body().data.total + " doctors found");
                    }
                } else {
                    Toast.makeText(getContext(), "Failed to fetch doctors", Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<DoctorResponse> call, Throwable t) {
                Log.e("API_ERROR", "Error: " + t.getMessage());
                Toast.makeText(getContext(), "Network error", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
"""

hospitals_fragment_java = """package com.simats.symptocareappfrontend;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.simats.symptocareappfrontend.adapters.HospitalAdapter;
import com.simats.symptocareappfrontend.api.ApiClient;
import com.simats.symptocareappfrontend.api.ApiService;
import com.simats.symptocareappfrontend.models.HospitalResponse;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class HospitalsFragment extends Fragment {

    private RecyclerView rvHospitals;
    private HospitalAdapter adapter;
    private TextView tvHospitalsFound;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_hospitals, container, false);
        
        rvHospitals = view.findViewById(R.id.rvHospitals);
        tvHospitalsFound = view.findViewById(R.id.tvHospitalsFound);
        
        rvHospitals.setLayoutManager(new LinearLayoutManager(getContext()));
        adapter = new HospitalAdapter();
        rvHospitals.setAdapter(adapter);

        fetchHospitals();

        return view;
    }

    private void fetchHospitals() {
        ApiService apiService = ApiClient.getClient().create(ApiService.class);
        apiService.getHospitals().enqueue(new Callback<HospitalResponse>() {
            @Override
            public void onResponse(Call<HospitalResponse> call, Response<HospitalResponse> response) {
                if (response.isSuccessful() && response.body() != null) {
                    if ("success".equals(response.body().status)) {
                        adapter.setHospitals(response.body().data.hospitals);
                        tvHospitalsFound.setText(response.body().data.total + " hospitals found");
                    }
                } else {
                    Toast.makeText(getContext(), "Failed to fetch hospitals", Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<HospitalResponse> call, Throwable t) {
                Log.e("API_ERROR", "Error: " + t.getMessage());
                Toast.makeText(getContext(), "Network error", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
"""

files = {
    os.path.join(adapters_path, "DoctorAdapter.java"): doctor_adapter_java,
    os.path.join(adapters_path, "HospitalAdapter.java"): hospital_adapter_java,
    os.path.join(base_pkg, "DoctorsFragment.java"): doctors_fragment_java,
    os.path.join(base_pkg, "HospitalsFragment.java"): hospitals_fragment_java
}

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Adapters and Fragments updated successfully.")

package com.simats.symptocareappfrontend;

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

import android.Manifest;
import android.content.pm.PackageManager;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.core.content.ContextCompat;
import com.google.android.gms.location.FusedLocationProviderClient;
import com.google.android.gms.location.LocationServices;
import android.content.Intent;
import android.provider.Settings;
import androidx.appcompat.app.AlertDialog;
import android.widget.ProgressBar;

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
    
    private FusedLocationProviderClient fusedLocationClient;
    private final ActivityResultLauncher<String[]> locationPermissionRequest = registerForActivityResult(
        new ActivityResultContracts.RequestMultiplePermissions(),
        result -> {
            Boolean fineLocationGranted = result.getOrDefault(Manifest.permission.ACCESS_FINE_LOCATION, false);
            Boolean coarseLocationGranted = result.getOrDefault(Manifest.permission.ACCESS_COARSE_LOCATION, false);
            if (fineLocationGranted != null && fineLocationGranted) {
                getCurrentLocation();
            } else if (coarseLocationGranted != null && coarseLocationGranted) {
                getCurrentLocation();
            } else {
                if (getContext() != null) {
                    Toast.makeText(getContext(), "Location permission is required to find nearby doctors and hospitals.", Toast.LENGTH_LONG).show();
                }
            }
        }
    );
    private TextView tvLocationTitle;
    private TextView tvLocationDesc;
    private TextView btnLocationAction;
    private AlertDialog progressDialog;
    private boolean isFetchingLocation = false;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_hospitals, container, false);
        
        rvHospitals = view.findViewById(R.id.rvHospitals);
        tvHospitalsFound = view.findViewById(R.id.tvHospitalsFound);
        
        rvHospitals.setLayoutManager(new LinearLayoutManager(getContext()));
        adapter = new HospitalAdapter();
        rvHospitals.setAdapter(adapter);

        fusedLocationClient = LocationServices.getFusedLocationProviderClient(requireActivity());

        tvLocationTitle = view.findViewById(R.id.tvLocationTitle);
        tvLocationDesc = view.findViewById(R.id.tvLocationDesc);
        btnLocationAction = view.findViewById(R.id.btnLocationAction);
        if (btnLocationAction != null) {
            btnLocationAction.setOnClickListener(v -> checkLocationPermission());
        }

        updateLocationUiState("normal");

        fetchHospitals();

        return view;
    }

    private void showLoading(String message) {
        if (progressDialog == null && getContext() != null) {
            AlertDialog.Builder builder = new AlertDialog.Builder(getContext());
            ProgressBar progressBar = new ProgressBar(getContext());
            progressBar.setPadding(40, 40, 40, 40);
            builder.setView(progressBar);
            builder.setMessage(message);
            builder.setCancelable(false);
            progressDialog = builder.create();
        }
        if (progressDialog != null && !progressDialog.isShowing()) {
            progressDialog.setMessage(message);
            progressDialog.show();
        }
    }

    private void hideLoading() {
        if (progressDialog != null && progressDialog.isShowing()) {
            progressDialog.dismiss();
        }
    }

    @Override
    public void onResume() {
        super.onResume();
        if (getActivity() != null) {
            android.content.SharedPreferences prefs = getActivity().getSharedPreferences("AppPrefs", android.content.Context.MODE_PRIVATE);
            if (prefs.getBoolean("should_retry_location", false)) {
                prefs.edit().remove("should_retry_location").apply();
                if (isLocationEnabled()) {
                    getCurrentLocation();
                } else {
                    Toast.makeText(getContext(), "Location is still disabled.", Toast.LENGTH_SHORT).show();
                }
            }
        }
    }

    private boolean isLocationEnabled() {
        if (getContext() == null) return false;
        android.location.LocationManager lm = (android.location.LocationManager) requireContext().getSystemService(android.content.Context.LOCATION_SERVICE);
        boolean gps_enabled = false;
        boolean network_enabled = false;
        try {
            gps_enabled = lm.isProviderEnabled(android.location.LocationManager.GPS_PROVIDER);
        } catch(Exception ex) {}
        try {
            network_enabled = lm.isProviderEnabled(android.location.LocationManager.NETWORK_PROVIDER);
        } catch(Exception ex) {}
        return gps_enabled || network_enabled;
    }

    private void checkLocationPermission() {
        if (ContextCompat.checkSelfPermission(requireContext(), Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED) {
            getCurrentLocation();
        } else if (shouldShowRequestPermissionRationale(Manifest.permission.ACCESS_FINE_LOCATION)) {
            showPermissionRationaleDialog();
        } else {
            if (getContext() != null) {
                android.content.SharedPreferences prefs = requireActivity().getSharedPreferences("AppPrefs", android.content.Context.MODE_PRIVATE);
                boolean alreadyRequested = prefs.getBoolean("location_permission_requested", false);
                if (alreadyRequested) {
                    updateLocationUiState("permission_denied");
                    showPermanentlyDeniedDialog();
                } else {
                    prefs.edit().putBoolean("location_permission_requested", true).apply();
                    showPermissionRationaleDialog();
                }
            }
        }
    }

    private void showPermissionRationaleDialog() {
        new AlertDialog.Builder(requireContext())
            .setTitle("Location Permission Required")
            .setMessage("SymptoCare requires your location to find nearby doctors and hospitals within a 25 km radius.")
            .setPositiveButton("Allow", (dialog, which) -> {
                locationPermissionRequest.launch(new String[]{
                    Manifest.permission.ACCESS_FINE_LOCATION,
                    Manifest.permission.ACCESS_COARSE_LOCATION
                });
            })
            .setNegativeButton("Don't allow", (dialog, which) -> {
                updateLocationUiState("permission_denied");
                Toast.makeText(getContext(), "Location permission is required to show nearby doctors and hospitals.", Toast.LENGTH_LONG).show();
            })
            .setCancelable(false)
            .show();
    }

    private void showPermanentlyDeniedDialog() {
        new AlertDialog.Builder(requireContext())
            .setTitle("Permission Permanently Denied")
            .setMessage("You have permanently denied location permission. Please enable it in the App Settings to find nearby doctors and hospitals.")
            .setPositiveButton("Go to Settings", (dialog, which) -> {
                Intent intent = new Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS);
                android.net.Uri uri = android.net.Uri.fromParts("package", requireActivity().getPackageName(), null);
                intent.setData(uri);
                startActivity(intent);
            })
            .setNegativeButton("Cancel", null)
            .setCancelable(false)
            .show();
    }

    private void updateLocationUiState(String state) {
        if (tvLocationTitle == null || tvLocationDesc == null || btnLocationAction == null) return;
        
        switch (state) {
            case "normal":
                tvLocationTitle.setText("Find Nearby Healthcare");
                tvLocationDesc.setText("Use your current location to find doctors, clinics and hospitals near you.");
                btnLocationAction.setText("📍 Use My Location");
                btnLocationAction.setVisibility(View.VISIBLE);
                break;
            case "loading":
                tvLocationTitle.setText("📍 Finding nearby healthcare...");
                tvLocationDesc.setText("Please wait.");
                btnLocationAction.setVisibility(View.GONE);
                break;
            case "enabled":
                tvLocationTitle.setText("✓ Location enabled");
                tvLocationDesc.setText("Showing healthcare near you");
                btnLocationAction.setText("🔄 Refresh Location");
                btnLocationAction.setVisibility(View.VISIBLE);
                break;
            case "permission_denied":
                tvLocationTitle.setText("📍 Location Permission Required");
                tvLocationDesc.setText("Allow location access to find nearby healthcare.");
                btnLocationAction.setText("Allow Location");
                btnLocationAction.setVisibility(View.VISIBLE);
                break;
            case "gps_off":
                tvLocationTitle.setText("📍 Location is turned off");
                tvLocationDesc.setText("Turn on Location to find nearby doctors and hospitals.");
                btnLocationAction.setText("Turn On Location");
                btnLocationAction.setVisibility(View.VISIBLE);
                break;
            case "no_results":
                tvLocationTitle.setText("No nearby hospitals or clinics found.");
                tvLocationDesc.setText("Try refreshing your location.");
                btnLocationAction.setText("🔄 Refresh Location");
                btnLocationAction.setVisibility(View.VISIBLE);
                break;
            case "unable_to_connect":
                tvLocationTitle.setText("⚠ Unable to connect to server");
                tvLocationDesc.setText("Please check that the SymptoCare server is running.");
                btnLocationAction.setText("Retry");
                btnLocationAction.setVisibility(View.VISIBLE);
                break;
        }
    }

    private void getCurrentLocation() {
        if (ContextCompat.checkSelfPermission(requireContext(), Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) return;
        
        if (!isLocationEnabled()) {
            updateLocationUiState("gps_off");
            new AlertDialog.Builder(requireContext())
                .setTitle("Location is turned off")
                .setMessage("Please turn on Location to find nearby doctors and hospitals.")
                .setPositiveButton("Turn On Location", (dialog, which) -> {
                    if (getActivity() != null) {
                        getActivity().getSharedPreferences("AppPrefs", android.content.Context.MODE_PRIVATE)
                            .edit().putBoolean("should_retry_location", true).apply();
                    }
                    Intent intent = new Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS);
                    startActivity(intent);
                })
                .setNegativeButton("Cancel", null)
                .setCancelable(false)
                .show();
            return;
        }

        showLoading("Finding nearby hospitals...");
        isFetchingLocation = true;
        updateLocationUiState("loading");
        
        fusedLocationClient.getLastLocation().addOnSuccessListener(requireActivity(), location -> {
            if (location != null) {
                Log.d("LOCATION", "Location permission granted");
                Log.d("LOCATION", "Location services enabled");
                Log.d("LOCATION", "Requesting current location");
                Log.d("LOCATION", "Location received");
                Log.d("LOCATION", "Latitude: " + location.getLatitude());
                Log.d("LOCATION", "Longitude: " + location.getLongitude());
                if (getActivity() != null) {
                    android.content.SharedPreferences prefs = getActivity().getSharedPreferences("AppPrefs", android.content.Context.MODE_PRIVATE);
                    prefs.edit().putFloat("user_lat", (float) location.getLatitude())
                                .putFloat("user_lng", (float) location.getLongitude()).apply();
                }
                updateLocationUiState("enabled");
                fetchHospitals();
            } else {
                hideLoading();
                isFetchingLocation = false;
                updateLocationUiState("normal");
                Toast.makeText(getContext(), "Unable to obtain location. Please retry.", Toast.LENGTH_LONG).show();
            }
        }).addOnFailureListener(e -> {
            hideLoading();
            isFetchingLocation = false;
            updateLocationUiState("normal");
            Toast.makeText(getContext(), "Error getting location: " + e.getMessage(), Toast.LENGTH_SHORT).show();
        });
    }

    private void fetchHospitals() {
        Double userLat = null;
        Double userLng = null;
        if (getActivity() != null) {
            android.content.SharedPreferences prefs = getActivity().getSharedPreferences("AppPrefs", android.content.Context.MODE_PRIVATE);
            if (prefs.contains("user_lat") && prefs.contains("user_lng")) {
                userLat = (double) prefs.getFloat("user_lat", 0);
                userLng = (double) prefs.getFloat("user_lng", 0);
            }
        }

        ApiService apiService = ApiClient.getClient().create(ApiService.class);
        apiService.getHospitals(userLat, userLng).enqueue(new Callback<HospitalResponse>() {
            @Override
            public void onResponse(Call<HospitalResponse> call, Response<HospitalResponse> response) {
                if (isFetchingLocation) {
                    hideLoading();
                    isFetchingLocation = false;
                }
                if (response.isSuccessful() && response.body() != null) {
                    if (response.body().success) {
                        adapter.setHospitals(response.body().data.hospitals);
                        tvHospitalsFound.setText(response.body().data.total + " hospitals found");
                        if (response.body().data.total == 0) {
                            updateLocationUiState("no_results");
                            Toast.makeText(getContext(), "No nearby hospitals found.", Toast.LENGTH_SHORT).show();
                        }
                    }
                } else {
                    updateLocationUiState("normal");
                    Toast.makeText(getContext(), "Failed to fetch hospitals", Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<HospitalResponse> call, Throwable t) {
                if (isFetchingLocation) {
                    hideLoading();
                    isFetchingLocation = false;
                }
                Log.e("API_ERROR", "Error: " + t.getMessage());
                if (getContext() != null) {
                    updateLocationUiState("unable_to_connect");
                }
            }
        });
    }
}

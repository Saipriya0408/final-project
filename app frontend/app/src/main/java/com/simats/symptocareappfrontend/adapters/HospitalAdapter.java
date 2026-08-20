package com.simats.symptocareappfrontend.adapters;

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
        
        String type = hosp.type;
        if (type == null || type.isEmpty()) {
            if (hosp.name != null && (hosp.name.toLowerCase().contains("clinic") || hosp.name.toLowerCase().contains("center") || hosp.name.toLowerCase().contains("care"))) {
                type = "Clinic";
            } else {
                type = "Hospital";
            }
        }
        
        if (hosp.distance != null) {
            holder.tvHospRating.setText(type + "  ⭐ " + hosp.rating + " (" + hosp.review_count + ")  📍 " + hosp.distance);
        } else {
            holder.tvHospRating.setText(type + "  ⭐ " + hosp.rating + " (" + hosp.review_count + ")");
        }
        
        holder.tvEmergencyBadge.setVisibility(hosp.emergency ? View.VISIBLE : View.GONE);
        
        // Handle specialists
        holder.tvDept1.setVisibility(View.GONE);
        holder.tvDept2.setVisibility(View.GONE);
        holder.tvDept3.setVisibility(View.GONE);
        holder.tvDeptMore.setVisibility(View.GONE);
        
        if (hosp.specialists != null) {
            if(hosp.specialists.size() > 0) { holder.tvDept1.setText(hosp.specialists.get(0)); holder.tvDept1.setVisibility(View.VISIBLE); }
            if(hosp.specialists.size() > 1) { holder.tvDept2.setText(hosp.specialists.get(1)); holder.tvDept2.setVisibility(View.VISIBLE); }
            if(hosp.specialists.size() > 2) { holder.tvDept3.setText(hosp.specialists.get(2)); holder.tvDept3.setVisibility(View.VISIBLE); }
            if(hosp.specialists.size() > 3) {
                holder.tvDeptMore.setText("+" + (hosp.specialists.size() - 3) + " more");
                holder.tvDeptMore.setVisibility(View.VISIBLE);
            }
        }
        
        holder.itemView.setOnClickListener(v -> {
            android.content.Intent intent = new android.content.Intent(v.getContext(), com.simats.symptocareappfrontend.HospitalProfileActivity.class);
            intent.putExtra("hosp_name", hosp.name);
            intent.putExtra("hosp_address", hosp.address);
            intent.putExtra("hosp_rating", hosp.rating);
            intent.putExtra("hosp_review_count", hosp.review_count);
            intent.putExtra("hosp_emergency", hosp.emergency);
            
            StringBuilder depts = new StringBuilder();
            if (hosp.specialists != null) {
                for(int i=0; i<hosp.specialists.size(); i++){
                    depts.append(hosp.specialists.get(i));
                    if(i < hosp.specialists.size() - 1) depts.append(", ");
                }
            }
            intent.putExtra("hosp_departments", depts.toString());
            v.getContext().startActivity(intent);
        });

        if (holder.btnDirections != null) {
            holder.btnDirections.setOnClickListener(v -> {
                if (hosp.lat != 0.0 && hosp.lng != 0.0) {
                    android.net.Uri gmmIntentUri = android.net.Uri.parse("google.navigation:q=" + hosp.lat + "," + hosp.lng);
                    android.content.Intent mapIntent = new android.content.Intent(android.content.Intent.ACTION_VIEW, gmmIntentUri);
                    mapIntent.setPackage("com.google.android.apps.maps");
                    if (mapIntent.resolveActivity(v.getContext().getPackageManager()) != null) {
                        v.getContext().startActivity(mapIntent);
                    } else {
                        android.net.Uri fallbackUri = android.net.Uri.parse("geo:" + hosp.lat + "," + hosp.lng + "?q=" + hosp.lat + "," + hosp.lng + "(" + android.net.Uri.encode(hosp.name) + ")");
                        android.content.Intent fallbackIntent = new android.content.Intent(android.content.Intent.ACTION_VIEW, fallbackUri);
                        if (fallbackIntent.resolveActivity(v.getContext().getPackageManager()) != null) {
                            v.getContext().startActivity(fallbackIntent);
                        } else {
                            android.widget.Toast.makeText(v.getContext(), "No Maps application is available on this device.", android.widget.Toast.LENGTH_LONG).show();
                        }
                    }
                } else {
                    android.widget.Toast.makeText(v.getContext(), "Location coordinates not available for this hospital.", android.widget.Toast.LENGTH_SHORT).show();
                }
            });
        }
    }

    @Override
    public int getItemCount() {
        return hospitals != null ? hospitals.size() : 0;
    }

    static class HospitalViewHolder extends RecyclerView.ViewHolder {
        TextView tvHospName, tvHospAddress, tvHospRating, tvEmergencyBadge;
        TextView tvDept1, tvDept2, tvDept3, tvDeptMore;
        TextView btnDirections;

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
            btnDirections = itemView.findViewById(R.id.btnDirections);
        }
    }
}

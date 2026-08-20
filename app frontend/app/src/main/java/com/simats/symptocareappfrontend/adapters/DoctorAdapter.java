package com.simats.symptocareappfrontend.adapters;

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

    private List<Doctor> fullDoctors = new ArrayList<>();
    private List<Doctor> doctors = new ArrayList<>();

    public void setDoctors(List<Doctor> doctors) {
        this.fullDoctors = new ArrayList<>(doctors);
        this.doctors = doctors;
        notifyDataSetChanged();
    }
    
    public void addDoctors(List<Doctor> newDoctors) {
        if (newDoctors != null && !newDoctors.isEmpty()) {
            int startPosition = this.doctors.size();
            this.fullDoctors.addAll(newDoctors);
            this.doctors.addAll(newDoctors);
            notifyItemRangeInserted(startPosition, newDoctors.size());
        }
    }
    
    public void filter(String query) {
        if (query == null || query.trim().isEmpty()) {
            this.doctors = new ArrayList<>(fullDoctors);
        } else {
            String lowerCaseQuery = query.toLowerCase().trim();
            List<Doctor> filtered = new ArrayList<>();
            for (Doctor doc : fullDoctors) {
                if (doc.name != null && doc.name.toLowerCase().contains(lowerCaseQuery)) {
                    filtered.add(doc);
                } else if (doc.specialist != null && doc.specialist.toLowerCase().contains(lowerCaseQuery)) {
                    filtered.add(doc);
                }
            }
            this.doctors = filtered;
        }
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
        if (doc.distance != null) {
            holder.tvRating.setText("⭐ " + doc.rating + " (" + doc.review_count + ")  📍 " + doc.distance);
        } else {
            holder.tvRating.setText("⭐ " + doc.rating + " (" + doc.review_count + ")");
        }
        
        holder.tvExperience.setText(doc.experience_years + " years");
        holder.tvFee.setText("Rs." + doc.consultation_fee);
        
        // Handle avatar initials
        String initialsStr = "";
        if(doc.name != null && doc.name.length() > 0) {
            String[] parts = doc.name.replace("Dr. ", "").split(" ");
            StringBuilder sb = new StringBuilder();
            for(String p : parts) {
                if(p.length() > 0) sb.append(p.charAt(0));
            }
            initialsStr = sb.toString().toUpperCase();
            holder.ivAvatar.setText(initialsStr);
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
        
        String finalInitials = initialsStr;
        android.view.View.OnClickListener onClick = v -> {
            android.content.Context context = holder.itemView.getContext();
            android.content.Intent intent = new android.content.Intent(context, com.simats.symptocareappfrontend.DoctorProfileActivity.class);
            intent.putExtra("doc_name", doc.name);
            intent.putExtra("doc_speciality", doc.specialist);
            intent.putExtra("doc_exp", doc.experience_years + " years");
            intent.putExtra("doc_fee", "Rs." + doc.consultation_fee);
            intent.putExtra("doc_initials", finalInitials);
            if (doc.distance != null) {
                intent.putExtra("doc_distance", doc.distance);
            }
            intent.putExtra("doc_lat", doc.lat);
            intent.putExtra("doc_lng", doc.lng);
            context.startActivity(intent);
        };
        holder.itemView.setOnClickListener(onClick);
        if (holder.btnBook != null) {
            holder.btnBook.setOnClickListener(onClick);
        }
        
        if (holder.btnNavigate != null) {
            holder.btnNavigate.setOnClickListener(v -> {
                android.net.Uri gmmIntentUri = android.net.Uri.parse("google.navigation:q=" + doc.lat + "," + doc.lng);
                android.content.Intent mapIntent = new android.content.Intent(android.content.Intent.ACTION_VIEW, gmmIntentUri);
                mapIntent.setPackage("com.google.android.apps.maps");
                try {
                    holder.itemView.getContext().startActivity(mapIntent);
                } catch (android.content.ActivityNotFoundException e) {
                    android.widget.Toast.makeText(holder.itemView.getContext(), "Google Maps is not installed", android.widget.Toast.LENGTH_SHORT).show();
                }
            });
        }
    }

    @Override
    public int getItemCount() {
        return doctors != null ? doctors.size() : 0;
    }

    static class DoctorViewHolder extends RecyclerView.ViewHolder {
        TextView tvDrName, tvDrSpec, tvRating, tvExperience, tvFee, ivAvatar, tvAvailableBadge, tvAvailableToday;
        TextView tvTime1, tvTime2, tvTime3, btnBook;
        android.widget.ImageView btnNavigate, btnCall;

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
            btnBook = itemView.findViewById(R.id.btnBook);
            btnNavigate = itemView.findViewById(R.id.btnNavigate);
            btnCall = itemView.findViewById(R.id.btnCall);
        }
    }
}

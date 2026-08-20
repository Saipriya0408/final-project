package com.simats.symptocareappfrontend.adapters;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import com.simats.symptocareappfrontend.R;
import java.util.List;

public class AppointmentAdapter extends RecyclerView.Adapter<AppointmentAdapter.ViewHolder> {
    
    public static class Appointment {
        public String docName;
        public String speciality;
        public String date;
        public Appointment(String docName, String speciality, String date) {
            this.docName = docName;
            this.speciality = speciality;
            this.date = date;
        }
    }

    private List<Appointment> appointments;

    public AppointmentAdapter(List<Appointment> appointments) {
        this.appointments = appointments;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_appointment, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        Appointment appt = appointments.get(position);
        holder.tvDocName.setText(appt.docName);
        holder.tvSpeciality.setText(appt.speciality);
        holder.tvDate.setText(appt.date);
    }

    @Override
    public int getItemCount() {
        return appointments != null ? appointments.size() : 0;
    }

    static class ViewHolder extends RecyclerView.ViewHolder {
        TextView tvDocName, tvSpeciality, tvDate;
        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            tvDocName = itemView.findViewById(R.id.tvApptDocName);
            tvSpeciality = itemView.findViewById(R.id.tvApptSpeciality);
            tvDate = itemView.findViewById(R.id.tvApptDate);
        }
    }
}

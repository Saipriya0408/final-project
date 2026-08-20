package com.simats.symptocareappfrontend.adapters;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import com.simats.symptocareappfrontend.R;
import java.util.List;

public class HealthHistoryAdapter extends RecyclerView.Adapter<HealthHistoryAdapter.ViewHolder> {
    
    public static class HealthRecord {
        public String symptoms;
        public String prediction;
        public String date;
        public HealthRecord(String symptoms, String prediction, String date) {
            this.symptoms = symptoms;
            this.prediction = prediction;
            this.date = date;
        }
    }

    private List<HealthRecord> records;

    public HealthHistoryAdapter(List<HealthRecord> records) {
        this.records = records;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_health_history, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        HealthRecord record = records.get(position);
        holder.tvDate.setText(record.date);
        holder.tvPrediction.setText(record.prediction);
        holder.tvSymptoms.setText("Symptoms: " + record.symptoms);
    }

    @Override
    public int getItemCount() {
        return records != null ? records.size() : 0;
    }

    static class ViewHolder extends RecyclerView.ViewHolder {
        TextView tvDate, tvPrediction, tvSymptoms;
        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            tvDate = itemView.findViewById(R.id.tvHistDate);
            tvPrediction = itemView.findViewById(R.id.tvHistPrediction);
            tvSymptoms = itemView.findViewById(R.id.tvHistSymptoms);
        }
    }
}

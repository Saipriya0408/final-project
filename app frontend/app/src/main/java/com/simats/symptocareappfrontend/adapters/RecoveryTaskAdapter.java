package com.simats.symptocareappfrontend.adapters;

import android.content.ContentValues;
import android.database.sqlite.SQLiteDatabase;
import android.graphics.Paint;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.simats.symptocareappfrontend.DatabaseHelper;
import com.simats.symptocareappfrontend.R;
import com.simats.symptocareappfrontend.models.RecoveryTask;

import java.util.List;

public class RecoveryTaskAdapter extends RecyclerView.Adapter<RecoveryTaskAdapter.TaskViewHolder> {

    private List<RecoveryTask> tasks;
    private OnTaskStatusChangedListener listener;
    private DatabaseHelper dbHelper;

    public interface OnTaskStatusChangedListener {
        void onStatusChanged();
    }

    public RecoveryTaskAdapter(List<RecoveryTask> tasks, DatabaseHelper dbHelper, OnTaskStatusChangedListener listener) {
        this.tasks = tasks;
        this.dbHelper = dbHelper;
        this.listener = listener;
    }

    public void updateTasks(List<RecoveryTask> newTasks) {
        this.tasks = newTasks;
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public TaskViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_recovery_task, parent, false);
        return new TaskViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull TaskViewHolder holder, int position) {
        RecoveryTask task = tasks.get(position);

        holder.tvTaskName.setText(task.taskName);
        holder.tvReminderTime.setText(task.reminderTimes);
        holder.tvTaskType.setText(task.taskType);

        // Badge styling based on type
        switch (task.taskType) {
            case "Tablet / Med":
                holder.tvTaskType.setBackgroundResource(R.drawable.bg_badge_purple);
                break;
            case "Topical / Apply":
                holder.tvTaskType.setBackgroundResource(R.drawable.bg_badge_teal);
                break;
            case "Exercise / Cardio":
                holder.tvTaskType.setBackgroundResource(R.drawable.bg_badge_orange);
                break;
            case "Check / Monitor":
                holder.tvTaskType.setBackgroundResource(R.drawable.bg_badge_gray);
                break;
            default:
                holder.tvTaskType.setBackgroundResource(R.drawable.bg_badge_gray);
                break;
        }

        updateTaskAppearance(holder, task);

        holder.itemView.setOnClickListener(v -> {
            task.isCompleted = !task.isCompleted;
            updateTaskAppearance(holder, task);
            
            // Save to DB
            SQLiteDatabase db = dbHelper.getWritableDatabase();
            ContentValues cv = new ContentValues();
            cv.put(DatabaseHelper.COL_RT_IS_COMPLETED, task.isCompleted ? 1 : 0);
            db.update(DatabaseHelper.TABLE_RECOVERY_TASKS, cv, DatabaseHelper.COL_RT_ID + "=?", new String[]{String.valueOf(task.id)});
            db.close();

            if (listener != null) {
                listener.onStatusChanged();
            }
        });
    }

    private void updateTaskAppearance(TaskViewHolder holder, RecoveryTask task) {
        if (task.isCompleted) {
            holder.ivCheckbox.setImageResource(R.drawable.ic_check_circle);
            holder.tvTaskName.setPaintFlags(holder.tvTaskName.getPaintFlags() | Paint.STRIKE_THRU_TEXT_FLAG);
            holder.tvTaskName.setAlpha(0.6f);
        } else {
            holder.ivCheckbox.setImageResource(R.drawable.ic_circle_outline);
            holder.tvTaskName.setPaintFlags(holder.tvTaskName.getPaintFlags() & (~Paint.STRIKE_THRU_TEXT_FLAG));
            holder.tvTaskName.setAlpha(1.0f);
        }
    }

    @Override
    public int getItemCount() {
        return tasks != null ? tasks.size() : 0;
    }

    static class TaskViewHolder extends RecyclerView.ViewHolder {
        ImageView ivCheckbox;
        TextView tvTaskName;
        TextView tvReminderTime;
        TextView tvTaskType;

        public TaskViewHolder(@NonNull View itemView) {
            super(itemView);
            ivCheckbox = itemView.findViewById(R.id.ivCheckbox);
            tvTaskName = itemView.findViewById(R.id.tvTaskName);
            tvReminderTime = itemView.findViewById(R.id.tvReminderTime);
            tvTaskType = itemView.findViewById(R.id.tvTaskType);
        }
    }
}

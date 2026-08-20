package com.simats.symptocareappfrontend;

import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Build;
import androidx.core.app.NotificationCompat;

public class TaskAlarmReceiver extends BroadcastReceiver {
    private static final String CHANNEL_ID = "SymptoCare_Reminders";

    @Override
    public void onReceive(Context context, Intent intent) {
        String taskName = intent.getStringExtra("task_name");
        if (taskName == null) taskName = "Recovery Task";

        NotificationManager notificationManager = (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            NotificationChannel channel = new NotificationChannel(
                    CHANNEL_ID,
                    "SymptoCare Reminders",
                    NotificationManager.IMPORTANCE_HIGH
            );
            channel.setDescription("Reminders for your recovery tasks");
            channel.enableVibration(true);
            channel.setLockscreenVisibility(android.app.Notification.VISIBILITY_PUBLIC);
            notificationManager.createNotificationChannel(channel);
        }

        Intent appIntent = new Intent(context, MainActivity.class);
        PendingIntent pendingIntent = PendingIntent.getActivity(context, 0, appIntent, PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE);

        NotificationCompat.Builder builder = new NotificationCompat.Builder(context, CHANNEL_ID)
                .setSmallIcon(R.drawable.ic_task)
                .setContentTitle("SymptoCare Reminder")
                .setContentText("It's time to take: " + taskName)
                .setPriority(NotificationCompat.PRIORITY_HIGH)
                .setAutoCancel(true)
                .setContentIntent(pendingIntent);

        notificationManager.notify((int) System.currentTimeMillis(), builder.build());

        // Handle task rescheduling or deletion based on the number of reminder times
        int taskId = intent.getIntExtra("task_id", -1);
        String reminderTime = intent.getStringExtra("reminder_time");
        int requestCode = intent.getIntExtra("request_code", -1);

        if (taskId != -1 && reminderTime != null && requestCode != -1) {
            DatabaseHelper dbHelper = new DatabaseHelper(context);
            android.database.sqlite.SQLiteDatabase db = dbHelper.getWritableDatabase();

            String timesCsv = "";
            android.database.Cursor c = db.rawQuery("SELECT " + DatabaseHelper.COL_RT_REMINDER_TIMES +
                    " FROM " + DatabaseHelper.TABLE_RECOVERY_TASKS + " WHERE " + DatabaseHelper.COL_RT_ID + "=?",
                    new String[]{String.valueOf(taskId)});
            if (c != null) {
                if (c.moveToFirst()) {
                    timesCsv = c.getString(0);
                }
                c.close();
            }

            boolean isSingleReminder = true;
            if (timesCsv != null && timesCsv.contains(", ")) {
                isSingleReminder = false;
            }

            if (isSingleReminder) {
                // Delete task from local SQLite
                db.delete(DatabaseHelper.TABLE_RECOVERY_TASKS, DatabaseHelper.COL_RT_ID + "=?", new String[]{String.valueOf(taskId)});
                db.close();

                // Cancel the alarm
                android.app.AlarmManager alarmManager = (android.app.AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
                if (alarmManager != null) {
                    Intent alarmIntent = new Intent(context, TaskAlarmReceiver.class);
                    PendingIntent pendingIntentDelete = PendingIntent.getBroadcast(
                            context,
                            requestCode,
                            alarmIntent,
                            PendingIntent.FLAG_NO_CREATE | PendingIntent.FLAG_IMMUTABLE
                    );
                    if (pendingIntentDelete != null) {
                        alarmManager.cancel(pendingIntentDelete);
                        pendingIntentDelete.cancel();
                    }
                }

                // Broadcast intent to refresh the RecoveryTasks page UI immediately
                Intent refreshIntent = new Intent("com.simats.symptocare.REFRESH_TASKS");
                context.sendBroadcast(refreshIntent);
            } else {
                db.close();
                // Reschedule daily exact alarm normally for tomorrow
                android.app.AlarmManager alarmManager = (android.app.AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
                if (alarmManager != null) {
                    try {
                        java.text.SimpleDateFormat sdf = new java.text.SimpleDateFormat("h:mm a", java.util.Locale.US);
                        java.util.Date d = sdf.parse(reminderTime);
                        java.util.Calendar alarmCal = java.util.Calendar.getInstance();
                        java.util.Calendar parsedCal = java.util.Calendar.getInstance();
                        parsedCal.setTime(d);

                        alarmCal.set(java.util.Calendar.HOUR_OF_DAY, parsedCal.get(java.util.Calendar.HOUR_OF_DAY));
                        alarmCal.set(java.util.Calendar.MINUTE, parsedCal.get(java.util.Calendar.MINUTE));
                        alarmCal.set(java.util.Calendar.SECOND, 0);

                        alarmCal.add(java.util.Calendar.DATE, 1); // schedule for tomorrow

                        Intent alarmIntent = new Intent(context, TaskAlarmReceiver.class);
                        alarmIntent.putExtra("task_id", taskId);
                        alarmIntent.putExtra("task_name", taskName);
                        alarmIntent.putExtra("reminder_time", reminderTime);
                        alarmIntent.putExtra("request_code", requestCode);

                        PendingIntent resIntent = PendingIntent.getBroadcast(
                                context,
                                requestCode,
                                alarmIntent,
                                PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE
                        );

                        try {
                            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                                alarmManager.setExactAndAllowWhileIdle(android.app.AlarmManager.RTC_WAKEUP, alarmCal.getTimeInMillis(), resIntent);
                            } else if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
                                alarmManager.setExact(android.app.AlarmManager.RTC_WAKEUP, alarmCal.getTimeInMillis(), resIntent);
                            } else {
                                alarmManager.set(android.app.AlarmManager.RTC_WAKEUP, alarmCal.getTimeInMillis(), resIntent);
                            }
                        } catch (SecurityException se) {
                            alarmManager.set(android.app.AlarmManager.RTC_WAKEUP, alarmCal.getTimeInMillis(), resIntent);
                        }
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
}

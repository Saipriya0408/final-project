package com.simats.symptocareappfrontend;

import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.text.TextUtils;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;

public class BootReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        if (Intent.ACTION_BOOT_COMPLETED.equals(intent.getAction())) {
            SharedPreferences prefs = context.getSharedPreferences("SymptoCarePrefs", Context.MODE_PRIVATE);
            long userId = prefs.getLong("active_user_id", -1);
            if (userId == -1) return;

            String today = new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault()).format(new Date());
            DatabaseHelper dbHelper = new DatabaseHelper(context);
            SQLiteDatabase db = dbHelper.getReadableDatabase();
            
            Cursor c = db.rawQuery("SELECT * FROM " + DatabaseHelper.TABLE_RECOVERY_TASKS + 
                    " WHERE " + DatabaseHelper.COL_RT_USER_ID + "=? AND " + DatabaseHelper.COL_RT_CREATED_DATE + "=?", 
                    new String[]{String.valueOf(userId), today});

            if (c != null && c.moveToFirst()) {
                AlarmManager alarmManager = (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
                if (alarmManager != null) {
                    SimpleDateFormat sdf = new SimpleDateFormat("h:mm a", Locale.US);
                    do {
                        int taskId = c.getInt(c.getColumnIndexOrThrow(DatabaseHelper.COL_RT_ID));
                        String taskName = c.getString(c.getColumnIndexOrThrow(DatabaseHelper.COL_RT_TASK_NAME));
                        String timesCsv = c.getString(c.getColumnIndexOrThrow(DatabaseHelper.COL_RT_REMINDER_TIMES));
                        
                        if (!TextUtils.isEmpty(timesCsv)) {
                            String[] times = timesCsv.split(", ");
                            for (int i = 0; i < times.length; i++) {
                                String timeStr = times[i];
                                try {
                                    Date d = sdf.parse(timeStr);
                                    Calendar alarmCal = Calendar.getInstance();
                                    Calendar parsedCal = Calendar.getInstance();
                                    parsedCal.setTime(d);
                                    
                                    alarmCal.set(Calendar.HOUR_OF_DAY, parsedCal.get(Calendar.HOUR_OF_DAY));
                                    alarmCal.set(Calendar.MINUTE, parsedCal.get(Calendar.MINUTE));
                                    alarmCal.set(Calendar.SECOND, 0);

                                    if (alarmCal.before(Calendar.getInstance())) {
                                        alarmCal.add(Calendar.DATE, 1);
                                    }

                                    Intent alarmIntent = new Intent(context, TaskAlarmReceiver.class);
                                    alarmIntent.putExtra("task_id", taskId);
                                    alarmIntent.putExtra("task_name", taskName);
                                    alarmIntent.putExtra("reminder_time", timeStr);
                                    
                                    int requestCode = taskId * 100 + i;
                                    alarmIntent.putExtra("request_code", requestCode);

                                    PendingIntent pendingIntent = PendingIntent.getBroadcast(
                                            context, 
                                            requestCode, 
                                            alarmIntent, 
                                            PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE
                                    );

                                    try {
                                        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.M) {
                                            alarmManager.setExactAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, alarmCal.getTimeInMillis(), pendingIntent);
                                        } else if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.KITKAT) {
                                            alarmManager.setExact(AlarmManager.RTC_WAKEUP, alarmCal.getTimeInMillis(), pendingIntent);
                                        } else {
                                            alarmManager.set(AlarmManager.RTC_WAKEUP, alarmCal.getTimeInMillis(), pendingIntent);
                                        }
                                    } catch (SecurityException se) {
                                        alarmManager.set(AlarmManager.RTC_WAKEUP, alarmCal.getTimeInMillis(), pendingIntent);
                                    }
                                } catch (Exception e) {
                                    e.printStackTrace();
                                }
                            }
                        }
                    } while (c.moveToNext());
                }
                c.close();
            }
            db.close();
        }
    }
}

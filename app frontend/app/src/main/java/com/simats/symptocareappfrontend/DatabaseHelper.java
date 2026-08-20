package com.simats.symptocareappfrontend;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import java.util.ArrayList;
import java.util.List;

public class DatabaseHelper extends SQLiteOpenHelper {

    private static final String DATABASE_NAME = "symptocare.db";
    private static final int DATABASE_VERSION = 3;

    // Users Table
    public static final String TABLE_USERS = "users";
    public static final String COL_USER_ID = "id";
    public static final String COL_USER_NAME = "name";
    public static final String COL_USER_EMAIL = "email";
    public static final String COL_USER_PHONE = "phone";
    public static final String COL_USER_PASSWORD = "password";

    // Appointments Table
    public static final String TABLE_APPOINTMENTS = "appointments";
    public static final String COL_APP_ID = "id";
    public static final String COL_APP_USER_ID = "user_id";
    public static final String COL_APP_DOC_NAME = "doctor_name";
    public static final String COL_APP_SPECIALITY = "speciality";
    public static final String COL_APP_DATETIME = "date_time";

    // Health History Table
    public static final String TABLE_HEALTH_HISTORY = "health_history";
    public static final String COL_HIST_ID = "id";
    public static final String COL_HIST_USER_ID = "user_id";
    public static final String COL_HIST_SYMPTOMS = "symptoms";
    public static final String COL_HIST_PREDICTION = "prediction";
    public static final String COL_HIST_TIMESTAMP = "timestamp";

    // Saved Doctors Table
    public static final String TABLE_SAVED_DOCTORS = "saved_doctors";
    public static final String COL_SD_ID = "id";
    public static final String COL_SD_USER_ID = "user_id";
    public static final String COL_SD_NAME = "name";
    public static final String COL_SD_SPECIALITY = "speciality";
    public static final String COL_SD_EXP = "experience";
    public static final String COL_SD_FEE = "fee";
    public static final String COL_SD_INITIALS = "initials";

    // Saved Hospitals Table
    public static final String TABLE_SAVED_HOSPITALS = "saved_hospitals";
    public static final String COL_SH_ID = "id";
    public static final String COL_SH_USER_ID = "user_id";
    public static final String COL_SH_NAME = "name";
    public static final String COL_SH_LOCATION = "location";
    public static final String COL_SH_DEPARTMENTS = "departments";
    public static final String COL_SH_RATING = "rating";
    public static final String COL_SH_EMERGENCY = "emergency";

    // Recovery Tasks Table
    public static final String TABLE_RECOVERY_TASKS = "recovery_tasks";
    public static final String COL_RT_ID = "id";
    public static final String COL_RT_USER_ID = "user_id";
    public static final String COL_RT_TASK_NAME = "task_name";
    public static final String COL_RT_TASK_TYPE = "task_type";
    public static final String COL_RT_REMINDER_TIMES = "reminder_times";
    public static final String COL_RT_DURATION_DAYS = "duration_days";
    public static final String COL_RT_CREATED_DATE = "created_date";
    public static final String COL_RT_IS_COMPLETED = "is_completed";

    public DatabaseHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        String createUsersTable = "CREATE TABLE " + TABLE_USERS + " (" +
                COL_USER_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                COL_USER_NAME + " TEXT, " +
                COL_USER_EMAIL + " TEXT, " +
                COL_USER_PHONE + " TEXT, " +
                COL_USER_PASSWORD + " TEXT)";

        String createAppointmentsTable = "CREATE TABLE " + TABLE_APPOINTMENTS + " (" +
                COL_APP_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                COL_APP_USER_ID + " INTEGER, " +
                COL_APP_DOC_NAME + " TEXT, " +
                COL_APP_SPECIALITY + " TEXT, " +
                COL_APP_DATETIME + " TEXT, " +
                "FOREIGN KEY(" + COL_APP_USER_ID + ") REFERENCES " + TABLE_USERS + "(" + COL_USER_ID + "))";

        String createHealthHistoryTable = "CREATE TABLE " + TABLE_HEALTH_HISTORY + " (" +
                COL_HIST_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                COL_HIST_USER_ID + " INTEGER, " +
                COL_HIST_SYMPTOMS + " TEXT, " +
                COL_HIST_PREDICTION + " TEXT, " +
                COL_HIST_TIMESTAMP + " TEXT, " +
                "FOREIGN KEY(" + COL_HIST_USER_ID + ") REFERENCES " + TABLE_USERS + "(" + COL_USER_ID + "))";

        String createSavedDoctorsTable = "CREATE TABLE " + TABLE_SAVED_DOCTORS + " (" +
                COL_SD_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                COL_SD_USER_ID + " INTEGER, " +
                COL_SD_NAME + " TEXT, " +
                COL_SD_SPECIALITY + " TEXT, " +
                COL_SD_EXP + " TEXT, " +
                COL_SD_FEE + " TEXT, " +
                COL_SD_INITIALS + " TEXT, " +
                "FOREIGN KEY(" + COL_SD_USER_ID + ") REFERENCES " + TABLE_USERS + "(" + COL_USER_ID + "))";

        String createSavedHospitalsTable = "CREATE TABLE " + TABLE_SAVED_HOSPITALS + " (" +
                COL_SH_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                COL_SH_USER_ID + " INTEGER, " +
                COL_SH_NAME + " TEXT, " +
                COL_SH_LOCATION + " TEXT, " +
                COL_SH_DEPARTMENTS + " TEXT, " +
                COL_SH_RATING + " TEXT, " +
                COL_SH_EMERGENCY + " INTEGER, " +
                "FOREIGN KEY(" + COL_SH_USER_ID + ") REFERENCES " + TABLE_USERS + "(" + COL_USER_ID + "))";

        String createRecoveryTasksTable = "CREATE TABLE " + TABLE_RECOVERY_TASKS + " (" +
                COL_RT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                COL_RT_USER_ID + " INTEGER, " +
                COL_RT_TASK_NAME + " TEXT, " +
                COL_RT_TASK_TYPE + " TEXT, " +
                COL_RT_REMINDER_TIMES + " TEXT, " +
                COL_RT_DURATION_DAYS + " INTEGER, " +
                COL_RT_CREATED_DATE + " TEXT, " +
                COL_RT_IS_COMPLETED + " INTEGER DEFAULT 0, " +
                "FOREIGN KEY(" + COL_RT_USER_ID + ") REFERENCES " + TABLE_USERS + "(" + COL_USER_ID + "))";

        db.execSQL(createUsersTable);
        db.execSQL(createAppointmentsTable);
        db.execSQL(createHealthHistoryTable);
        db.execSQL(createSavedDoctorsTable);
        db.execSQL(createSavedHospitalsTable);
        db.execSQL(createRecoveryTasksTable);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_RECOVERY_TASKS);
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_SAVED_HOSPITALS);
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_SAVED_DOCTORS);
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_HEALTH_HISTORY);
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_APPOINTMENTS);
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_USERS);
        onCreate(db);
    }
}

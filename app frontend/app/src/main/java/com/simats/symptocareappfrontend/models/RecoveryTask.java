package com.simats.symptocareappfrontend.models;

public class RecoveryTask {
    public int id;
    public long userId;
    public String taskName;
    public String taskType;
    public String reminderTimes;
    public int durationDays;
    public String createdDate;
    public boolean isCompleted;

    public RecoveryTask() {}

    public RecoveryTask(int id, long userId, String taskName, String taskType, String reminderTimes, int durationDays, String createdDate, boolean isCompleted) {
        this.id = id;
        this.userId = userId;
        this.taskName = taskName;
        this.taskType = taskType;
        this.reminderTimes = reminderTimes;
        this.durationDays = durationDays;
        this.createdDate = createdDate;
        this.isCompleted = isCompleted;
    }
}

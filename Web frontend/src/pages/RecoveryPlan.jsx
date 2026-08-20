import React, { useState, useEffect } from 'react';
import { ChevronLeft, Plus, Check, Clock, Calendar as CalendarIcon, Activity, Droplets } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export default function RecoveryPlan() {
  const navigate = useNavigate();
  const [tasks, setTasks] = useState([]);
  const [showModal, setShowModal] = useState(false);
  
  // Modal Form State
  const [taskType, setTaskType] = useState('');
  const [taskName, setTaskName] = useState('');
  const [selectedTimes, setSelectedTimes] = useState([]);
  const [customTime, setCustomTime] = useState('');
  const [repeatDays, setRepeatDays] = useState(7);
  
  const PRESET_TIMES = ['08:00 AM', '02:00 PM', '08:00 PM'];
  const TASK_TYPES = [
    { id: 'tablet', label: 'Tablet / Med', icon: <Droplets size={24} /> },
    { id: 'topical', label: 'Topical / Apply', icon: <Activity size={24} /> },
    { id: 'exercise', label: 'Exercise / Cardio', icon: <Activity size={24} /> },
    { id: 'monitor', label: 'Check / Monitor', icon: <CalendarIcon size={24} /> }
  ];

  const todayStr = new Date().toDateString();
  const [notificationStatus, setNotificationStatus] = useState('granted');

  useEffect(() => {
    const saved = JSON.parse(localStorage.getItem('recovery_tasks') || '[]');
    setTasks(saved);

    if (!('Notification' in window)) {
      setNotificationStatus('unsupported');
    } else {
      setNotificationStatus(Notification.permission);
      if (Notification.permission === 'default') {
        Notification.requestPermission().then(permission => {
          setNotificationStatus(permission);
        });
      }
    }
  }, []);

  const saveTasks = (newTasks) => {
    setTasks(newTasks);
    localStorage.setItem('recovery_tasks', JSON.stringify(newTasks));
  };

  const handleToggleTask = (task) => {
    const isCompleted = task.completed_dates?.includes(todayStr);
    let newDates = task.completed_dates || [];
    if (isCompleted) {
      newDates = newDates.filter(d => d !== todayStr);
    } else {
      newDates = [...newDates, todayStr];
    }
    
    const newTasks = tasks.map(t => t.id === task.id ? { ...t, completed_dates: newDates } : t);
    saveTasks(newTasks);
  };

  const handleSaveNewTask = () => {
    if (!taskType || !taskName || selectedTimes.length === 0 || !repeatDays) {
      alert("Please fill all fields");
      return;
    }
    
    const newTask = {
      id: Date.now(),
      type: taskType,
      name: taskName,
      reminderTimes: selectedTimes,
      repeatDays: parseInt(repeatDays, 10),
      created_at: new Date().toISOString(),
      completed_dates: []
    };
    
    saveTasks([...tasks, newTask]);
    setShowModal(false);
    
    // Reset form
    setTaskType('');
    setTaskName('');
    setSelectedTimes([]);
    setCustomTime('');
    setRepeatDays(7);
  };

  const toggleTime = (time) => {
    if (selectedTimes.includes(time)) {
      setSelectedTimes(selectedTimes.filter(t => t !== time));
    } else {
      setSelectedTimes([...selectedTimes, time]);
    }
  };

  const handleAddCustomTime = () => {
    if (customTime && !selectedTimes.includes(customTime)) {
      // Format 24hr customTime to 12hr AM/PM for consistency
      const [hours, minutes] = customTime.split(':');
      const h = parseInt(hours, 10);
      const ampm = h >= 12 ? 'PM' : 'AM';
      const formattedH = h % 12 || 12;
      const formattedTime = `${formattedH.toString().padStart(2, '0')}:${minutes} ${ampm}`;
      
      if (!selectedTimes.includes(formattedTime)) {
        setSelectedTimes([...selectedTimes, formattedTime]);
      }
    }
  };

  // Calculations for progress bar
  const todayTasks = tasks.filter(t => {
    // Basic filter: checking if today is within created_at + repeatDays
    const createdDate = new Date(t.created_at);
    const diffDays = Math.floor((new Date() - createdDate) / (1000 * 60 * 60 * 24));
    return diffDays <= t.repeatDays;
  });
  
  const completedToday = todayTasks.filter(t => t.completed_dates?.includes(todayStr)).length;
  const progressPercent = todayTasks.length === 0 ? 0 : Math.round((completedToday / todayTasks.length) * 100);

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <button onClick={() => navigate(-1)} style={styles.backBtn}>
          <ChevronLeft size={24} color="#0f172a" />
        </button>
        <h2 style={styles.title}>Recovery Plan</h2>
        <div style={{width: 24}}></div>
      </div>

      {notificationStatus === 'unsupported' && (
        <div style={{
          backgroundColor: '#fee2e2',
          border: '1px solid #fca5a5',
          borderRadius: '12px',
          padding: '16px',
          marginBottom: '20px',
          color: '#b91c1c',
          fontSize: '14px',
          display: 'flex',
          alignItems: 'center',
          gap: '8px'
        }}>
          <Info size={18} />
          <span>Browser notifications are not supported by your browser. Reminders will not trigger.</span>
        </div>
      )}

      {notificationStatus === 'denied' && (
        <div style={{
          backgroundColor: '#fef3c7',
          border: '1px solid #fcd34d',
          borderRadius: '12px',
          padding: '16px',
          marginBottom: '20px',
          color: '#d97706',
          fontSize: '14px',
          display: 'flex',
          alignItems: 'center',
          gap: '8px'
        }}>
          <Info size={18} />
          <span>Notification permission is denied. Enable notifications in your browser settings to receive medicine reminders.</span>
        </div>
      )}

      <div style={styles.progressCard}>
        <div style={styles.progressHeader}>
          <div>
            <h3 style={styles.progressTitle}>Daily Progress</h3>
            <p style={styles.progressSubtitle}>{completedToday} of {todayTasks.length} tasks done</p>
          </div>
          <div style={styles.progressPercent}>{progressPercent}%</div>
        </div>
        <div style={styles.progressBarBg}>
          <div style={{...styles.progressBarFill, width: `${progressPercent}%`}}></div>
        </div>
      </div>

      <div style={styles.taskList}>
        <h3 style={styles.sectionTitle}>Today's Tasks</h3>
        {todayTasks.length === 0 ? (
          <p style={styles.emptyState}>No tasks for today. Add a task from your doctor's instructions.</p>
        ) : (
          todayTasks.map(task => {
            const isCompleted = task.completed_dates?.includes(todayStr);
            return (
              <div key={task.id} style={styles.taskCard}>
                <div style={{ display: 'flex', alignItems: 'center', flex: 1 }} onClick={() => handleToggleTask(task)}>
                  <div style={{
                    ...styles.checkbox, 
                    backgroundColor: isCompleted ? '#38bdf8' : '#ffffff',
                    borderColor: isCompleted ? '#38bdf8' : '#cbd5e1'
                  }}>
                    {isCompleted && <Check size={14} color="#ffffff" />}
                  </div>
                  <div style={styles.taskInfo}>
                    <p style={{
                      ...styles.taskName,
                      textDecoration: isCompleted ? 'line-through' : 'none',
                      color: isCompleted ? '#94a3b8' : '#0f172a'
                    }}>
                      {task.name}
                    </p>
                    <p style={styles.taskMeta}>
                      <Clock size={12} style={{marginRight: 4}} /> 
                      {task.reminderTimes.join(', ')}
                    </p>
                  </div>
                </div>
                <button 
                  style={{
                    background: 'none',
                    border: 'none',
                    color: '#ef4444',
                    cursor: 'pointer',
                    padding: '8px',
                    fontSize: '14px',
                    fontWeight: '600'
                  }}
                  onClick={(e) => {
                    e.stopPropagation();
                    if (window.confirm("Are you sure you want to delete this task?")) {
                      const newTasks = tasks.filter(t => t.id !== task.id);
                      saveTasks(newTasks);
                    }
                  }}
                >
                  Delete
                </button>
              </div>
            );
          })
        )}
      </div>

      <button style={styles.addBtn} onClick={() => setShowModal(true)}>
        <Plus size={20} style={{marginRight: 8}} /> Add task from doctor's instructions
      </button>

      {showModal && (
        <div style={styles.modalOverlay}>
          <div style={styles.modalContent}>
            <div style={styles.modalHeader}>
              <h3 style={styles.modalTitle}>Add Recovery Task</h3>
              <button style={styles.closeBtn} onClick={() => setShowModal(false)}>&times;</button>
            </div>
            
            <div style={styles.formGroup}>
              <label style={styles.label}>Task Type</label>
              <div style={styles.typeGrid}>
                {TASK_TYPES.map(type => (
                  <div 
                    key={type.id} 
                    style={{
                      ...styles.typeCard,
                      borderColor: taskType === type.id ? '#38bdf8' : '#e2e8f0',
                      backgroundColor: taskType === type.id ? '#f0f9ff' : '#ffffff'
                    }}
                    onClick={() => setTaskType(type.id)}
                  >
                    {type.icon}
                    <span style={styles.typeLabel}>{type.label}</span>
                  </div>
                ))}
              </div>
            </div>

            <div style={styles.formGroup}>
              <label style={styles.label}>Task Name</label>
              <input 
                style={styles.input} 
                placeholder="e.g. Take Aspirin 50mg"
                value={taskName}
                onChange={e => setTaskName(e.target.value)}
              />
            </div>

            <div style={styles.formGroup}>
              <label style={styles.label}>Reminder Times</label>
              <div style={styles.chipsRow}>
                {PRESET_TIMES.map(time => (
                  <button 
                    key={time}
                    style={{
                      ...styles.chip,
                      backgroundColor: selectedTimes.includes(time) ? '#38bdf8' : '#f1f5f9',
                      color: selectedTimes.includes(time) ? '#ffffff' : '#475569'
                    }}
                    onClick={() => toggleTime(time)}
                  >
                    {time}
                  </button>
                ))}
              </div>
              <div style={{display: 'flex', gap: '8px', marginTop: '12px'}}>
                <input 
                  type="time" 
                  style={{...styles.input, flex: 1, marginBottom: 0}}
                  value={customTime}
                  onChange={e => setCustomTime(e.target.value)}
                />
                <button 
                  style={{...styles.btnSecondary, padding: '0 16px'}}
                  onClick={handleAddCustomTime}
                >
                  Add
                </button>
              </div>
              {selectedTimes.length > 0 && (
                <div style={{marginTop: 8, fontSize: 13, color: '#64748b'}}>
                  Selected: {selectedTimes.join(', ')}
                </div>
              )}
            </div>

            <div style={styles.formGroup}>
              <label style={styles.label}>Repeat Duration (Days)</label>
              <input 
                type="number" 
                style={styles.input} 
                value={repeatDays}
                onChange={e => setRepeatDays(e.target.value)}
                min="1"
              />
            </div>

            <button style={styles.btnPrimary} onClick={handleSaveNewTask}>
              Save Task
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

const styles = {
  container: {
    backgroundColor: '#ffffff',
    minHeight: '100%',
    padding: '24px 20px',
    paddingBottom: '100px',
  },
  header: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: '24px',
  },
  backBtn: {
    background: 'none',
    border: 'none',
    cursor: 'pointer',
    padding: '4px',
  },
  title: {
    fontSize: '18px',
    fontWeight: '700',
    color: '#0f172a',
  },
  progressCard: {
    backgroundColor: '#f8fafc',
    borderRadius: '16px',
    padding: '20px',
    marginBottom: '24px',
    border: '1px solid #e2e8f0',
  },
  progressHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: '16px',
  },
  progressTitle: {
    fontSize: '16px',
    fontWeight: '600',
    color: '#0f172a',
    marginBottom: '4px',
  },
  progressSubtitle: {
    fontSize: '13px',
    color: '#64748b',
  },
  progressPercent: {
    fontSize: '24px',
    fontWeight: '700',
    color: '#38bdf8',
  },
  progressBarBg: {
    height: '8px',
    backgroundColor: '#e2e8f0',
    borderRadius: '4px',
    overflow: 'hidden',
  },
  progressBarFill: {
    height: '100%',
    backgroundColor: '#38bdf8',
    transition: 'width 0.3s ease',
  },
  sectionTitle: {
    fontSize: '16px',
    fontWeight: '700',
    color: '#0f172a',
    marginBottom: '16px',
  },
  taskList: {
    display: 'flex',
    flexDirection: 'column',
    gap: '12px',
    marginBottom: '24px',
  },
  emptyState: {
    fontSize: '14px',
    color: '#94a3b8',
    textAlign: 'center',
    padding: '24px 0',
  },
  taskCard: {
    display: 'flex',
    alignItems: 'center',
    padding: '16px',
    backgroundColor: '#ffffff',
    borderRadius: '12px',
    border: '1px solid #e2e8f0',
    cursor: 'pointer',
    boxShadow: '0 2px 4px rgba(0,0,0,0.02)',
  },
  checkbox: {
    width: '24px',
    height: '24px',
    borderRadius: '12px',
    border: '2px solid',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: '16px',
    transition: 'all 0.2s',
  },
  taskInfo: {
    flex: 1,
  },
  taskName: {
    fontSize: '15px',
    fontWeight: '500',
    marginBottom: '4px',
    transition: 'all 0.2s',
  },
  taskMeta: {
    fontSize: '12px',
    color: '#64748b',
    display: 'flex',
    alignItems: 'center',
  },
  addBtn: {
    width: '100%',
    padding: '16px',
    borderRadius: '12px',
    border: '2px dashed #cbd5e1',
    backgroundColor: '#f8fafc',
    color: '#475569',
    fontSize: '14px',
    fontWeight: '600',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    cursor: 'pointer',
  },
  modalOverlay: {
    position: 'fixed',
    top: 0, left: 0, right: 0, bottom: 0,
    backgroundColor: 'rgba(15, 23, 42, 0.6)',
    zIndex: 200,
    display: 'flex',
    alignItems: 'flex-end',
    justifyContent: 'center',
  },
  modalContent: {
    backgroundColor: '#ffffff',
    width: '100%',
    maxHeight: '90vh',
    overflowY: 'auto',
    borderTopLeftRadius: '24px',
    borderTopRightRadius: '24px',
    padding: '24px',
    paddingBottom: '40px',
  },
  modalHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '24px',
  },
  modalTitle: {
    fontSize: '20px',
    fontWeight: '700',
    color: '#0f172a',
  },
  closeBtn: {
    background: 'none',
    border: 'none',
    fontSize: '28px',
    color: '#64748b',
    cursor: 'pointer',
  },
  formGroup: {
    marginBottom: '24px',
  },
  label: {
    display: 'block',
    fontSize: '14px',
    fontWeight: '600',
    color: '#475569',
    marginBottom: '12px',
  },
  typeGrid: {
    display: 'grid',
    gridTemplateColumns: '1fr 1fr',
    gap: '12px',
  },
  typeCard: {
    border: '1px solid',
    borderRadius: '12px',
    padding: '16px',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: '8px',
    cursor: 'pointer',
    color: '#0f172a',
  },
  typeLabel: {
    fontSize: '13px',
    fontWeight: '500',
    textAlign: 'center',
  },
  input: {
    width: '100%',
    padding: '14px 16px',
    borderRadius: '12px',
    border: '1px solid #cbd5e1',
    fontSize: '15px',
    backgroundColor: '#f8fafc',
    marginBottom: '12px',
  },
  chipsRow: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '8px',
  },
  chip: {
    padding: '8px 16px',
    borderRadius: '20px',
    border: 'none',
    fontSize: '13px',
    fontWeight: '500',
    cursor: 'pointer',
  },
  btnSecondary: {
    backgroundColor: '#e2e8f0',
    color: '#475569',
    border: 'none',
    borderRadius: '12px',
    fontWeight: '600',
    cursor: 'pointer',
  },
  btnPrimary: {
    width: '100%',
    padding: '16px',
    backgroundColor: '#38bdf8',
    color: '#ffffff',
    border: 'none',
    borderRadius: '12px',
    fontSize: '16px',
    fontWeight: '600',
    cursor: 'pointer',
    marginTop: '12px',
  }
};

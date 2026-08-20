import React, { useState, useEffect } from 'react';
import { Calendar, Heart, Bookmark, Activity, Droplets, LogOut, ChevronRight, ListChecks } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export default function Profile() {
  const navigate = useNavigate();
  const [appointments, setAppointments] = useState([]);
  const [aiScans, setAiScans] = useState([]);
  const [recentActivity, setRecentActivity] = useState([]);
  const [waterIntake, setWaterIntake] = useState(0);

  const [savedDoctorsCount, setSavedDoctorsCount] = useState(0);
  const [savedHospitalsCount, setSavedHospitalsCount] = useState(0);
  const [activeTasksCount, setActiveTasksCount] = useState(0);

  const [user, setUser] = useState(null);

  useEffect(() => {
    // Load data from localStorage
    const savedUser = JSON.parse(localStorage.getItem('user') || 'null');
    const savedAppointments = JSON.parse(localStorage.getItem('appointments') || '[]');
    const savedScans = JSON.parse(localStorage.getItem('ai_scans') || '[]');
    const savedActivity = JSON.parse(localStorage.getItem('recent_activity') || '[]');
    const sDoctors = JSON.parse(localStorage.getItem('saved_doctors') || '[]');
    const sHospitals = JSON.parse(localStorage.getItem('saved_hospitals') || '[]');
    const tasks = JSON.parse(localStorage.getItem('recovery_tasks') || '[]');
    
    // For water intake, check if it's a new day
    const lastWaterDate = localStorage.getItem('water_date');
    const today = new Date().toDateString();
    let currentWater = 0;
    
    if (lastWaterDate === today) {
      currentWater = parseInt(localStorage.getItem('water_intake') || '0', 10);
    } else {
      localStorage.setItem('water_date', today);
      localStorage.setItem('water_intake', '0');
    }

    setUser(savedUser);
    setAppointments(savedAppointments);
    setAiScans(savedScans);
    setRecentActivity(savedActivity);
    setWaterIntake(currentWater);
    setSavedDoctorsCount(sDoctors.length);
    setSavedHospitalsCount(sHospitals.length);

    const todayStr = new Date().toDateString();
    const activeTasks = tasks.filter(t => !t.completed_dates?.includes(todayStr));
    setActiveTasksCount(activeTasks.length);
  }, []);

  const addWater = () => {
    if (waterIntake < 8) {
      const newAmount = waterIntake + 1;
      setWaterIntake(newAmount);
      localStorage.setItem('water_intake', newAmount.toString());
    }
  };

  const formatDate = (isoString) => {
    const date = new Date(isoString);
    return date.toLocaleString('en-US', { 
      day: '2-digit', month: 'short', year: 'numeric', 
      hour: '2-digit', minute: '2-digit', hour12: true 
    });
  };

  const handleSignOut = () => {
    if (window.confirm('Are you sure you want to sign out? This will clear all your local session data.')) {
      localStorage.clear();
      navigate('/');
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <div style={styles.avatar}>{user ? user.name.charAt(0).toUpperCase() : 'S'}</div>
        <h2 style={styles.userName}>{user ? user.name : 'Guest User'}</h2>
        <p style={styles.userEmail}>{user ? user.email : 'guest@symptocare.com'}</p>
      </div>

      <div style={styles.statsGrid}>
        <div style={styles.statCard}>
          <div style={{...styles.iconWrapper, backgroundColor: '#e0f2fe'}}>
            <Calendar size={20} color="#0284c7" />
          </div>
          <span style={styles.statValue}>{appointments.length}</span>
          <span style={styles.statLabel}>Appointments</span>
        </div>
        
        <div style={styles.statCard}>
          <div style={{...styles.iconWrapper, backgroundColor: '#ffe4e6'}}>
            <Heart size={20} color="#e11d48" />
          </div>
          <span style={styles.statValue}>{savedDoctorsCount}</span>
          <span style={styles.statLabel}>Saved Doctors</span>
        </div>

        <div style={styles.statCard}>
          <div style={{...styles.iconWrapper, backgroundColor: '#f3e8ff'}}>
            <Bookmark size={20} color="#9333ea" />
          </div>
          <span style={styles.statValue}>{savedHospitalsCount}</span>
          <span style={styles.statLabel}>Saved Hospitals</span>
        </div>

        <div style={styles.statCard}>
          <div style={{...styles.iconWrapper, backgroundColor: '#dcfce7'}}>
            <Activity size={20} color="#16a34a" />
          </div>
          <span style={styles.statValue}>{aiScans.length}</span>
          <span style={styles.statLabel}>AI Scans</span>
        </div>
      </div>

      <div style={{...styles.waterCard, backgroundColor: '#fef3c7', borderColor: '#fde68a', cursor: 'pointer'}} onClick={() => navigate('/recovery-plan')}>
        <div style={{...styles.waterIcon, color: '#d97706'}}>
          <ListChecks size={24} />
        </div>
        <div style={styles.waterInfo}>
          <h3 style={styles.waterTitle}>Recovery Tasks</h3>
          <p style={{...styles.waterSubtitle, color: '#b45309'}}>{activeTasksCount} tasks remaining today</p>
        </div>
        <ChevronRight size={20} color="#d97706" />
      </div>

      <div style={styles.waterCard}>
        <div style={styles.waterIcon}>
          <Droplets size={24} color="#38bdf8" />
        </div>
        <div style={styles.waterInfo}>
          <h3 style={styles.waterTitle}>Daily Water Intake</h3>
          <p style={styles.waterSubtitle}>{waterIntake}/8 Glasses</p>
        </div>
        <button 
          style={{...styles.addBtn, opacity: waterIntake >= 8 ? 0.5 : 1}} 
          onClick={addWater}
          disabled={waterIntake >= 8}
        >
          {waterIntake >= 8 ? '✓' : '+'}
        </button>
      </div>

      <div style={styles.section}>
        <h3 style={styles.sectionTitle}>Recent Activity</h3>
        <div style={styles.activityList}>
          {recentActivity.length === 0 ? (
            <p style={{fontSize: 14, color: '#64748b'}}>No recent activity yet. Analyze symptoms or book an appointment to see them here.</p>
          ) : (
            recentActivity.map(activity => (
              <div key={activity.id} style={styles.activityItem}>
                <div style={{
                  ...styles.activityDot, 
                  backgroundColor: activity.type === 'scan' ? '#16a34a' : '#38bdf8'
                }} />
                <div style={styles.activityContent}>
                  <p style={styles.activityTitle}>{activity.title}</p>
                  <p style={styles.activityTime}>{formatDate(activity.date)}</p>
                </div>
              </div>
            ))
          )}
        </div>
      </div>

      <div style={styles.settingsSection}>
        <button style={styles.settingBtn} onClick={handleSignOut}>
          <span style={{display: 'flex', alignItems: 'center', gap: 12}}>
            <LogOut size={20} color="#ef4444" />
            <span style={{color: '#ef4444', fontWeight: 500}}>Sign Out</span>
          </span>
          <ChevronRight size={20} color="#94a3b8" />
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    minHeight: '100%',
    backgroundColor: '#ffffff',
    padding: '24px 20px',
  },
  header: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    marginBottom: '32px',
    marginTop: '24px',
  },
  avatar: {
    width: '80px',
    height: '80px',
    borderRadius: '40px',
    backgroundColor: '#38bdf8',
    color: '#ffffff',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '32px',
    fontWeight: '700',
    marginBottom: '16px',
    boxShadow: '0 4px 10px rgba(56, 189, 248, 0.3)',
  },
  userName: {
    fontSize: '20px',
    fontWeight: '700',
    color: '#0f172a',
    marginBottom: '4px',
  },
  userEmail: {
    fontSize: '14px',
    color: '#64748b',
  },
  statsGrid: {
    display: 'grid',
    gridTemplateColumns: '1fr 1fr',
    gap: '16px',
    marginBottom: '32px',
  },
  statCard: {
    backgroundColor: '#f8fafc',
    borderRadius: '16px',
    padding: '16px',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'flex-start',
    border: '1px solid #f1f5f9',
  },
  iconWrapper: {
    width: '36px',
    height: '36px',
    borderRadius: '10px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: '12px',
  },
  statValue: {
    fontSize: '20px',
    fontWeight: '700',
    color: '#0f172a',
    marginBottom: '2px',
  },
  statLabel: {
    fontSize: '12px',
    color: '#64748b',
  },
  waterCard: {
    display: 'flex',
    alignItems: 'center',
    backgroundColor: '#f0f9ff',
    borderRadius: '16px',
    padding: '16px',
    border: '1px solid #e0f2fe',
    marginBottom: '32px',
  },
  waterIcon: {
    width: '48px',
    height: '48px',
    borderRadius: '24px',
    backgroundColor: '#ffffff',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: '16px',
    boxShadow: '0 2px 4px rgba(56, 189, 248, 0.1)',
  },
  waterInfo: {
    flex: 1,
  },
  waterTitle: {
    fontSize: '15px',
    fontWeight: '600',
    color: '#0f172a',
    marginBottom: '2px',
  },
  waterSubtitle: {
    fontSize: '13px',
    color: '#0284c7',
  },
  addBtn: {
    width: '32px',
    height: '32px',
    borderRadius: '8px',
    backgroundColor: '#38bdf8',
    color: '#ffffff',
    border: 'none',
    fontSize: '20px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    cursor: 'pointer',
  },
  section: {
    marginBottom: '32px',
  },
  sectionTitle: {
    fontSize: '16px',
    fontWeight: '700',
    color: '#0f172a',
    marginBottom: '16px',
  },
  activityList: {
    display: 'flex',
    flexDirection: 'column',
    gap: '16px',
  },
  activityItem: {
    display: 'flex',
    alignItems: 'flex-start',
    gap: '12px',
  },
  activityDot: {
    width: '10px',
    height: '10px',
    borderRadius: '5px',
    backgroundColor: '#38bdf8',
    marginTop: '6px',
  },
  activityContent: {
    flex: 1,
  },
  activityTitle: {
    fontSize: '14px',
    fontWeight: '500',
    color: '#0f172a',
    marginBottom: '4px',
    lineHeight: 1.4,
  },
  activityTime: {
    fontSize: '12px',
    color: '#64748b',
  },
  settingsSection: {
    marginTop: 'auto',
    borderTop: '1px solid #f1f5f9',
    paddingTop: '16px',
  },
  settingBtn: {
    width: '100%',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: '16px 0',
    backgroundColor: 'transparent',
    border: 'none',
    cursor: 'pointer',
  }
};

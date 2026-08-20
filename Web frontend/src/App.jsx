import { Routes, Route, Navigate } from 'react-router-dom';
import MainLayout from './layouts/MainLayout';
import Onboarding from './pages/Onboarding';
import SignUp from './pages/SignUp';
import SignIn from './pages/SignIn';
import Home from './pages/Home';
import Symptoms from './pages/Symptoms';
import Doctors from './pages/Doctors';
import Hospitals from './pages/Hospitals';
import Profile from './pages/Profile';
import RecoveryPlan from './pages/RecoveryPlan';
import { useEffect, useRef } from 'react';

function useNotifications() {
  const lastNotified = useRef({});

  useEffect(() => {
    if ('Notification' in window && Notification.permission === 'default') {
      Notification.requestPermission();
    }

    const interval = setInterval(() => {
      if (!('Notification' in window) || Notification.permission !== 'granted') return;

      const tasks = JSON.parse(localStorage.getItem('recovery_tasks') || '[]');
      const now = new Date();
      let hours = now.getHours();
      let minutes = now.getMinutes();
      const ampm = hours >= 12 ? 'PM' : 'AM';
      hours = hours % 12 || 12;
      
      const currentTimeStr = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')} ${ampm}`;
      const todayStr = now.toDateString();

      tasks.forEach(task => {
        const createdDate = new Date(task.created_at);
        const diffDays = Math.floor((now - createdDate) / (1000 * 60 * 60 * 24));
        if (diffDays > task.repeatDays) return;
        
        if (task.completed_dates?.includes(todayStr)) return;

        if (task.reminderTimes.includes(currentTimeStr)) {
          const notificationKey = `${task.id}-${todayStr}-${currentTimeStr}`;
          if (!lastNotified.current[notificationKey]) {
            new Notification('Recovery Task Reminder', {
              body: `It's time to: ${task.name}`,
            });
            lastNotified.current[notificationKey] = true;
          }
        }
      });
    }, 30000);

    return () => clearInterval(interval);
  }, []);
}

function App() {
  useNotifications();
  
  return (
    <div className="app-container">
      <Routes>
        <Route path="/" element={<Navigate to="/onboarding" replace />} />
        <Route path="/onboarding" element={<Onboarding />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/signin" element={<SignIn />} />
        
        {/* Protected/Main App Routes wrapped in BottomNav Layout */}
        <Route element={<MainLayout />}>
          <Route path="/home" element={<Home />} />
          <Route path="/symptoms" element={<Symptoms />} />
          <Route path="/doctors" element={<Doctors />} />
          <Route path="/hospitals" element={<Hospitals />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/recovery-plan" element={<RecoveryPlan />} />
        </Route>
      </Routes>
    </div>
  );
}

export default App;

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Bell, HeartPulse, Activity, AlertTriangle, Phone, ActivitySquare } from 'lucide-react';

export default function Home() {
  const navigate = useNavigate();
  const [selectedEmoji, setSelectedEmoji] = useState(null);

  const handleEmojiClick = (idx) => {
    setSelectedEmoji(idx);
    // In a real app, this would send a POST to the backend
  };

  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <div>
          <h1 style={styles.greeting}>Welcome to SymptoCare</h1>
          <p style={styles.subtitle}>Your personal health assistant</p>
        </div>
        <div style={styles.headerIcons}>
          <button style={styles.iconBtn} onClick={() => alert('Notifications coming soon!')}>
            <Bell size={20} color="#0f172a" />
          </button>
        </div>
      </header>

      <div style={styles.dashboardGrid}>
        {/* Left Column */}
        <div style={styles.mainColumn}>
          <section style={styles.scanCard}>
            <div style={styles.scanIconWrapper}>
              <HeartPulse size={48} color="#38bdf8" />
            </div>
            <div style={styles.scanText}>
              <h2 style={styles.scanTitle}>AI Symptom Checker</h2>
              <p style={styles.scanDesc}>Get an instant AI-powered health analysis using our advanced medical algorithms.</p>
            </div>
            <button style={styles.scanBtn} onClick={() => navigate('/symptoms')}>
              Start Guided Scan
            </button>
          </section>

          <section style={styles.section}>
            <h3 style={styles.sectionTitle}>Daily Wellness Check-in</h3>
            <div style={styles.emojiContainer}>
              {['😄', '🙂', '😐', '😔', '🤒'].map((emoji, idx) => (
                <button 
                  key={idx} 
                  style={{
                    ...styles.emojiBtn, 
                    backgroundColor: selectedEmoji === idx ? '#e0f2fe' : '#ffffff',
                    borderColor: selectedEmoji === idx ? '#38bdf8' : '#e2e8f0'
                  }}
                  onClick={() => handleEmojiClick(idx)}
                >
                  {emoji}
                </button>
              ))}
            </div>
          </section>

          <section style={styles.section}>
            <h3 style={styles.sectionTitle}>
              <ActivitySquare size={20} color="#38bdf8" style={{marginRight: 8}} />
              Health Articles
            </h3>
            <div style={styles.articlesGrid}>
              <a href="https://www.sleepfoundation.org/how-sleep-works/why-do-we-need-sleep" target="_blank" rel="noreferrer" style={{textDecoration: 'none'}}>
                <div style={styles.articleCard}>
                  <div style={{...styles.articleImg, backgroundColor: '#ffe4e6'}}>
                    <HeartPulse size={32} color="#f43f5e" />
                  </div>
                  <p style={styles.articleTitle}>The importance of 8 Hours of Sleep</p>
                  <p style={{fontSize: 13, color: '#64748b', marginTop: 4}}>Learn why sleep is critical for recovery.</p>
                </div>
              </a>
              <a href="https://www.mayoclinic.org/healthy-lifestyle/fitness/expert-answers/heart-rate/faq-20057979" target="_blank" rel="noreferrer" style={{textDecoration: 'none'}}>
                <div style={styles.articleCard}>
                  <div style={{...styles.articleImg, backgroundColor: '#e0f2fe'}}>
                    <Activity size={32} color="#0284c7" />
                  </div>
                  <p style={styles.articleTitle}>Understanding Your Heart Rate</p>
                  <p style={{fontSize: 13, color: '#64748b', marginTop: 4}}>What your resting heart rate says about you.</p>
                </div>
              </a>
            </div>
          </section>
        </div>

        {/* Right Column */}
        <div style={styles.sideColumn}>
          <section style={styles.section}>
            <h3 style={styles.sectionTitle}>
              <Activity size={18} color="#4ade80" style={{marginRight: 8}} />
              Health Tip of the Day
            </h3>
            <div style={styles.tipCard}>
              <p style={styles.tipText}>
                Drink at least 8 glasses of water today. Staying hydrated keeps your memory sharp, your mood stable and your motivation intact.
              </p>
            </div>
          </section>

          <section style={styles.section}>
            <h3 style={styles.sectionTitle}>
              <AlertTriangle size={18} color="#f59e0b" style={{marginRight: 8}} />
              Did You Know?
            </h3>
            <div style={{...styles.tipCard, backgroundColor: '#fdf4ff', border: '1px solid #f5d0fe'}}>
              <p style={{...styles.tipText, color: '#86198f'}}>
                Laughing is good for the heart and can increase blood flow by 20 percent.
              </p>
            </div>
          </section>

          <section style={styles.section}>
            <h3 style={styles.sectionTitle}>
              <Phone size={18} color="#ef4444" style={{marginRight: 8}} />
              Emergency Contacts
            </h3>
            <div style={styles.emergencyContainer}>
              <div style={styles.emergencyRow}>
                <span style={styles.emergencyLabel}>Ambulance</span>
                <a href="tel:108" style={styles.emergencyNumber}>108</a>
              </div>
              <div style={styles.emergencyRow}>
                <span style={styles.emergencyLabel}>General Emergency</span>
                <a href="tel:112" style={styles.emergencyNumber}>112</a>
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
  );
}

const styles = {
  container: {
    width: '100%',
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '32px',
  },
  greeting: {
    fontSize: '28px',
    fontWeight: '700',
    color: '#0f172a',
    marginBottom: '4px',
  },
  subtitle: {
    fontSize: '16px',
    color: '#64748b',
  },
  headerIcons: {
    display: 'flex',
    gap: '12px',
  },
  iconBtn: {
    background: '#ffffff',
    border: '1px solid #e2e8f0',
    borderRadius: '12px',
    width: '48px',
    height: '48px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    cursor: 'pointer',
    boxShadow: '0 2px 4px rgba(0,0,0,0.02)',
  },
  dashboardGrid: {
    display: 'grid',
    gridTemplateColumns: '2fr 1fr',
    gap: '32px',
  },
  mainColumn: {
    display: 'flex',
    flexDirection: 'column',
    gap: '32px',
  },
  sideColumn: {
    display: 'flex',
    flexDirection: 'column',
    gap: '32px',
  },
  scanCard: {
    backgroundColor: '#38bdf8',
    borderRadius: '24px',
    padding: '40px',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    textAlign: 'center',
    boxShadow: '0 10px 25px -5px rgba(56, 189, 248, 0.4)',
  },
  scanIconWrapper: {
    width: '96px',
    height: '96px',
    backgroundColor: '#ffffff',
    borderRadius: '24px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: '24px',
  },
  scanTitle: {
    color: '#ffffff',
    fontSize: '28px',
    fontWeight: '700',
    marginBottom: '12px',
  },
  scanDesc: {
    color: 'rgba(255, 255, 255, 0.9)',
    fontSize: '16px',
    marginBottom: '32px',
    maxWidth: '400px',
  },
  scanBtn: {
    backgroundColor: '#ffffff',
    color: '#38bdf8',
    border: 'none',
    borderRadius: '12px',
    padding: '16px 32px',
    fontWeight: '700',
    fontSize: '18px',
    cursor: 'pointer',
  },
  sectionTitle: {
    fontSize: '20px',
    fontWeight: '700',
    color: '#0f172a',
    marginBottom: '20px',
    display: 'flex',
    alignItems: 'center',
  },
  emojiContainer: {
    display: 'flex',
    gap: '16px',
  },
  emojiBtn: {
    background: '#ffffff',
    border: '1px solid #e2e8f0',
    borderRadius: '16px',
    width: '72px',
    height: '72px',
    fontSize: '36px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    cursor: 'pointer',
    boxShadow: '0 2px 4px rgba(0,0,0,0.02)',
    transition: 'transform 0.2s ease',
  },
  tipCard: {
    backgroundColor: '#ffffff',
    border: '1px solid #e2e8f0',
    borderRadius: '16px',
    padding: '24px',
    boxShadow: '0 4px 6px rgba(0,0,0,0.02)',
  },
  tipText: {
    fontSize: '15px',
    color: '#475569',
    lineHeight: 1.6,
  },
  emergencyContainer: {
    backgroundColor: '#ffffff',
    border: '1px solid #fee2e2',
    borderRadius: '16px',
    padding: '0 24px',
    boxShadow: '0 4px 6px rgba(0,0,0,0.02)',
  },
  emergencyRow: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '20px 0',
    borderBottom: '1px solid #f1f5f9',
  },
  emergencyLabel: {
    fontSize: '16px',
    fontWeight: '600',
    color: '#0f172a',
  },
  emergencyNumber: {
    backgroundColor: '#fef2f2',
    color: '#ef4444',
    padding: '8px 20px',
    borderRadius: '8px',
    fontWeight: '700',
    textDecoration: 'none',
    fontSize: '16px',
  },
  articlesGrid: {
    display: 'grid',
    gridTemplateColumns: '1fr 1fr',
    gap: '24px',
  },
  articleCard: {
    backgroundColor: '#ffffff',
    border: '1px solid #e2e8f0',
    borderRadius: '20px',
    padding: '24px',
    boxShadow: '0 4px 6px rgba(0,0,0,0.02)',
  },
  articleImg: {
    width: '100%',
    height: '140px',
    borderRadius: '12px',
    marginBottom: '16px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  articleTitle: {
    fontSize: '16px',
    fontWeight: '700',
    color: '#0f172a',
    lineHeight: 1.4,
  }
};

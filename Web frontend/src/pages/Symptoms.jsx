import React, { useState, useEffect } from 'react';
import { Search, Activity, Info, Loader, X, Check } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

const categoryMeta = {
  gastrointestinal: { name: 'Digestive', icon: '🍽️', color: '#fca5a5' },
  cardiac: { name: 'Heart & Cardio', icon: '❤️', color: '#f87171' },
  respiratory: { name: 'Respiratory', icon: '🫁', color: '#38bdf8' },
  skin: { name: 'Skin & Allergy', icon: '🦠', color: '#a78bfa' },
  musculoskeletal: { name: 'Joints & Muscle', icon: '💪', color: '#60a5fa' },
  neurological: { name: 'Brain & Nerves', icon: '🧠', color: '#34d399' },
  eyes_ent: { name: 'Eyes & ENT', icon: '👃', color: '#fbbf24' },
  urinary: { name: 'Urinary', icon: '🚽', color: '#f59e0b' },
  metabolic: { name: 'Metabolic & Hormonal', icon: '🧬', color: '#ec4899' },
  general: { name: 'General & Systemic', icon: '🏥', color: '#94a3b8' },
  liver: { name: 'Liver & Jaundice', icon: '🧪', color: '#14b8a6' },
  reproductive: { name: 'Other & Reproductive', icon: '🌺', color: '#f43f5e' },
  infection_markers: { name: 'Infection Markers', icon: '🛡️', color: '#8b5cf6' },
  bowel: { name: 'Bowel & Rectal', icon: '🧻', color: '#d97706' }
};

export default function Symptoms() {
  const navigate = useNavigate();
  const [symptomText, setSymptomText] = useState('');
  const [analysisResult, setAnalysisResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const [selectedCategory, setSelectedCategory] = useState(null);
  const [selectedGuidedSymptoms, setSelectedGuidedSymptoms] = useState([]);
  const [categories, setCategories] = useState([]);

  const commonSymptoms = ['Fever', 'Headache', 'Cough', 'Fatigue', 'Nausea'];

  useEffect(() => {
    const fetchSymptoms = async () => {
      try {
        const response = await fetch('http://10.250.236.211:5000/api/symptoms');
        const data = await response.json();
        if (data.success && data.data?.symptoms) {
          const grouped = {};
          data.data.symptoms.forEach(sym => {
            const catKey = sym.category || 'general';
            if (!grouped[catKey]) {
              grouped[catKey] = [];
            }
            grouped[catKey].push({ id: sym.name, label: sym.display });
          });

          const categoryList = Object.keys(grouped).map(catKey => {
            const meta = categoryMeta[catKey] || { name: catKey.toUpperCase(), icon: '❓', color: '#94a3b8' };
            return {
              name: meta.name,
              icon: meta.icon,
              color: meta.color,
              symptoms: grouped[catKey]
            };
          });

          categoryList.sort((a, b) => a.name.localeCompare(b.name));
          setCategories(categoryList);
        }
      } catch (err) {
        console.error('Error fetching symptoms:', err);
      }
    };

    fetchSymptoms();
  }, []);

  const handleAnalyzeText = async () => {
    if (!symptomText.trim()) {
      setError('Please describe your symptoms first.');
      return;
    }
    await fetchAnalysis({ message: symptomText });
  };

  const handleAnalyzeGuided = async () => {
    if (selectedGuidedSymptoms.length === 0) {
      alert('Please select at least one symptom.');
      return;
    }
    await fetchAnalysis({ symptoms: selectedGuidedSymptoms });
    setSelectedCategory(null);
    setSelectedGuidedSymptoms([]);
  };

  const fetchAnalysis = async (payload) => {
    setLoading(true);
    setError('');
    try {
      const response = await fetch('http://10.250.236.211:5000/api/analyze-symptoms', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      if (data.success && data.data) {
        setAnalysisResult({
          disease: data.data.predictedDisease,
          severity: data.data.severityLevel || 'Unknown',
          description: data.data.diseaseDescription,
          precautions: data.data.precautions || [],
          specialist: data.data.recommendedSpecialist,
          confidence: data.data.confidence
        });

        // Save to localStorage
        const scans = JSON.parse(localStorage.getItem('ai_scans') || '[]');
        scans.push({ 
          id: Date.now(),
          disease: data.data.predictedDisease,
          date: new Date().toISOString() 
        });
        localStorage.setItem('ai_scans', JSON.stringify(scans));

        const activities = JSON.parse(localStorage.getItem('recent_activity') || '[]');
        activities.unshift({
          id: Date.now(),
          title: `AI Analysis: ${data.data.predictedDisease}`,
          date: new Date().toISOString(),
          type: 'scan'
        });
        localStorage.setItem('recent_activity', JSON.stringify(activities.slice(0, 10)));
      } else {
        setError(data.error?.message || 'Failed to analyze symptoms.');
      }
    } catch (err) {
      console.error('API Error:', err);
      setError('Could not connect to the backend server.');
    } finally {
      setLoading(false);
    }
  };

  const toggleGuidedSymptom = (id) => {
    setSelectedGuidedSymptoms(prev => 
      prev.includes(id) ? prev.filter(s => s !== id) : [...prev, id]
    );
  };

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <div style={styles.headerTop}>
          <div style={styles.avatar}>U</div>
          <span style={styles.userEmail}>user@symptocare.com</span>
        </div>
      </div>

      <div style={styles.content}>
        <h2 style={styles.title}>Describe your symptoms</h2>
        <p style={styles.subtitle}>Type your symptoms or select from below</p>

        <div className="input-field" style={{marginBottom: error ? '8px' : '24px'}}>
          <Search className="input-icon" />
          <input 
            type="text" 
            placeholder="e.g. I have a severe headache..." 
            value={symptomText}
            onChange={(e) => setSymptomText(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleAnalyzeText()}
          />
        </div>
        
        {error && <p style={{color: '#ef4444', fontSize: '14px', marginBottom: '16px'}}>{error}</p>}

        <div style={styles.section}>
          <h3 style={styles.sectionTitle}>Common Symptoms</h3>
          <div style={styles.chipContainer}>
            {commonSymptoms.map((sym, idx) => (
              <button 
                key={idx} 
                style={styles.chip}
                onClick={() => setSymptomText(prev => prev ? `${prev}, ${sym}` : sym)}
              >
                {sym}
              </button>
            ))}
          </div>
        </div>

        <button 
          className="btn-primary" 
          style={{...styles.analyzeBtn, opacity: loading ? 0.7 : 1}} 
          onClick={handleAnalyzeText}
          disabled={loading}
        >
          {loading ? <Loader size={20} className="spinner" /> : <Activity size={20} />}
          {loading ? 'Analyzing...' : 'Analyze Symptoms'}
        </button>

        <div style={styles.section}>
          <h3 style={styles.sectionTitle}>Guided Symptom Selection</h3>
          <p style={{fontSize: 14, color: '#64748b', marginBottom: 16}}>Select a category to pick symptoms from a list.</p>
          <div style={styles.categoriesGrid}>
            {categories.map((cat, idx) => (
              <div key={idx} style={styles.categoryCard} onClick={() => setSelectedCategory(cat)}>
                <div style={{...styles.categoryIcon, backgroundColor: `${cat.color}20`}}>
                  <span style={{fontSize: '24px'}}>{cat.icon}</span>
                </div>
                <span style={styles.categoryName}>{cat.name}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {selectedCategory && (
        <div style={styles.modalOverlay}>
          <div style={styles.modalContent}>
            <div style={{...styles.modalHeader, backgroundColor: selectedCategory.color}}>
              <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
                <div>
                  <h3 style={styles.modalTitle}>Select Symptoms</h3>
                  <h2 style={{...styles.diseaseName, marginBottom: 0}}>{selectedCategory.icon} {selectedCategory.name}</h2>
                </div>
                <button style={styles.headerCloseBtn} onClick={() => { setSelectedCategory(null); setSelectedGuidedSymptoms([]); }}>
                  <X size={24} />
                </button>
              </div>
            </div>
            <div style={styles.modalBody}>
              <div style={styles.symptomList}>
                {selectedCategory.symptoms.map(sym => (
                  <div 
                    key={sym.id} 
                    style={{
                      ...styles.symptomItem, 
                      borderColor: selectedGuidedSymptoms.includes(sym.id) ? selectedCategory.color : '#e2e8f0',
                      backgroundColor: selectedGuidedSymptoms.includes(sym.id) ? `${selectedCategory.color}10` : '#ffffff',
                    }}
                    onClick={() => toggleGuidedSymptom(sym.id)}
                  >
                    <span style={{fontWeight: selectedGuidedSymptoms.includes(sym.id) ? 600 : 400, color: '#0f172a'}}>
                      {sym.label}
                    </span>
                    {selectedGuidedSymptoms.includes(sym.id) && <Check size={20} color={selectedCategory.color} />}
                  </div>
                ))}
              </div>
              <button 
                className="btn-primary" 
                style={{width: '100%', marginTop: 24, padding: 16, backgroundColor: selectedCategory.color, borderColor: selectedCategory.color}} 
                onClick={handleAnalyzeGuided}
                disabled={loading}
              >
                {loading ? 'Analyzing...' : `Analyze Selected (${selectedGuidedSymptoms.length})`}
              </button>
            </div>
          </div>
        </div>
      )}

      {analysisResult && (
        <div style={styles.modalOverlay}>
          <div style={styles.modalContent}>
            <div style={styles.modalHeader}>
              <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
                <h3 style={styles.modalTitle}>Analysis Result</h3>
                <button style={styles.headerCloseBtn} onClick={() => setAnalysisResult(null)}>
                  <X size={24} />
                </button>
              </div>
            </div>
            
            <div style={styles.modalBody}>
              <div style={styles.resultBox}>
                <p style={styles.predictedDisease}>Predicted Disease: <span style={{fontWeight: 700}}>{analysisResult.disease}</span></p>
              </div>

              <div style={{...styles.infoSection, borderBottom: 'none', paddingBottom: 0, marginBottom: 24}}>
                <p style={{fontSize: '15px', color: '#475569', lineHeight: 1.5, margin: 0}}>
                  Based on your symptoms, you should consult a <span style={{fontWeight: 700, color: '#0369a1'}}>{analysisResult.specialist}</span>.
                </p>
              </div>

              <button 
                className="btn-primary" 
                style={{width: '100%', padding: 16}} 
                onClick={() => {
                  const specialist = analysisResult.specialist;
                  setAnalysisResult(null);
                  if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(
                      (position) => {
                        const lat = position.coords.latitude;
                        const lng = position.coords.longitude;
                        navigate(`/doctors?specialist=${encodeURIComponent(specialist)}&lat=${lat}&lng=${lng}`);
                      },
                      (error) => {
                        console.error("Error getting location:", error);
                        navigate(`/doctors?specialist=${encodeURIComponent(specialist)}`);
                      },
                      { enableHighAccuracy: true, timeout: 5000 }
                    );
                  } else {
                    navigate(`/doctors?specialist=${encodeURIComponent(specialist)}`);
                  }
                }}
              >
                Find Nearby {analysisResult.specialist}s
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

const styles = {
  container: { width: '100%', padding: '0' },
  header: { backgroundColor: '#38bdf8', padding: '40px 32px', color: '#ffffff' },
  headerTop: { display: 'flex', alignItems: 'center', gap: '12px', maxWidth: '800px', margin: '0 auto' },
  avatar: { width: '40px', height: '40px', borderRadius: '20px', backgroundColor: 'rgba(255, 255, 255, 0.2)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: '600', fontSize: '16px' },
  userEmail: { fontSize: '14px', fontWeight: '500' },
  content: { maxWidth: '800px', margin: '0 auto', padding: '32px 24px' },
  title: { fontSize: '24px', fontWeight: '700', color: '#0f172a', marginBottom: '8px' },
  subtitle: { fontSize: '15px', color: '#64748b', marginBottom: '24px' },
  section: { marginBottom: '32px' },
  sectionTitle: { fontSize: '16px', fontWeight: '700', color: '#0f172a', marginBottom: '16px' },
  chipContainer: { display: 'flex', flexWrap: 'wrap', gap: '12px' },
  chip: { padding: '10px 20px', backgroundColor: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '20px', fontSize: '14px', color: '#475569', cursor: 'pointer', transition: 'all 0.2s' },
  analyzeBtn: { width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '10px', fontSize: '16px', marginBottom: '32px', padding: '16px' },
  categoriesGrid: { display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '16px' },
  categoryCard: { backgroundColor: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '16px', padding: '24px 16px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: '12px', boxShadow: '0 4px 6px rgba(0,0,0,0.02)', cursor: 'pointer' },
  categoryIcon: { width: '48px', height: '48px', borderRadius: '16px', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '24px' },
  categoryName: { fontSize: '14px', fontWeight: '600', color: '#0f172a' },
  modalOverlay: { position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, backgroundColor: 'rgba(15, 23, 42, 0.6)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1000 },
  modalContent: { backgroundColor: '#ffffff', borderRadius: '24px', width: '90%', maxWidth: '500px', maxHeight: '90vh', overflowY: 'auto', position: 'relative' },
  modalHeader: { backgroundColor: '#38bdf8', padding: '24px', color: '#ffffff' },
  headerCloseBtn: { background: 'none', border: 'none', color: '#ffffff', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '8px', borderRadius: '50%', backgroundColor: 'rgba(255,255,255,0.2)' },
  modalTitle: { fontSize: '14px', fontWeight: '600', opacity: 0.9, marginBottom: '8px' },
  diseaseName: { fontSize: '24px', fontWeight: '700', marginBottom: '16px' },
  modalBody: { padding: '24px' },
  resultBox: { backgroundColor: '#f8fafc', borderRadius: '16px', padding: '16px', marginBottom: '24px', border: '1px solid #f1f5f9' },
  predictedDisease: { fontSize: '16px', color: '#0f172a', marginBottom: '8px' },
  severity: { fontSize: '14px', color: '#64748b' },
  infoSection: { marginBottom: '20px', paddingBottom: '20px', borderBottom: '1px solid #f1f5f9' },
  infoTitle: { fontSize: '15px', fontWeight: '600', color: '#0f172a', marginBottom: '12px' },
  infoText: { fontSize: '14px', color: '#475569', lineHeight: 1.5 },
  list: { margin: 0, paddingLeft: '20px' },
  listItem: { fontSize: '14px', color: '#475569', marginBottom: '6px', lineHeight: 1.4 },
  specialistBadge: { display: 'inline-flex', alignItems: 'center', gap: '8px', backgroundColor: '#e0f2fe', padding: '8px 16px', borderRadius: '8px', marginTop: '8px' },
  symptomList: { display: 'flex', flexDirection: 'column', gap: '12px' },
  symptomItem: { padding: '16px', border: '2px solid', borderRadius: '12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', cursor: 'pointer', transition: 'all 0.2s' }
};

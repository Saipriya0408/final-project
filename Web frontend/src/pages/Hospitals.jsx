import React, { useState, useEffect } from 'react';
import { Search, MapPin, Navigation, Star, Loader, Bookmark } from 'lucide-react';

export default function Hospitals() {
  const [hospitals, setHospitals] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Location states
  const [locationState, setLocationState] = useState('normal'); // 'normal', 'loading', 'enabled', 'permission_denied', 'gps_off', 'no_results', 'unable_to_connect'
  const [coords, setCoords] = useState(null);

  useEffect(() => {
    if (coords) {
      fetchHospitalsWithCoords(coords.lat, coords.lng);
    } else {
      fetchHospitals();
    }
  }, [coords]);

  const fetchHospitals = async () => {
    try {
      const response = await fetch('http://10.250.236.211:5000/api/hospitals');
      const data = await response.json();
      
      if (data.success) {
        setHospitals(data.data.hospitals || []);
      } else {
        setError('Failed to fetch hospitals');
      }
    } catch (err) {
      console.error(err);
      setError('Could not connect to backend');
    } finally {
      setLoading(false);
    }
  };

  const fetchHospitalsWithCoords = async (lat, lng) => {
    setLoading(true);
    setError('');
    try {
      const response = await fetch(`http://10.250.236.211:5000/api/hospitals?lat=${lat}&lng=${lng}`);
      const data = await response.json();
      
      if (data.success) {
        const list = data.data.hospitals || [];
        setHospitals(list);
        if (list.length === 0) {
          setLocationState('no_results');
        } else {
          setLocationState('enabled');
        }
      } else {
        setLocationState('unable_to_connect');
        setError('Failed to fetch hospitals');
      }
    } catch (err) {
      console.error(err);
      setLocationState('unable_to_connect');
      setError('Could not connect to backend');
    } finally {
      setLoading(false);
    }
  };

  const handleUseLocation = () => {
    if (!navigator.geolocation) {
      setLocationState('gps_off');
      alert("Geolocation is not supported by your browser");
      return;
    }

    setLocationState('loading');
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const lat = position.coords.latitude;
        const lng = position.coords.longitude;
        setCoords({ lat, lng });
      },
      (error) => {
        console.error(error);
        if (error.code === error.PERMISSION_DENIED) {
          setLocationState('permission_denied');
        } else {
          setLocationState('gps_off');
        }
      },
      { enableHighAccuracy: true, timeout: 10000 }
    );
  };

  const handleNavigate = (hospital) => {
    const url = `https://www.google.com/maps/dir/?api=1&destination=${hospital.lat},${hospital.lng}`;
    window.open(url, '_blank');
  };

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <div className="input-field" style={{marginBottom: 0, backgroundColor: '#ffffff'}}>
          <Search className="input-icon" />
          <input type="text" placeholder="Search hospitals..." />
        </div>
      </div>

      {/* Location UI Card */}
      <div style={styles.locationCard}>
        <div style={styles.locationHeader}>
          <MapPin size={20} color="#4ade80" />
          <h3 style={styles.locationTitle}>
            {locationState === 'normal' && "📍 Nearby Hospitals & Clinics"}
            {locationState === 'loading' && "📍 Getting your location..."}
            {locationState === 'enabled' && "✓ Location enabled"}
            {locationState === 'permission_denied' && "📍 Location Permission Required"}
            {locationState === 'gps_off' && "📍 Location is turned off"}
            {locationState === 'no_results' && "No nearby hospitals or clinics found."}
            {locationState === 'unable_to_connect' && "⚠ Unable to connect to SymptoCare server."}
          </h3>
        </div>
        <p style={styles.locationDesc}>
          {locationState === 'normal' && "Find healthcare facilities near your current location."}
          {locationState === 'loading' && "🔎 Finding nearby hospitals... Please wait."}
          {locationState === 'enabled' && "Showing hospitals and clinics near you."}
          {locationState === 'permission_denied' && "Location permission is required to find nearby doctors and hospitals."}
          {locationState === 'gps_off' && "Please turn on Location to find nearby doctors and hospitals."}
          {locationState === 'no_results' && "Try refreshing your location."}
          {locationState === 'unable_to_connect' && "Please check that the SymptoCare server is running."}
        </p>
        {locationState !== 'loading' && (
          <button 
            style={styles.locationBtn}
            onClick={handleUseLocation}
          >
            {locationState === 'enabled' ? "🔄 Refresh Location" : "📍 Use My Location"}
          </button>
        )}
      </div>

      <div style={styles.listContainer}>
        <div style={styles.listHeader}>
          <span style={styles.resultCount}>
            {loading ? 'Searching hospitals...' : `${hospitals.length} hospitals found nearby`}
          </span>
        </div>

        {loading ? (
          <div style={{display: 'flex', justifyContent: 'center', padding: '40px'}}>
            <Loader className="spinner" size={32} color="#4ade80" />
          </div>
        ) : error && hospitals.length === 0 ? (
          <div style={{color: '#ef4444', textAlign: 'center', padding: '20px'}}>{error}</div>
        ) : (
          <div style={styles.list}>
            {hospitals.map(hospital => (
              <div key={hospital.id} style={styles.hospitalCard}>
                <div style={styles.cardHeader}>
                  <div style={styles.hospitalInfo}>
                    <h3 style={styles.hospitalName}>{hospital.name}</h3>
                    <div style={styles.ratingRow}>
                      <Star size={14} fill="#f59e0b" color="#f59e0b" />
                      <span style={styles.rating}>{hospital.rating}</span>
                    </div>
                    <p style={styles.hospitalType}>{hospital.name.toLowerCase().includes('clinic') || hospital.name.toLowerCase().includes('centre') || hospital.name.toLowerCase().includes('care') ? 'Clinic' : 'Hospital'}</p>
                    {hospital._dist_km !== undefined && (
                      <span style={styles.distanceBadge}>{hospital._dist_km.toFixed(1)} km away</span>
                    )}
                  </div>
                  <button 
                    style={{background: 'none', border: 'none', cursor: 'pointer', padding: 4}}
                    onClick={() => {
                      const saved = JSON.parse(localStorage.getItem('saved_hospitals') || '[]');
                      const isSaved = saved.some(h => h.id === hospital.id);
                      if (isSaved) {
                        localStorage.setItem('saved_hospitals', JSON.stringify(saved.filter(h => h.id !== hospital.id)));
                      } else {
                        localStorage.setItem('saved_hospitals', JSON.stringify([...saved, hospital]));
                      }
                      setHospitals([...hospitals]);
                    }}
                  >
                    <Bookmark 
                      size={20} 
                      fill={JSON.parse(localStorage.getItem('saved_hospitals') || '[]').some(h => h.id === hospital.id) ? '#9333ea' : 'none'} 
                      color={JSON.parse(localStorage.getItem('saved_hospitals') || '[]').some(h => h.id === hospital.id) ? '#9333ea' : '#94a3b8'} 
                    />
                  </button>
                </div>

                <div style={styles.addressRow}>
                  <MapPin size={16} color="#64748b" style={{flexShrink: 0}} />
                  <span style={styles.address}>{hospital.address}</span>
                </div>

                <button className="btn-outline" style={styles.navBtn} onClick={() => handleNavigate(hospital)}>
                  <Navigation size={18} />
                  Get Directions
                </button>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    minHeight: '100%',
    backgroundColor: '#f8fafc',
  },
  header: {
    padding: '24px 20px',
    backgroundColor: '#4ade80',
  },
  listContainer: {
    padding: '20px',
  },
  listHeader: {
    marginBottom: '16px',
  },
  resultCount: {
    fontSize: '14px',
    color: '#64748b',
    fontWeight: '500',
  },
  list: {
    display: 'flex',
    flexDirection: 'column',
    gap: '16px',
  },
  hospitalCard: {
    backgroundColor: '#ffffff',
    borderRadius: '16px',
    padding: '16px',
    border: '1px solid #e2e8f0',
    boxShadow: '0 4px 6px rgba(0,0,0,0.02)',
  },
  cardHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: '12px',
  },
  hospitalInfo: {
    flex: 1,
  },
  hospitalName: {
    fontSize: '16px',
    fontWeight: '700',
    color: '#0f172a',
    marginBottom: '4px',
  },
  ratingRow: {
    display: 'flex',
    alignItems: 'center',
    gap: '4px',
    marginBottom: '4px',
  },
  rating: {
    fontSize: '13px',
    color: '#475569',
    fontWeight: '500',
  },
  hospitalType: {
    fontSize: '13px',
    color: '#64748b',
  },
  addressRow: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    backgroundColor: '#f1f5f9',
    padding: '12px',
    borderRadius: '8px',
    marginBottom: '16px',
  },
  address: {
    fontSize: '13px',
    color: '#475569',
  },
  navBtn: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '8px',
    color: '#4ade80',
    borderColor: '#4ade80',
  },
  locationCard: {
    backgroundColor: '#ffffff',
    borderRadius: '16px',
    padding: '16px',
    margin: '16px 20px',
    border: '1px solid #e2e8f0',
    boxShadow: '0 4px 6px rgba(0,0,0,0.02)',
  },
  locationHeader: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    marginBottom: '8px',
  },
  locationTitle: {
    fontSize: '15px',
    fontWeight: '700',
    color: '#0f172a',
    margin: 0,
  },
  locationDesc: {
    fontSize: '13px',
    color: '#64748b',
    marginBottom: '12px',
    lineHeight: '1.4',
  },
  locationBtn: {
    backgroundColor: '#f0fdf4',
    border: '1px solid #4ade80',
    color: '#16a34a',
    padding: '8px 16px',
    borderRadius: '8px',
    fontSize: '13px',
    fontWeight: '600',
    cursor: 'pointer',
    width: '100%',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '6px',
  },
  distanceBadge: {
    display: 'inline-block',
    backgroundColor: '#dcfce7',
    color: '#15803d',
    fontSize: '11px',
    fontWeight: '600',
    padding: '2px 8px',
    borderRadius: '6px',
    marginTop: '4px',
  }
};

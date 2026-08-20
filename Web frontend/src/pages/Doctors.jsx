import React, { useState, useEffect, useRef } from 'react';
import { Search, MapPin, Navigation, Calendar as CalendarIcon, Clock, Loader, Heart } from 'lucide-react';
import { useLocation } from 'react-router-dom';

export default function Doctors() {
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const initialSpecialist = searchParams.get('specialist') || 'All';

  const [activeFilter, setActiveFilter] = useState(initialSpecialist);
  const [showBooking, setShowBooking] = useState(false);
  const [selectedDoctor, setSelectedDoctor] = useState(null);
  
  const [doctors, setDoctors] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [offset, setOffset] = useState(0);
  const [hasMore, setHasMore] = useState(true);
  const observerTarget = useRef(null);
  const limit = 50;

  // New location states
  const latParam = searchParams.get('lat');
  const lngParam = searchParams.get('lng');
  const initialCoords = latParam && lngParam ? { lat: parseFloat(latParam), lng: parseFloat(lngParam) } : null;

  const [locationState, setLocationState] = useState(initialCoords ? 'enabled' : 'normal'); // 'normal', 'loading', 'enabled', 'permission_denied', 'gps_off', 'no_results', 'unable_to_connect'
  const [coords, setCoords] = useState(initialCoords);

  const filters = ['All', 'Cardiologist', 'Neurologist', 'General Physician', 'Pediatrician', 'Dermatologist'];
  
  // Ensure the initial specialist from URL is in the filters list
  if (initialSpecialist !== 'All' && !filters.includes(initialSpecialist)) {
    filters.push(initialSpecialist);
  }

  useEffect(() => {
    setDoctors([]);
    setOffset(0);
    setHasMore(true);
    if (coords) {
      fetchDoctorsWithCoords(coords.lat, coords.lng, activeFilter === 'All' ? '' : activeFilter, 0);
    } else {
      fetchDoctors(activeFilter === 'All' ? '' : activeFilter, 0);
    }
  }, [activeFilter, coords]);

  useEffect(() => {
    const observer = new IntersectionObserver(
      entries => {
        if (entries[0].isIntersecting && !loading && hasMore) {
          const nextOffset = offset + limit;
          setOffset(nextOffset);
          if (coords) {
            fetchDoctorsWithCoords(coords.lat, coords.lng, activeFilter === 'All' ? '' : activeFilter, nextOffset);
          } else {
            fetchDoctors(activeFilter === 'All' ? '' : activeFilter, nextOffset);
          }
        }
      },
      { threshold: 0.1 }
    );

    if (observerTarget.current) {
      observer.observe(observerTarget.current);
    }

    return () => {
      if (observerTarget.current) observer.disconnect();
    };
  }, [loading, hasMore, offset, activeFilter, coords]);

  const fetchDoctors = async (specialist, currentOffset) => {
    setLoading(true);
    try {
      let url = specialist 
        ? `http://10.250.236.211:5000/api/doctors?specialist=${encodeURIComponent(specialist)}`
        : 'http://10.250.236.211:5000/api/doctors';
        
      url += url.includes('?') ? `&limit=${limit}&offset=${currentOffset}` : `?limit=${limit}&offset=${currentOffset}`;
        
      const response = await fetch(url);
      const data = await response.json();
      
      if (data.success) {
        const newDoctors = data.data.doctors || [];
        if (newDoctors.length < limit) setHasMore(false);
        setDoctors(prev => currentOffset === 0 ? newDoctors : [...prev, ...newDoctors]);
      } else {
        setError('Failed to fetch doctors');
      }
    } catch (err) {
      console.error(err);
      setError('Could not connect to backend');
    } finally {
      setLoading(false);
    }
  };

  const fetchDoctorsWithCoords = async (lat, lng, specialist, currentOffset) => {
    setLoading(true);
    setError('');
    try {
      let url = `http://10.250.236.211:5000/api/doctors?lat=${lat}&lng=${lng}`;
      if (specialist) {
        url += `&specialist=${encodeURIComponent(specialist)}`;
      }
      url += `&limit=${limit}&offset=${currentOffset}`;
      
      const response = await fetch(url);
      const data = await response.json();
      
      if (data.success) {
        const newDoctors = data.data.doctors || [];
        if (newDoctors.length < limit) setHasMore(false);
        setDoctors(prev => currentOffset === 0 ? newDoctors : [...prev, ...newDoctors]);
        if (newDoctors.length === 0 && currentOffset === 0) {
          setLocationState('no_results');
        } else {
          setLocationState('enabled');
        }
      } else {
        setLocationState('unable_to_connect');
        setError('Failed to fetch doctors');
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

  const handleBook = (doc) => {
    setSelectedDoctor(doc);
    setShowBooking(true);
  };

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <div className="input-field" style={{marginBottom: 0, backgroundColor: '#ffffff'}}>
          <Search className="input-icon" />
          <input type="text" placeholder="Search doctors..." />
        </div>
      </div>

      <div style={styles.filtersWrapper}>
        <div style={styles.filtersScroll}>
          {filters.map((f, idx) => (
            <button 
              key={idx} 
              style={{
                ...styles.filterChip, 
                backgroundColor: activeFilter === f ? '#38bdf8' : '#ffffff',
                color: activeFilter === f ? '#ffffff' : '#38bdf8',
                borderColor: activeFilter === f ? '#38bdf8' : '#e2e8f0'
              }}
              onClick={() => setActiveFilter(f)}
            >
              {f}
            </button>
          ))}
        </div>
      </div>

      {/* Location UI Card */}
      <div style={styles.locationCard}>
        <div style={styles.locationHeader}>
          <MapPin size={20} color="#38bdf8" />
          <h3 style={styles.locationTitle}>
            {locationState === 'normal' && "📍 Find Nearby Doctors"}
            {locationState === 'loading' && "📍 Getting your location..."}
            {locationState === 'enabled' && "✓ Location enabled"}
            {locationState === 'permission_denied' && "📍 Location Permission Required"}
            {locationState === 'gps_off' && "📍 Location is turned off"}
            {locationState === 'no_results' && "No nearby doctors found."}
            {locationState === 'unable_to_connect' && "⚠ Unable to connect to SymptoCare server."}
          </h3>
        </div>
        <p style={styles.locationDesc}>
          {locationState === 'normal' && "Find doctors near your current location."}
          {locationState === 'loading' && "🔎 Finding nearby doctors... Please wait."}
          {locationState === 'enabled' && "Showing doctors near you."}
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
            {loading ? 'Searching doctors...' : `${doctors.length} doctors found`}
          </span>
        </div>

        {loading && doctors.length === 0 ? (
          <div style={{display: 'flex', justifyContent: 'center', padding: '40px'}}>
            <Loader className="spinner" size={32} color="#38bdf8" />
          </div>
        ) : error && doctors.length === 0 ? (
          <div style={{color: '#ef4444', textAlign: 'center', padding: '20px'}}>{error}</div>
        ) : (
          <div style={styles.list}>
            {doctors.map(doc => (
              <div key={doc.id} style={styles.docCard}>
                <div style={styles.docHeader}>
                  <div style={styles.avatar}>{doc.name.charAt(4) || 'D'}</div>
                  <div style={styles.docInfo}>
                    <h3 style={styles.docName}>{doc.name}</h3>
                    <p style={styles.docSpec}>{doc.specialist || doc.specialization}</p>
                    <p style={styles.docHospital}>{doc.hospital}</p>
                    {doc.address && <p style={styles.docAddress}>📍 {doc.address}</p>}
                    {doc._dist_km !== undefined && (
                      <span style={styles.distanceBadge}>{doc._dist_km.toFixed(1)} km away</span>
                    )}
                    <div style={styles.ratingRow}>
                      <span style={styles.rating}>⭐ {doc.rating} ({doc.reviews_count || doc.review_count || 120})</span>
                    </div>
                  </div>
                  <div style={{display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: 8}}>
                    {doc.available_today && <span style={{...styles.badge, position: 'relative', top: 0, right: 0}}>Available Today</span>}
                    <button 
                      style={{background: 'none', border: 'none', cursor: 'pointer', padding: 4}}
                      onClick={() => {
                        const saved = JSON.parse(localStorage.getItem('saved_doctors') || '[]');
                        const isSaved = saved.some(d => d.id === doc.id);
                        if (isSaved) {
                          localStorage.setItem('saved_doctors', JSON.stringify(saved.filter(d => d.id !== doc.id)));
                        } else {
                          localStorage.setItem('saved_doctors', JSON.stringify([...saved, doc]));
                        }
                        // Force re-render to update heart color (simplified for this mock)
                        setDoctors([...doctors]); 
                      }}
                    >
                      <Heart 
                        size={20} 
                        fill={JSON.parse(localStorage.getItem('saved_doctors') || '[]').some(d => d.id === doc.id) ? '#e11d48' : 'none'} 
                        color={JSON.parse(localStorage.getItem('saved_doctors') || '[]').some(d => d.id === doc.id) ? '#e11d48' : '#94a3b8'} 
                      />
                    </button>
                  </div>
                </div>
                
                <div style={styles.statsRow}>
                  <div style={styles.statCol}>
                    <span style={styles.statLabel}>Experience</span>
                    <span style={styles.statValue}>{doc.experience_years} Years</span>
                  </div>
                  <div style={styles.statCol}>
                    <span style={styles.statLabel}>Consultation Fee</span>
                    <span style={styles.statValue}>Rs.{doc.consultation_fee}</span>
                  </div>
                </div>

                <div style={styles.actionRow}>
                  <button className="btn-primary" style={styles.bookBtn} onClick={() => handleBook(doc)}>
                    Book
                  </button>
                  <button 
                    style={styles.navBtn} 
                    onClick={() => {
                      const url = `https://www.google.com/maps/dir/?api=1&destination=${doc.lat},${doc.lng}`;
                      window.open(url, '_blank');
                    }}
                    title="Get Directions"
                  >
                    <Navigation size={20} color="#38bdf8" />
                  </button>
                </div>
              </div>
            ))}
            {hasMore && !loading && (
              <div ref={observerTarget} style={{height: '20px', margin: '20px 0'}}></div>
            )}
            {hasMore && loading && doctors.length > 0 && (
              <div style={{display: 'flex', justifyContent: 'center', padding: '20px'}}>
                <Loader className="spinner" size={24} color="#38bdf8" />
              </div>
            )}
          </div>
        )}
      </div>

      {/* Booking Modal */}
      {showBooking && selectedDoctor && (
        <div style={styles.modalOverlay}>
          <div style={styles.modalContent}>
            <div style={styles.modalHeader}>
              <h3 style={styles.modalTitle}>Book Appointment</h3>
              <button style={styles.closeBtn} onClick={() => setShowBooking(false)}>&times;</button>
            </div>
            
            <div style={styles.selectedDocInfo}>
              <h4 style={{fontSize: '16px', color: '#0f172a'}}>{selectedDoctor.name}</h4>
              <p style={{fontSize: '14px', color: '#64748b'}}>{selectedDoctor.specialization}</p>
            </div>

            <div style={styles.bookingForm}>
              <div className="input-group">
                <label className="input-label">Select Date</label>
                <div className="input-field">
                  <CalendarIcon className="input-icon" />
                  <input type="date" />
                </div>
              </div>
              <div className="input-group">
                <label className="input-label">Select Time</label>
                <div className="input-field">
                  <Clock className="input-icon" />
                  <input type="time" />
                </div>
              </div>
            </div>

            <button className="btn-primary" style={{width: '100%', padding: '16px'}} onClick={() => {
              // Save to localStorage
              const appointments = JSON.parse(localStorage.getItem('appointments') || '[]');
              appointments.push({ 
                id: Date.now(),
                doctorName: selectedDoctor.name,
                specialty: selectedDoctor.specialization,
                date: new Date().toISOString() 
              });
              localStorage.setItem('appointments', JSON.stringify(appointments));

              const activities = JSON.parse(localStorage.getItem('recent_activity') || '[]');
              activities.unshift({
                id: Date.now(),
                title: `Appointment Booked with ${selectedDoctor.name}`,
                date: new Date().toISOString(),
                type: 'appointment'
              });
              localStorage.setItem('recent_activity', JSON.stringify(activities.slice(0, 10))); // Keep last 10

              alert('Appointment Booked successfully!');
              setShowBooking(false);
            }}>
              Confirm Booking
            </button>
          </div>
        </div>
      )}
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
    backgroundColor: '#38bdf8',
  },
  filtersWrapper: {
    backgroundColor: '#f8fafc',
    padding: '16px 20px',
    borderBottom: '1px solid #e2e8f0',
  },
  filtersScroll: {
    display: 'flex',
    gap: '8px',
    overflowX: 'auto',
    paddingBottom: '4px',
    scrollbarWidth: 'none',
  },
  filterChip: {
    padding: '8px 16px',
    borderRadius: '20px',
    border: '1px solid',
    fontSize: '13px',
    fontWeight: '600',
    whiteSpace: 'nowrap',
    cursor: 'pointer',
    transition: 'all 0.2s',
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
  docCard: {
    backgroundColor: '#ffffff',
    borderRadius: '16px',
    padding: '16px',
    border: '1px solid #e2e8f0',
    boxShadow: '0 4px 6px rgba(0,0,0,0.02)',
  },
  docHeader: {
    display: 'flex',
    gap: '16px',
    alignItems: 'flex-start',
    marginBottom: '16px',
    position: 'relative',
  },
  avatar: {
    width: '60px',
    height: '60px',
    borderRadius: '16px',
    backgroundColor: '#e0f2fe',
    color: '#0284c7',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '24px',
    fontWeight: '700',
  },
  docInfo: {
    flex: 1,
  },
  docName: {
    fontSize: '16px',
    fontWeight: '700',
    color: '#0f172a',
    marginBottom: '2px',
  },
  docSpec: {
    fontSize: '14px',
    color: '#64748b',
    marginBottom: '4px',
  },
  ratingRow: {
    display: 'flex',
    alignItems: 'center',
    gap: '4px',
  },
  rating: {
    fontSize: '13px',
    color: '#475569',
    fontWeight: '500',
  },
  badge: {
    position: 'absolute',
    top: 0,
    right: 0,
    backgroundColor: '#dcfce7',
    color: '#166534',
    padding: '4px 8px',
    borderRadius: '8px',
    fontSize: '11px',
    fontWeight: '600',
  },
  statsRow: {
    display: 'flex',
    justifyContent: 'space-between',
    padding: '12px 0',
    borderTop: '1px solid #f1f5f9',
    borderBottom: '1px solid #f1f5f9',
    marginBottom: '16px',
  },
  statCol: {
    display: 'flex',
    flexDirection: 'column',
    gap: '4px',
  },
  statLabel: {
    fontSize: '12px',
    color: '#64748b',
  },
  statValue: {
    fontSize: '14px',
    fontWeight: '600',
    color: '#0f172a',
  },
  actionRow: {
    display: 'flex',
    gap: '12px',
  },
  bookBtn: {
    flex: 1,
    padding: '12px',
  },
  navBtn: {
    width: '48px',
    height: '48px',
    borderRadius: '12px',
    border: '1px solid #38bdf8',
    backgroundColor: '#f0f9ff',
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
    alignItems: 'center',
    justifyContent: 'center',
    padding: '20px',
  },
  modalContent: {
    backgroundColor: '#ffffff',
    width: '100%',
    borderRadius: '24px',
    padding: '24px',
  },
  modalHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '16px',
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
    lineHeight: 1,
  },
  selectedDocInfo: {
    backgroundColor: '#f8fafc',
    padding: '12px',
    borderRadius: '12px',
    marginBottom: '20px',
    border: '1px solid #e2e8f0',
  },
  bookingForm: {
    marginBottom: '24px',
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
    backgroundColor: '#f0f9ff',
    border: '1px solid #38bdf8',
    color: '#0284c7',
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
  docHospital: {
    fontSize: '13px',
    fontWeight: '500',
    color: '#475569',
    marginTop: '2px',
  },
  docAddress: {
    fontSize: '12px',
    color: '#64748b',
    marginTop: '2px',
  },
  distanceBadge: {
    display: 'inline-block',
    backgroundColor: '#e0f2fe',
    color: '#0369a1',
    fontSize: '11px',
    fontWeight: '600',
    padding: '2px 8px',
    borderRadius: '6px',
    marginTop: '4px',
  }
};

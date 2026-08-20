import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { MessageSquare, BrainCircuit, MapPin } from 'lucide-react';

const slides = [
  {
    id: 1,
    icon: <MessageSquare size={56} color="white" />,
    title: "Describe Your\nSymptoms",
    description: "Easily describe symptoms using text or\nicons. Simple and stress-free.",
    bgColor: "#38bdf8",
  },
  {
    id: 2,
    icon: <BrainCircuit size={56} color="white" />,
    title: "Smart Specialist\nRecommendation",
    description: "AI-powered healthcare logic\nrecommends the right specialist for you.",
    bgColor: "#4ade80",
  },
  {
    id: 3,
    icon: <MapPin size={56} color="white" />,
    title: "Nearby Doctors &\nHospitals",
    description: "Discover nearby hospitals and qualified\ndoctors instantly.",
    bgColor: "#a78bfa",
  }
];

export default function Onboarding() {
  const [currentSlide, setCurrentSlide] = useState(0);
  const navigate = useNavigate();

  const handleNext = () => {
    if (currentSlide < slides.length - 1) {
      setCurrentSlide(prev => prev + 1);
    } else {
      navigate('/signup');
    }
  };

  const handleSkip = () => {
    navigate('/signup');
  };

  const slide = slides[currentSlide];

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <button onClick={handleSkip} style={styles.skipBtn}>Skip</button>
      </div>
      
      <div style={styles.content}>
        <div style={{...styles.iconWrapper, backgroundColor: slide.bgColor}}>
          {slide.icon}
        </div>
        
        <h1 style={styles.title}>{slide.title}</h1>
        <p style={styles.description}>{slide.description}</p>
      </div>

      <div style={styles.footer}>
        <div style={styles.dots}>
          {slides.map((_, idx) => (
            <div 
              key={idx} 
              style={{
                ...styles.dot, 
                backgroundColor: currentSlide === idx ? '#38bdf8' : '#e2e8f0',
                width: currentSlide === idx ? '24px' : '8px'
              }} 
            />
          ))}
        </div>
        
        <button className="btn-primary" onClick={handleNext}>
          {currentSlide === slides.length - 1 ? 'Get Started' : 'Next'} 
          <span style={{marginLeft: 4}}>&rsaquo;</span>
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    padding: '24px',
    height: '100%',
  },
  header: {
    display: 'flex',
    justifyContent: 'flex-end',
    paddingTop: '16px',
  },
  skipBtn: {
    background: 'none',
    border: 'none',
    color: '#64748b',
    fontWeight: '600',
    fontSize: '16px',
    cursor: 'pointer',
  },
  content: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    textAlign: 'center',
  },
  iconWrapper: {
    width: '120px',
    height: '120px',
    borderRadius: '32px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: '40px',
    boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.1)',
  },
  title: {
    fontSize: '28px',
    color: '#0f172a',
    marginBottom: '16px',
    whiteSpace: 'pre-line',
    lineHeight: 1.2,
  },
  description: {
    fontSize: '16px',
    color: '#64748b',
    whiteSpace: 'pre-line',
  },
  footer: {
    paddingBottom: '32px',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: '32px',
  },
  dots: {
    display: 'flex',
    gap: '8px',
    justifyContent: 'center',
  },
  dot: {
    height: '8px',
    borderRadius: '4px',
    transition: 'all 0.3s ease',
  }
};

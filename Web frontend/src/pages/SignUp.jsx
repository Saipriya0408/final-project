import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Heart, User, Phone, Mail, Lock, MapPin } from 'lucide-react';

const styles = {
  container: {
    minHeight: '100vh',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    background: 'linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%)',
    padding: '24px',
  },
  card: {
    backgroundColor: '#ffffff',
    borderRadius: '24px',
    padding: '40px',
    width: '100%',
    maxWidth: '480px',
    boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.02)',
    display: 'flex',
    flexDirection: 'column',
  },
  header: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    marginBottom: '32px',
  },
  iconWrapper: {
    width: '64px',
    height: '64px',
    borderRadius: '32px',
    backgroundColor: '#38bdf8',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: '16px',
    boxShadow: '0 10px 15px -3px rgba(56, 189, 248, 0.4)',
  },
  title: {
    fontSize: '26px',
    fontWeight: '700',
    color: '#0f172a',
    marginBottom: '8px',
  },
  subtitle: {
    fontSize: '15px',
    color: '#64748b',
    textAlign: 'center',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
  },
  locationBox: {
    backgroundColor: '#f8fafc',
    borderRadius: '12px',
    padding: '16px',
    display: 'flex',
    alignItems: 'center',
    gap: '12px',
    marginTop: '8px',
    border: '1px solid #e2e8f0',
  },
  locationText: {
    fontSize: '13px',
    color: '#475569',
    lineHeight: 1.5,
  },
  footer: {
    marginTop: '32px',
    textAlign: 'center',
  },
  footerText: {
    fontSize: '15px',
    color: '#64748b',
  },
  link: {
    color: '#38bdf8',
    fontWeight: '600',
    textDecoration: 'none',
  }
};

export default function SignUp() {
  const navigate = useNavigate();

  const handleSignUp = async (e) => {
    e.preventDefault();
    const name = e.target[0].value;
    const phone = e.target[1].value;
    const email = e.target[2].value;
    const password = e.target[3].value;
    const confirmPassword = e.target[4].value;
    
    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }
    
    try {
      const response = await fetch('http://10.250.236.211:5000/api/auth/signup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, phone, email, password })
      });
      
      const data = await response.json();
      
      if (data.success) {
        localStorage.setItem('user', JSON.stringify(data.data.user));
        localStorage.setItem('token', data.data.token);
        navigate('/home');
      } else {
        alert(data.error?.message || "Signup failed");
      }
    } catch (err) {
      alert("Could not connect to the server.");
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <div style={styles.header}>
          <div style={styles.iconWrapper}>
            <Heart size={32} color="white" fill="white" />
          </div>
          <h1 style={styles.title}>Create Account</h1>
          <p style={styles.subtitle}>Join SymptoCare for smarter healthcare</p>
        </div>

        <form onSubmit={handleSignUp} style={styles.form}>
          <div className="input-group">
            <label className="input-label">Full Name</label>
            <div className="input-field">
              <User className="input-icon" />
              <input type="text" placeholder="Enter your full name" required />
            </div>
          </div>

          <div className="input-group">
            <label className="input-label">Phone Number</label>
            <div className="input-field">
              <Phone className="input-icon" />
              <input type="tel" placeholder="Enter your phone number" required />
            </div>
          </div>

          <div className="input-group">
            <label className="input-label">Email</label>
            <div className="input-field">
              <Mail className="input-icon" />
              <input type="email" placeholder="Enter your email" required />
            </div>
          </div>

          <div className="input-group">
            <label className="input-label">Password</label>
            <div className="input-field">
              <Lock className="input-icon" />
              <input type="password" placeholder="Create a password" required />
            </div>
          </div>

          <div className="input-group">
            <label className="input-label">Confirm Password</label>
            <div className="input-field">
              <Lock className="input-icon" />
              <input type="password" placeholder="Confirm your password" required />
            </div>
          </div>

          <div style={styles.locationBox}>
            <MapPin size={24} color="#38bdf8" style={{flexShrink: 0}} />
            <p style={styles.locationText}>We'll need location access to show nearby doctors and hospitals accurately.</p>
          </div>

          <button type="submit" className="btn-primary" style={{marginTop: '24px', padding: '16px', fontSize: '16px'}}>
            Create Account
          </button>
        </form>

        <div style={styles.footer}>
          <p style={styles.footerText}>
            Already have an account? <Link to="/signin" style={styles.link}>Sign in</Link>
          </p>
        </div>
      </div>
    </div>
  );
}

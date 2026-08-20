import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Heart, Mail, Lock } from 'lucide-react';

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
    maxWidth: '440px',
    boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.02)',
    display: 'flex',
    flexDirection: 'column',
  },
  header: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    marginBottom: '40px',
  },
  iconWrapper: {
    width: '64px',
    height: '64px',
    borderRadius: '32px',
    backgroundColor: '#38bdf8',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: '20px',
    boxShadow: '0 10px 15px -3px rgba(56, 189, 248, 0.4)',
  },
  title: {
    fontSize: '28px',
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
  forgotPassword: {
    display: 'flex',
    justifyContent: 'flex-end',
    marginBottom: '24px',
  },
  forgotBtn: {
    background: 'none',
    border: 'none',
    color: '#38bdf8',
    fontWeight: '600',
    fontSize: '14px',
    cursor: 'pointer',
  },
  dividerContainer: {
    display: 'flex',
    alignItems: 'center',
    margin: '32px 0',
  },
  dividerLine: {
    flex: 1,
    height: '1px',
    backgroundColor: '#e2e8f0',
  },
  dividerText: {
    padding: '0 16px',
    color: '#94a3b8',
    fontSize: '14px',
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

export default function SignIn() {
  const navigate = useNavigate();

  const handleSignIn = async (e) => {
    e.preventDefault();
    const email_or_phone = e.target[0].value;
    const password = e.target[1].value;
    
    try {
      const response = await fetch('http://10.250.236.211:5000/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email_or_phone, password })
      });
      
      const data = await response.json();
      
      if (data.success) {
        localStorage.setItem('user', JSON.stringify(data.data.user));
        localStorage.setItem('token', data.data.token);
        navigate('/home');
      } else {
        alert(data.error?.message || "Login failed");
      }
    } catch (err) {
      alert("Could not connect to the server.");
    }
  };

  const handleGuestLogin = () => {
    navigate('/home');
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <div style={styles.header}>
          <div style={styles.iconWrapper}>
            <Heart size={32} color="white" fill="white" />
          </div>
          <h1 style={styles.title}>Welcome Back</h1>
          <p style={styles.subtitle}>Sign in to continue your healthcare journey</p>
        </div>

        <form onSubmit={handleSignIn} style={styles.form}>
          <div className="input-group">
            <label className="input-label">Email or Phone</label>
            <div className="input-field">
              <Mail className="input-icon" />
              <input type="text" placeholder="Enter your email or phone" required />
            </div>
          </div>

          <div className="input-group" style={{marginBottom: '8px'}}>
            <label className="input-label">Password</label>
            <div className="input-field">
              <Lock className="input-icon" />
              <input type="password" placeholder="Enter your password" required />
            </div>
          </div>

          <div style={styles.forgotPassword}>
            <button type="button" style={styles.forgotBtn}>Forgot Password?</button>
          </div>

          <button type="submit" className="btn-primary" style={{padding: '16px', fontSize: '16px'}}>
            Login
          </button>
        </form>

        <div style={styles.dividerContainer}>
          <div style={styles.dividerLine} />
          <span style={styles.dividerText}>or</span>
          <div style={styles.dividerLine} />
        </div>

        <button type="button" className="btn-outline" onClick={handleGuestLogin} style={{padding: '16px', fontSize: '16px'}}>
          Continue as Guest
        </button>

        <div style={styles.footer}>
          <p style={styles.footerText}>
            Don't have an account? <Link to="/signup" style={styles.link}>Sign Up</Link>
          </p>
        </div>
      </div>
    </div>
  );
}

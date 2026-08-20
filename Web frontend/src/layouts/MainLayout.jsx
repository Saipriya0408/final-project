import React from 'react';
import { NavLink, Outlet } from 'react-router-dom';
import { Home, Stethoscope, Users, Building2, User, Heart } from 'lucide-react';

export default function MainLayout() {
  return (
    <div style={styles.container}>
      {/* Top Navigation for Desktop Website */}
      <nav style={styles.topNav}>
        <div style={styles.navContainer}>
          <div style={styles.logo}>
            <Heart size={28} color="white" fill="#38bdf8" stroke="none" />
            <span style={styles.logoText}>SymptoCare</span>
          </div>
          
          <div style={styles.navLinks}>
            <NavItem to="/home" icon={<Home size={20} />} label="Home" />
            <NavItem to="/symptoms" icon={<Stethoscope size={20} />} label="Symptoms" />
            <NavItem to="/doctors" icon={<Users size={20} />} label="Doctors" />
            <NavItem to="/hospitals" icon={<Building2 size={20} />} label="Hospitals" />
          </div>

          <div style={styles.profileSection}>
             <NavLink to="/profile" style={styles.profileBtn}>
                <User size={20} />
                <span>Profile</span>
             </NavLink>
          </div>
        </div>
      </nav>

      <div style={styles.content}>
        <div style={styles.pageWrapper}>
          <Outlet />
        </div>
      </div>
    </div>
  );
}

function NavItem({ to, icon, label }) {
  return (
    <NavLink 
      to={to} 
      style={({ isActive }) => ({
        ...styles.navItem,
        color: isActive ? '#38bdf8' : '#475569',
        borderBottom: isActive ? '3px solid #38bdf8' : '3px solid transparent'
      })}
    >
      {icon}
      <span style={styles.navLabel}>{label}</span>
    </NavLink>
  );
}

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    minHeight: '100vh',
    backgroundColor: '#f8fafc',
  },
  topNav: {
    backgroundColor: '#ffffff',
    boxShadow: '0 2px 10px rgba(0, 0, 0, 0.05)',
    position: 'sticky',
    top: 0,
    zIndex: 100,
  },
  navContainer: {
    maxWidth: '1200px',
    margin: '0 auto',
    padding: '0 24px',
    height: '70px',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  logo: {
    display: 'flex',
    alignItems: 'center',
    gap: '10px',
  },
  logoText: {
    fontSize: '22px',
    fontWeight: '700',
    color: '#0f172a',
  },
  navLinks: {
    display: 'flex',
    height: '100%',
    gap: '32px',
  },
  navItem: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    textDecoration: 'none',
    fontWeight: '600',
    fontSize: '15px',
    padding: '0 8px',
    transition: 'all 0.2s',
  },
  profileSection: {
    display: 'flex',
    alignItems: 'center',
  },
  profileBtn: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    backgroundColor: '#f0f9ff',
    color: '#0284c7',
    padding: '8px 16px',
    borderRadius: '20px',
    textDecoration: 'none',
    fontWeight: '600',
    fontSize: '14px',
  },
  content: {
    flex: 1,
    display: 'flex',
    justifyContent: 'center',
    padding: '32px 24px',
  },
  pageWrapper: {
    width: '100%',
    maxWidth: '1200px',
  }
};

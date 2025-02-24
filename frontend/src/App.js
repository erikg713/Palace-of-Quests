import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Header from './components/Shared/Header';
import Navbar from './components/Navbar';
import Notifications from './components/Shared/Notifications';
import Login from './components/Authentication/Login';
import QuestList from './components/Quests/QuestList';
import CompletedQuests from './components/Quests/CompletedQuests';
import Marketplace from './components/Marketplace/Marketplace';
import AddItem from './components/Marketplace/AddItem';
import AdminPanel from './components/Admin/AdminPanel';
import UserDashboard from './components/Shared/UserDashboard';
import HomePage from './pages/HomePage';
import AboutPage from './pages/AboutPage';
import Payment from './components/Payment';
import { UserProvider } from './context/UserContext';
import './App.css'; // Custom CSS for overrides

function App() {
  const [userId, setUserId] = useState(null);
  const [notifications, setNotifications] = useState([]);

  const addNotification = (message) => {
    setNotifications((prev) => [...prev, message]);
    setTimeout(() => {
      setNotifications((prev) => prev.slice(1));
    }, 5000); // Remove notification after 5 seconds
  };

  return (
    <UserProvider>
      <Router>
        <Header />
        <Navbar />
        <Notifications messages={notifications} />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route 
            path="/login" 
            element={!userId ? <Login setUser={setUserId} /> : <Navigate to="/dashboard" />}
          />
          <Route 
            path="/quests" 
            element={userId ? <QuestList userId={userId} /> : <Navigate to="/login" />}
          />
          <Route 
            path="/completed-quests" 
            element={userId ? <CompletedQuests userId={userId} /> : <Navigate to="/login" />}
          />
          <Route 
            path="/marketplace" 
            element={userId ? <Marketplace userId={userId} /> : <Navigate to="/login" />}
          />
          <Route 
            path="/marketplace/add" 
            element={userId ? <AddItem /> : <Navigate to="/login" />}
          />
          <Route 
            path="/admin" 
            element={userId ? <AdminPanel /> : <Navigate to="/login" />}
          />
          <Route 
            path="/dashboard" 
            element={userId ? <UserDashboard userId={userId} /> : <Navigate to="/login" />}
          />
          <Route path="/payment" element={<Payment />} />
        </Routes>
      </Router>
    </UserProvider>
  );
}

export default App;

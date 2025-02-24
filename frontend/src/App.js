import React, { useContext, useState } from 'react';
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
import UserContext from './context/UserContext';
import './App.css';

function App() {
  const { user } = useContext(UserContext);
  const [notifications, setNotifications] = useState([]);

  const addNotification = (message) => {
    setNotifications((prev) => [...prev, message]);
    setTimeout(() => {
      setNotifications((prev) => prev.slice(1));
    }, 5000);
  };

  return (
    <Router>
      <Header />
      <Navbar />
      <Notifications messages={notifications} />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route
          path="/login"
          element={!user ? <Login /> : <Navigate to="/dashboard" />}
        />
        <Route
          path="/quests"
          element={
            user ? <QuestList userId={user.id} /> : <Navigate to="/login" />
          }
        />
        {/* ...other routes */}
      </Routes>
    </Router>
  );
}
import React, { useState } from 'react';
import PiAuth from './components/Authentication/PiAuth';
import Marketplace from './components/Marketplace/Marketplace';

function App() {
  const [authData, setAuthData] = useState(null);

  const handleAuthenticated = (auth) => {
    setAuthData(auth);
  };

  return (
    <div>
      {!authData ? (
        <PiAuth onAuthenticated={handleAuthenticated} />
      ) : (
        <>
          <h1>Welcome, {authData.user.username}!</h1>
          <Marketplace />
        </>
      )}
    </div>
  );
}

export default App;

export default App;

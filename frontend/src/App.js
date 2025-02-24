import React, { useContext } from 'react';
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
            element={!user ? <Login /> : <Navigate to="/dashboard" />}
          />
          <Route
            path="/quests"
            element={user ? <QuestList userId={user.id} /> : <Navigate to="/login" />}
          />
          {/* ...other routes */}
        </Routes>
      </Router>
    </UserProvider>
  );
}

export default App;
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import QuestPage from './pages/QuestPage';
import LoginPage from './pages/LoginPage';
import Navbar from './components/Navbar';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/quest" element={<QuestPage />} />
        <Route path="/login" element={<LoginPage />} />
      </Routes>
    </Router>
  );
}

export default App;
import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Login from './components/Login';
import QuestList from './components/QuestList';
import Marketplace from './components/Marketplace';
import UserDashboard from './components/UserDashboard';

function App() {
  const [userId, setUserId] = useState(null);

  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Login setUser={setUserId} />} />
        <Route path="/quests" element={<QuestList userId={userId} />} />
        <Route path="/marketplace" element={<Marketplace userId={userId} />} />
        <Route path="/dashboard" element={<UserDashboard userId={userId} />} />
      </Routes>
    </Router>
  );
}

export default App;
import ProtectedRoute from './ProtectedRoute';

// ...

<Routes>
  {/* Public routes */}
  <Route path="/" element={<HomePage />} />
  <Route path="/about" element={<AboutPage />} />
  <Route
    path="/login"
    element={!user ? <Login /> : <Navigate to="/dashboard" />}
  />

  {/* Protected routes */}
  <Route
    path="/quests"
    element={<ProtectedRoute element={QuestList} />}
  />
  <Route
    path="/admin"
    element={<ProtectedRoute element={AdminPanel} roles={['admin']} />}
  />
  {/* ...other routes */}
</Routes>

import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Header from './components/Shared/Header';
import Notifications from './components/Shared/Notifications';
import Login from './components/Authentication/Login';
import QuestList from './components/Quests/QuestList';
import CompletedQuests from './components/Quests/CompletedQuests';
import Marketplace from './components/Marketplace/Marketplace';
import AddItem from './components/Marketplace/AddItem';
import AdminPanel from './components/Admin/AdminPanel';
import UserDashboard from './components/Shared/UserDashboard';
import { UserProvider } from './context/UserContext';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginForm from './components/LoginForm';

const App = () => (
  <Router>
    <Routes>
      <Route path="/login" element={<LoginForm />} />
      {/* Add other routes here */}
    </Routes>
  </Router>
);

export default App;

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
        <Notifications messages={notifications} />
        <Routes>
          <Route
            path="/"
            element={!userId ? <Login setUser={setUserId} /> : <Navigate to="/dashboard" />}
          />
          <Route
            path="/quests"
            element={userId ? <QuestList userId={userId} /> : <Navigate to="/" />}
          />
          <Route
            path="/completed-quests"
            element={userId ? <CompletedQuests userId={userId} /> : <Navigate to="/" />}
          />
          <Route
            path="/marketplace"
            element={userId ? <Marketplace userId={userId} /> : <Navigate to="/" />}
          />
          <Route
            path="/marketplace/add"
            element={userId ? <AddItem /> : <Navigate to="/" />}
          />
          <Route
            path="/admin"
            element={userId ? <AdminPanel /> : <Navigate to="/" />}
          />
          <Route
            path="/dashboard"
            element={userId ? <UserDashboard userId={userId} /> : <Navigate to="/" />}
          />
        </Routes>
      </Router>
    </UserProvider>
  );
}

export default App;

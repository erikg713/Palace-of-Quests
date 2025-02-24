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
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import AboutPage from "./pages/AboutPage";
import "./App.css"; // Custom CSS for overrides
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
const App = () => {
  return (
    <Router>
      <div className="container">
        <header className="text-center my-4">
          <h1>Palace of Quests</h1>
        </header>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/about" element={<AboutPage />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;

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

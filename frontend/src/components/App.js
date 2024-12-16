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

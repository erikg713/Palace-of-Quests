import React, { useContext, useReducer, useCallback } from 'react';
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

const notificationReducer = (state, action) => {
  switch (action.type) {
    case 'ADD':
      return [...state, action.payload];
    case 'REMOVE':
      return state.slice(1);
    default:
      return state;
  }
};

const ProtectedRoute = ({ user, children, redirectTo = "/login" }) => (
  user ? children : <Navigate to={redirectTo} replace />
);

function App() {
  const { user } = useContext(UserContext);
  const [notifications, dispatch] = useReducer(notificationReducer, []);

  const addNotification = useCallback((message) => {
    dispatch({ type: 'ADD', payload: message });
    setTimeout(() => dispatch({ type: 'REMOVE' }), 5000);
  }, []);

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
          element={
            !user ? <Login addNotification={addNotification} /> : <Navigate to="/dashboard" replace />
          }
        />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute user={user}>
              <UserDashboard user={user} />
            </ProtectedRoute>
          }
        />
        <Route
          path="/quests"
          element={
            <ProtectedRoute user={user}>
              <QuestList userId={user?.id} addNotification={addNotification} />
            </ProtectedRoute>
          }
        />
        <Route
          path="/quests/completed"
          element={
            <ProtectedRoute user={user}>
              <CompletedQuests userId={user?.id} />
            </ProtectedRoute>
          }
        />
        <Route
          path="/marketplace"
          element={
            <ProtectedRoute user={user}>
              <Marketplace user={user} addNotification={addNotification} />
            </ProtectedRoute>
          }
        />
        <Route
          path="/marketplace/add"
          element={
            <ProtectedRoute user={user}>
              <AddItem addNotification={addNotification} />
            </ProtectedRoute>
          }
        />
        <Route
          path="/admin"
          element={
            <ProtectedRoute user={user && user.isAdmin} redirectTo="/">
              <AdminPanel />
            </ProtectedRoute>
          }
        />
        <Route
          path="/payment"
          element={
            <ProtectedRoute user={user}>
              <Payment />
            </ProtectedRoute>
          }
        />
        {/* Add additional routes here */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
}

export default App;

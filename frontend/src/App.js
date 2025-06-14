import React, { useContext, useReducer, useCallback, Suspense, lazy } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';

import UserContext from './context/UserContext';
import './App.css';

// Lazy loaded components for better performance
const Header = lazy(() => import('./components/Shared/Header'));
const Navbar = lazy(() => import('./components/Navbar'));
const Notifications = lazy(() => import('./components/Shared/Notifications'));
const Login = lazy(() => import('./components/Authentication/Login'));
const QuestList = lazy(() => import('./components/Quests/QuestList'));
const CompletedQuests = lazy(() => import('./components/Quests/CompletedQuests'));
const Marketplace = lazy(() => import('./components/Marketplace/Marketplace'));
const AddItem = lazy(() => import('./components/Marketplace/AddItem'));
const AdminPanel = lazy(() => import('./components/Admin/AdminPanel'));
const UserDashboard = lazy(() => import('./components/Shared/UserDashboard'));
const HomePage = lazy(() => import('./pages/HomePage'));
const AboutPage = lazy(() => import('./pages/AboutPage'));
const Payment = lazy(() => import('./components/Payment'));

// Notification reducer for managing notification queue
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

// ProtectedRoute for authenticated and authorized routes
const ProtectedRoute = ({ user, children, redirectTo = "/login" }) => {
  return user ? children : <Navigate to={redirectTo} replace />;
};

function App() {
  const { user } = useContext(UserContext);
  const [notifications, dispatch] = useReducer(notificationReducer, []);

  const addNotification = useCallback((message) => {
    dispatch({ type: 'ADD', payload: message });
    setTimeout(() => dispatch({ type: 'REMOVE' }), 5000);
  }, []);

  return (
    <Router>
      <Suspense fallback={<div className="app-loading">Loading...</div>}>
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
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </Suspense>
    </Router>
  );
}

export default App;

import React from 'react';
import { Routes, Route } from 'react-router-dom';
import PrivateRoute from './PrivateRoute';
import useAnalytics from './middleware/useAnalytics';
import ErrorBoundary from './middleware/ErrorBoundary';
import Login from './components/Authentication/Login';
import QuestList from './components/Quests/QuestList';
import CompletedQuests from './components/Quests/CompletedQuests';
import Marketplace from './components/Marketplace/Marketplace';
import AddItem from './components/Marketplace/AddItem';
import AdminPanel from './components/Admin/AdminPanel';
import UserDashboard from './components/Shared/UserDashboard';

const RoutesConfig = () => {
  // Tracks route changes
  useAnalytics();

  const QuestList = React.lazy(() => import('./components/Quests/QuestList'));

<Suspense fallback={<div>Loading...</div>}>
  <QuestList />
</Suspense>

  return (
    <ErrorBoundary>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/quests" element={<PrivateRoute element={<QuestList />} />} />
        <Route path="/completed-quests" element={<PrivateRoute element={<CompletedQuests />} />} />
        <Route path="/marketplace" element={<PrivateRoute element={<Marketplace />} />} />
        <Route path="/marketplace/add" element={<PrivateRoute element={<AddItem />} />} />
        <Route path="/admin" element={<PrivateRoute requiredRole="admin" element={<AdminPanel />} />} />
        <Route path="/dashboard" element={<PrivateRoute element={<UserDashboard />} />} />
      </Routes>
    </ErrorBoundary>
  );
};

export default RoutesConfig;

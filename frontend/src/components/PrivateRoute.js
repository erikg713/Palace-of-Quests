// components/PrivateRoute.js
import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const PrivateRoute = ({ element, requiredRole = null, redirectTo = '/' }) => {
  const { user } = useAuth();

  if (!user?.id) return <Navigate to={redirectTo} />;
  if (requiredRole && user.role !== requiredRole) return <Navigate to="/unauthorized" />;

  return element;
};

export default PrivateRoute;

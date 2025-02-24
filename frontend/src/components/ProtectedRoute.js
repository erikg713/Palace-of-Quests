import React, { useContext } from 'react';
import { Navigate } from 'react-router-dom';
import UserContext from './context/UserContext';

const ProtectedRoute = ({ element: Component, roles, ...rest }) => {
  const { user } = useContext(UserContext);

  if (!user) {
    // User is not authenticated
    return <Navigate to="/login" />;
  }

  if (roles && !roles.includes(user.role)) {
    // User does not have the required role
    return <Navigate to="/unauthorized" />;
  }

  return <Component {...rest} />;
};

export default ProtectedRoute;
const ProtectedRoute = ({ children, roles }) => {
  const { user } = useContext(UserContext);

  if (!user) {
    return <Navigate to="/login" />;
  }

  if (roles && !roles.includes(user.role)) {
    return <Navigate to="/unauthorized" />;
  }

  return children;
};

export default ProtectedRoute;

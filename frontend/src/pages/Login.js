import React, { useState, useContext } from 'react';
import UserContext from '../../context/UserContext';

const Login = () => {
  const { login } = useContext(UserContext);
  const [credentials, setCredentials] = useState({ username: '', password: '' });

  const handleSubmit = (e) => {
    e.preventDefault();
    // Perform authentication (API call)
    const userData = {
      id: 1,
      username: credentials.username,
      role: 'user', // or 'admin'
    };
    login(userData);
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Input fields for username and password */}
      <button type="submit">Login</button>
    </form>
  );
};

export default Login;

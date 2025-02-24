import React, { useState, useContext } from 'react';
import UserContext from '../../context/UserContext';

const Login = () => {
  const { login } = useContext(UserContext);
  const [credentials, setCredentials] = useState({ username: '', password: '' });

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Assume authenticate is a function that verifies user credentials
    const userData = await authenticate(credentials);
    if (userData) {
      login(userData);
    } else {
      // Handle login failure
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Input fields for username and password */}
      <button type="submit">Login</button>
    </form>
  );
};

export default Login;

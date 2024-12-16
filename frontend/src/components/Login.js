import React, { useState } from 'react';

function Login({ setUser }) {
  const [walletAddress, setWalletAddress] = useState('');
  const [username, setUsername] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ wallet_address: walletAddress, username }),
    });
    const data = await response.json();
    if (data.user_id) {
      setUser(data.user_id);
      alert('Login successful!');
    } else {
      alert('Login failed');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      <label>
        Wallet Address:
        <input type="text" value={walletAddress} onChange={(e) => setWalletAddress(e.target.value)} required />
      </label>
      <label>
        Username:
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
      </label>
      <button type="submit">Login</button>
    </form>
  );
}

export default Login;

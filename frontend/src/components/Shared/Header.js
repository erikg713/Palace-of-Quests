import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header>
      <h1>Palace of Quests</h1>
      <nav>
        <Link to="/">Login</Link>
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/quests">Quests</Link>
        <Link to="/completed-quests">Completed Quests</Link>
        <Link to="/marketplace">Marketplace</Link>
        <Link to="/marketplace/add">Add Item</Link>
        <Link to="/admin">Admin Panel</Link>
      </nav>
    </header>
  );
}

export default Header;

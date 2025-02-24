import React from 'react';
import ReactDOM from 'react-dom/client'; // Import from 'react-dom/client' for React 18
import App from './App';
import { UserProvider } from './context/UserContext';
import { NotificationProvider } from './context/NotificationContext';

// If you have global styles
import './styles/global.css';

// Create a root using React 18's createRoot
const root = ReactDOM.createRoot(document.getElementById('root'));

// Render your app wrapped with Context Providers
root.render(
  <React.StrictMode>
    <UserProvider>
      <NotificationProvider>
        <App />
      </NotificationProvider>
    </UserProvider>
  </React.StrictMode>
);

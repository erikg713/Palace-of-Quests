import React, { Suspense } from 'react';
import ReactDOM from 'react-dom/client';
import ErrorBoundary from './components/ErrorBoundary';
import { UserProvider } from './context/UserContext';
import { NotificationProvider } from './context/NotificationContext';
import './styles/global.css';

const App = React.lazy(() => import('./App'));

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    <ErrorBoundary>
      <UserProvider>
        <NotificationProvider>
          <Suspense fallback={<div>Loading application...</div>}>
            <App />
          </Suspense>
        </NotificationProvider>
      </UserProvider>
    </ErrorBoundary>
  </React.StrictMode>
);

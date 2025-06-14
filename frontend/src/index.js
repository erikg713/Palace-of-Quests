import React, { Suspense } from 'react';
import ReactDOM from 'react-dom/client';
import ErrorBoundary from './components/ErrorBoundary';
import { UserProvider } from './context/UserContext';
import { NotificationProvider } from './context/NotificationContext';
import './styles/global.css';

const App = React.lazy(() => import('./App'));

// Ensure the root element exists before continuing
const rootElement = document.getElementById('root');
if (!rootElement) {
  throw new Error('Root element not found. Please ensure there is a <div id="root"></div> in your index.html.');
}

const root = ReactDOM.createRoot(rootElement);

// Main render tree with providers and error boundaries for robust UX
root.render(
  <React.StrictMode>
    <ErrorBoundary>
      <UserProvider>
        <NotificationProvider>
          <Suspense fallback={
            <div role="status" aria-live="polite" style={{ textAlign: 'center', marginTop: '2rem' }}>
              Loading application...
            </div>
          }>
            <App />
          </Suspense>
        </NotificationProvider>
      </UserProvider>
    </ErrorBoundary>
  </React.StrictMode>
);

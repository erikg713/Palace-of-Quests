// middleware/useAnalytics.js
import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';

const useAnalytics = () => {
  const location = useLocation();

  useEffect(() => {
    console.log(`Navigated to: ${location.pathname}`);
    // Example: Google Analytics
    // window.gtag('config', 'GA_TRACKING_ID', { page_path: location.pathname });
  }, [location]);

  return (eventName, eventData) => {
    console.log(`Event: ${eventName}`, eventData);
    // Example: window.analytics.track(eventName, eventData);
  };
};

export default useAnalytics;

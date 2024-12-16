import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';

const useAnalytics = () => {
  const location = useLocation();

  useEffect(() => {
    // Log page navigation
    console.log(`Navigated to: ${location.pathname}`);
    
    // Example: Send navigation data to Google Analytics
    // window.gtag('config', 'GA_TRACKING_ID', { page_path: location.pathname });

    // Example: Custom analytics service
    // sendToAnalytics({ event: 'page_view', path: location.pathname });
  }, [location]);
};

export default useAnalytics;

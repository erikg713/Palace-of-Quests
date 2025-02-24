import React, { useEffect } from 'react';

const PiAuth = ({ onAuthenticated }) => {
  useEffect(() => {
    if (!window.Pi) {
      console.error('Pi SDK not loaded.');
      return;
    }

    const scopes = ['payments', 'username'];

    function onIncompletePaymentFound(payment) {
      console.log('Incomplete payment found:', payment);
      // Handle incomplete payments
    }

    window.Pi.authenticate(scopes, onIncompletePaymentFound)
      .then(function(auth) {
        console.log('Authentication successful:', auth);
        if (onAuthenticated) onAuthenticated(auth);
      })
      .catch(function(error) {
        console.error('Authentication error:', error);
      });
  }, [onAuthenticated]);

  return null; // This component doesn't render anything
};

export default PiAuth;

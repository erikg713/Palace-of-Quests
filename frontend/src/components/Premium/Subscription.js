// components/Premium/Subscription.js
import React from 'react';

const Subscription = () => {
  const handleSubscription = () => {
    // Handle Pi Network payment here using Pi Network SDK
    console.log('Processing Pi payment for premium subscription...');
  };

  return (
    <div>
      <h2>Premium Subscription</h2>
      <p>Get all upgrades unlocked for 1 year for $9.99</p>
      <button onClick={handleSubscription}>Subscribe</button>
    </div>
  );
};

export default Subscription;
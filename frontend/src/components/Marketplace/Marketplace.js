import React, { useState, useEffect } from 'react';
import MarketplaceItem from './MarketplaceItem';

const Marketplace = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    // Fetch items from your backend or define them statically
    setItems([
      { id: 1, name: 'Item 1', price: 19.99, image: 'item1.jpg' },
      { id: 2, name: 'Item 2', price: 29.99, image: 'item2.jpg' },
      { id: 3, name: 'Item 3', price: 39.99, image: 'item3.jpg' },
    ]);
  }, []);

  const handleBuy = (item) => {
    if (!window.Pi) {
      console.error('Pi SDK not loaded.');
      return;
    }

    const payment = {
      amount: item.price.toString(),
      memo: `Purchase ${item.name}`,
      metadata: { itemId: item.id },
    };

    window.Pi.createPayment(payment, {
      // Callbacks
      onReadyForServerApproval: (paymentId) => {
        console.log('Ready for server approval:', paymentId);
        // Send paymentId to your server to approve the payment
      },
      onReadyForServerCompletion: (paymentId, txid) => {
        console.log('Ready for server completion:', paymentId, txid);
        // Verify transaction and complete payment on your server
      },
      onCancel: (paymentId) => {
        console.log('Payment cancelled:', paymentId);
      },
      onError: (error, payment) => {
        console.error('Payment error:', error, payment);
      },
    });
  };

  return (
    <div className="container">
      {items.map((item) => (
        <MarketplaceItem key={item.id} item={item} onBuy={handleBuy} />
      ))}
    </div>
  );
};

export default Marketplace;

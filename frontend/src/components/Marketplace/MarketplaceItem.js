import React from 'react';

const MarketplaceItem = ({ item, onBuy }) => {
  return (
    <div className="marketplace-card">
      <img src={item.image} alt={item.name} />
      <h3>{item.name}</h3>
      <p>{item.price} Pi</p>
      <button onClick={() => onBuy(item)}>Buy Now</button>
    </div>
  );
};

export default MarketplaceItem;

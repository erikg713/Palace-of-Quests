import React, { useEffect, useState } from 'react';

function Marketplace({ userId }) {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch('/api/marketplace')
      .then(response => response.json())
      .then(data => setItems(data));
  }, []);

  const buyItem = async (itemId) => {
    await fetch('/api/marketplace/buy', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ buyer_id: userId, item_id: itemId }),
    });
    alert('Item purchased!');
  };

  return (
    <div>
      <h2>Marketplace</h2>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.name} - Price: {item.price}
            <button onClick={() => buyItem(item.id)}>Buy</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Marketplace;

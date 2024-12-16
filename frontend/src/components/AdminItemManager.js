import React, { useState, useEffect } from 'react';

function AdminItemManager() {
  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState({ name: '', price: 0 });

  useEffect(() => {
    fetch('/api/marketplace')
      .then(response => response.json())
      .then(data => setItems(data));
  }, []);

  const handleAddItem = async () => {
    await fetch('/api/marketplace', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newItem),
    });
    alert('Item added!');
    setNewItem({ name: '', price: 0 });
  };

  const handleDeleteItem = async (id) => {
    await fetch(`/api/marketplace/${id}`, { method: 'DELETE' });
    alert('Item deleted!');
    setItems(items.filter(item => item.id !== id));
  };

  return (
    <div>
      <h3>Marketplace Items</h3>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.name} - Price: {item.price}
            <button onClick={() => handleDeleteItem(item.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <div>
        <h4>Add New Item</h4>
        <input
          type="text"
          placeholder="Name"
          value={newItem.name}
          onChange={(e) => setNewItem({ ...newItem, name: e.target.value })}
        />
        <input
          type="number"
          placeholder="Price"
          value={newItem.price}
          onChange={(e) => setNewItem({ ...newItem, price: parseInt(e.target.value) })}
        />
        <button onClick={handleAddItem}>Add Item</button>
      </div>
    </div>
  );
}

export default AdminItemManager;

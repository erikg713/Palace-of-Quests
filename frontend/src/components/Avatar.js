import React, { useState, useEffect } from "react";
import { getInventory, equipItem, sellItem } from "../api/inventoryAPI";

const Inventory = () => {
  const [items, setItems] = useState([]);
  const [currency, setCurrency] = useState(0);

  useEffect(() => {
    const fetchInventory = async () => {
      const data = await getInventory();
      setItems(data.items);
      setCurrency(data.currency);
    };
    fetchInventory();
  }, []);

  const handleEquipItem = async (itemId) => {
    const updatedItems = await equipItem(itemId);
    setItems(updatedItems);
  };

  const handleSellItem = async (itemId) => {
    const result = await sellItem(itemId);
    setItems(result.items);
    setCurrency(result.currency);
  };

  return (
    <div className="container">
      <h2>Your Inventory</h2>
      <p>Currency: {currency}</p>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            <h3>{item.name}</h3>
            <p>{item.description}</p>
            {item.equipped ? (
              <p>Equipped</p>
            ) : (
              <>
                <button onClick={() => handleEquipItem(item.id)}>Equip</button>
                <button onClick={() => handleSellItem(item.id)}>Sell</button>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Inventory;

import React, { useState, useEffect } from "react";
import { getAvatar, customizeAvatar } from "../api/avatarAPI";

const Avatar = () => {
  const [avatar, setAvatar] = useState(null);

  useEffect(() => {
    const fetchAvatar = async () => {
      const data = await getAvatar();
      setAvatar(data);
    };
    fetchAvatar();
  }, []);

  const handleCustomization = async (attribute, value) => {
    const updatedAvatar = await customizeAvatar(attribute, value);
    setAvatar(updatedAvatar);
  };

  return (
    <div className="container">
      <h2>{avatar?.name}'s Avatar</h2>
      <p>Level: {avatar?.level}</p>
      <div>
        <label>
          Outfit:
          <select onChange={(e) => handleCustomization("outfit", e.target.value)}>
            <option value="default">Default</option>
            <option value="warrior">Warrior</option>
            <option value="mage">Mage</option>
          </select>
        </label>
        <label>
          Helmet:
          <select onChange={(e) => handleCustomization("helmet", e.target.value)}>
            <option value="none">None</option>
            <option value="iron_helmet">Iron Helmet</option>
            <option value="golden_helmet">Golden Helmet</option>
          </select>
        </label>
      </div>
    </div>
  );
};

export default Avatar;

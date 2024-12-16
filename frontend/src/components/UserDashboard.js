import React, { useEffect, useState } from 'react';

function UserDashboard({ userId }) {
  const [activeQuests, setActiveQuests] = useState([]);
  const [inventory, setInventory] = useState([]);

  useEffect(() => {
    fetch(`/api/user/${userId}/quests`)
      .then(response => response.json())
      .then(data => setActiveQuests(data));
    fetch(`/api/user/${userId}/inventory`)
      .then(response => response.json())
      .then(data => setInventory(data));
  }, [userId]);

  return (
    <div>
      <h2>Your Dashboard</h2>
      <section>
        <h3>Active Quests</h3>
        <ul>
          {activeQuests.map(quest => (
            <li key={quest.id}>{quest.name} - Reward: {quest.reward}</li>
          ))}
        </ul>
      </section>
      <section>
        <h3>Your Inventory</h3>
        <ul>
          {inventory.map(item => (
            <li key={item.id}>{item.name}</li>
          ))}
        </ul>
      </section>
    </div>
  );
}

export default UserDashboard;

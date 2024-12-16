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
import React, { useEffect, useState } from "react";

function UserDashboard({ userId }) {
  const [activeQuests, setActiveQuests] = useState([]);
  const [inventory, setInventory] = useState([]);
  const [profile, setProfile] = useState({
    username: "Player",
    avatar: "",
    achievements: [],
  });

  // Fetch data
  useEffect(() => {
    const fetchPlayerData = async () => {
      const profileResponse = await fetch(`/api/user/${userId}/profile`);
      const profileData = await profileResponse.json();
      setProfile(profileData);

      const questsResponse = await fetch(`/api/user/${userId}/quests`);
      const questsData = await questsResponse.json();
      setActiveQuests(questsData);

      const inventoryResponse = await fetch(`/api/user/${userId}/inventory`);
      const inventoryData = await inventoryResponse.json();
      setInventory(inventoryData);
    };

    fetchPlayerData();
  }, [userId]);

  // Handle item usage
  const handleUseItem = (itemId) => {
    fetch(`/api/user/${userId}/inventory/use/${itemId}`, { method: "POST" })
      .then(() => setInventory(inventory.filter((item) => item.id !== itemId)));
  };

  // Handle marking quest complete
  const handleMarkComplete = (questId) => {
    fetch(`/api/user/${userId}/quests/complete/${questId}`, { method: "POST" })
      .then(() =>
        setActiveQuests(activeQuests.filter((quest) => quest.id !== questId))
      );
  };

  return (
    <div className="p-4">
      {/* Player Profile */}
      <section className="mb-6">
        <h2 className="text-2xl font-bold">{profile.username}'s Dashboard</h2>
        <img
          src={profile.avatar || "https://via.placeholder.com/150"}
          alt="Profile"
          className="w-20 h-20 rounded-full mt-2"
        />
        <h3 className="mt-4 text-xl">Achievements</h3>
        <ul>
          {profile.achievements.map((ach, idx) => (
            <li key={idx}>{ach}</li>
          ))}
        </ul>
      </section>

      {/* Active Quests */}
      <section className="mb-6">
        <h3 className="text-xl font-bold">Active Quests</h3>
        <ul>
          {activeQuests.map((quest) => (
            <li key={quest.id} className="mb-2">
              <strong>{quest.name}</strong> - {quest.reward}
              <div className="mt-1">
                Progress: {quest.progress}%{" "}
                <progress value={quest.progress} max="100" className="w-full" />
              </div>
              <button
                onClick={() => handleMarkComplete(quest.id)}
                className="bg-green-500 text-white px-2 py-1 mt-2 rounded"
              >
                Mark Complete
              </button>
            </li>
          ))}
        </ul>
      </section>

      {/* Inventory */}
      <section>
        <h3 className="text-xl font-bold">Your Inventory</h3>
        <ul className="grid grid-cols-2 gap-4">
          {inventory.map((item) => (
            <li key={item.id} className="border p-2 rounded">
              <strong>{item.name}</strong>
              <img
                src={item.image || "https://via.placeholder.com/50"}
                alt={item.name}
                className="w-12 h-12 mt-2"
              />
              <button
                onClick={() => handleUseItem(item.id)}
                className="bg-blue-500 text-white px-2 py-1 mt-2 rounded"
              >
                Use
              </button>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}

export default UserDashboard;

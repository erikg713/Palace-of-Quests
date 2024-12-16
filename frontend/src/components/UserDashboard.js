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
import React, { useEffect, useState } from "react";

const UserDashboard = ({ userId }) => {
  const [activeQuests, setActiveQuests] = useState([]);
  const [inventory, setInventory] = useState([]);
  const [profile, setProfile] = useState({
    username: "Player",
    avatar: "",
    achievements: [],
  });
  const [isConnected, setIsConnected] = useState(false);

  useEffect(() => {
    // Initialize WebSocket
    const socket = new WebSocket(`wss://yourserver.com/ws/user/${userId}`);

    // Open connection
    socket.onopen = () => {
      setIsConnected(true);
      console.log("WebSocket connected");
    };

    // Close connection
    socket.onclose = () => {
      setIsConnected(false);
      console.log("WebSocket disconnected");
      reconnectSocket();
    };

    // Handle incoming messages
    socket.onmessage = (event) => {
      const message = JSON.parse(event.data);
      switch (message.type) {
        case "PROFILE_UPDATE":
          setProfile((prev) => ({ ...prev, ...message.data }));
          break;
        case "QUEST_UPDATE":
          setActiveQuests((prev) =>
            prev.map((quest) =>
              quest.id === message.data.id ? { ...quest, ...message.data } : quest
            )
          );
          break;
        case "INVENTORY_UPDATE":
          setInventory(message.data);
          break;
        default:
          console.warn("Unhandled WebSocket message:", message);
      }
    };

    // Cleanup on unmount
    return () => socket.close();
  }, [userId]);

  // Reconnection logic
  const reconnectSocket = () => {
    let attempt = 0;
    const retry = () => {
      setTimeout(() => {
        attempt += 1;
        console.log(`Reconnecting attempt ${attempt}`);
        const socket = new WebSocket(`wss://yourserver.com/ws/user/${userId}`);
        socket.onopen = () => {
          setIsConnected(true);
          console.log("Reconnected!");
        };
        socket.onclose = () => {
          if (attempt < 5) retry();
        };
      }, Math.min(1000 * 2 ** attempt, 30000)); // Exponential backoff
    };
    retry();
  };

  return (
    <div className="p-4">
      {/* Connection Status */}
      <div className="mb-4">
        <p>
          WebSocket Status:{" "}
          <span
            className={`font-bold ${
              isConnected ? "text-green-500" : "text-red-500"
            }`}
          >
            {isConnected ? "Connected" : "Disconnected"}
          </span>
        </p>
      </div>

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
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
};

export default UserDashboard;
import React, { useEffect, useState } from "react";

const UserDashboard = ({ userId }) => {
  const [activeQuests, setActiveQuests] = useState(new Map());
  const [inventory, setInventory] = useState(new Map());
  const [profile, setProfile] = useState({
    username: "Player",
    avatar: "",
    achievements: [],
  });
  const [isConnected, setIsConnected] = useState(false);
  const [retryCount, setRetryCount] = useState(0);

  const MAX_RETRIES = 5;

  // Modular WebSocket message handler
  const handleWebSocketMessage = (message) => {
    switch (message.type) {
      case "PROFILE_UPDATE":
        setProfile((prev) => ({ ...prev, ...message.data }));
        break;

      case "QUEST_UPDATE":
        setActiveQuests((prev) => {
          const updated = new Map(prev);
          updated.set(message.data.id, message.data);
          return updated;
        });
        break;

      case "INVENTORY_UPDATE":
        setInventory(new Map(message.data.map((item) => [item.id, item])));
        break;

      default:
        console.warn("Unhandled WebSocket message:", message);
    }
  };

  // Reconnection logic with retry limit
  const reconnectSocket = () => {
    if (retryCount >= MAX_RETRIES) {
      console.error("Maximum reconnection attempts reached");
      return;
    }

    setTimeout(() => {
      console.log(`Reconnection attempt ${retryCount + 1}`);
      initializeWebSocket();
      setRetryCount((prev) => prev + 1);
    }, Math.min(1000 * 2 ** retryCount, 30000)); // Exponential backoff
  };

  // Initialize WebSocket
  const initializeWebSocket = () => {
    const socket = new WebSocket(`wss://yourserver.com/ws/user/${userId}`);

    socket.onopen = () => {
      setIsConnected(true);
      setRetryCount(0);
      console.log("WebSocket connected");
    };

    socket.onclose = () => {
      setIsConnected(false);
      console.log("WebSocket disconnected");
      reconnectSocket();
    };

    socket.onmessage = (event) => {
      const message = JSON.parse(event.data);
      handleWebSocketMessage(message);
    };

    socket.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    return socket;
  };

  useEffect(() => {
    const socket = initializeWebSocket();
    return () => socket.close();
  }, [userId]);

  // Debounce updates for smoother re-renders
  const debouncedState = (stateMap) => Array.from(stateMap.values());

  return (
    <div className="p-4">
      {/* Connection Status */}
      <div className="mb-4">
        <p>
          WebSocket Status:{" "}
          <span
            className={`font-bold ${
              isConnected ? "text-green-500" : "text-red-500"
            }`}
          >
            {isConnected ? "Connected" : "Disconnected"}
          </span>
        </p>
        {!isConnected && retryCount >= MAX_RETRIES && (
          <button
            className="bg-blue-500 text-white px-4 py-2 rounded mt-2"
            onClick={reconnectSocket}
          >
            Retry Connection
          </button>
        )}
      </div>

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
          {debouncedState(activeQuests).map((quest) => (
            <li key={quest.id} className="mb-2">
              <strong>{quest.name}</strong> - {quest.reward}
              <div className="mt-1">
                Progress: {quest.progress}%{" "}
                <progress value={quest.progress} max="100" className="w-full" />
              </div>
            </li>
          ))}
        </ul>
      </section>

      {/* Inventory */}
      <section>
        <h3 className="text-xl font-bold">Your Inventory</h3>
        <ul className="grid grid-cols-2 gap-4">
          {debouncedState(inventory).map((item) => (
            <li key={item.id} className="border p-2 rounded">
              <strong>{item.name}</strong>
              <img
                src={item.image || "https://via.placeholder.com/50"}
                alt={item.name}
                className="w-12 h-12 mt-2"
              />
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
};

export default UserDashboard;

import React from "react";
import React, { useEffect, useState } from "react";
import axios from "axios";

const HomePage = () => {
  const [quests, setQuests] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/quests")
      .then((response) => setQuests(response.data))
      .catch((error) => console.error("Error fetching quests:", error));
  }, []);

  return (
    <div className="text-center">
      <h2>Available Quests</h2>
      <ul>
        {quests.map((quest) => (
          <li key={quest.id}>
            {quest.name} - Reward: {quest.reward} points
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HomePage;

const HomePage = () => {
  return (
    <div className="text-center">
      <h2>Welcome to Palace of Quests</h2>
      <p>Embark on an adventure in the metaverse!</p>
      <button className="btn btn-primary">Get Started</button>
    </div>
  );
};

export default HomePage;

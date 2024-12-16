import React, { useEffect, useState } from 'react';

function QuestList({ userId }) {
  const [quests, setQuests] = useState([]);

  useEffect(() => {
    fetch('/api/quests')
      .then(response => response.json())
      .then(data => setQuests(data));
  }, []);

  const acceptQuest = async (questId) => {
    await fetch('/api/quests/assign', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_id: userId, quest_id: questId }),
    });
    alert('Quest accepted!');
  };

  return (
    <div>
      <h2>Available Quests</h2>
      <ul>
        {quests.map(quest => (
          <li key={quest.id}>
            {quest.name} - Reward: {quest.reward}
            <button onClick={() => acceptQuest(quest.id)}>Accept</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default QuestList;

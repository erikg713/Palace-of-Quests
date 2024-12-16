import React, { useEffect, useState } from 'react';

function QuestHistory({ userId }) {
  const [completedQuests, setCompletedQuests] = useState([]);

  useEffect(() => {
    fetch(`/api/user/${userId}/quests/completed`)
      .then(response => response.json())
      .then(data => setCompletedQuests(data));
  }, [userId]);

  return (
    <div>
      <h2>Completed Quests</h2>
      <ul>
        {completedQuests.map(quest => (
          <li key={quest.id}>
            {quest.name} - Reward: {quest.reward}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default QuestHistory;

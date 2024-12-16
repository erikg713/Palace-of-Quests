import React, { useState, useEffect } from 'react';

function AdminQuestManager() {
  const [quests, setQuests] = useState([]);
  const [newQuest, setNewQuest] = useState({ name: '', reward: 0, description: '' });

  useEffect(() => {
    fetch('/api/quests')
      .then(response => response.json())
      .then(data => setQuests(data));
  }, []);

  const handleAddQuest = async () => {
    await fetch('/api/quests', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newQuest),
    });
    alert('Quest added!');
    setNewQuest({ name: '', reward: 0, description: '' });
  };

  const handleDeleteQuest = async (id) => {
    await fetch(`/api/quests/${id}`, { method: 'DELETE' });
    alert('Quest deleted!');
    setQuests(quests.filter(quest => quest.id !== id));
  };

  return (
    <div>
      <h3>Quests</h3>
      <ul>
        {quests.map(quest => (
          <li key={quest.id}>
            {quest.name} - Reward: {quest.reward}
            <button onClick={() => handleDeleteQuest(quest.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <div>
        <h4>Add New Quest</h4>
        <input
          type="text"
          placeholder="Name"
          value={newQuest.name}
          onChange={(e) => setNewQuest({ ...newQuest, name: e.target.value })}
        />
        <input
          type="number"
          placeholder="Reward"
          value={newQuest.reward}
          onChange={(e) => setNewQuest({ ...newQuest, reward: parseInt(e.target.value) })}
        />
        <textarea
          placeholder="Description"
          value={newQuest.description}
          onChange={(e) => setNewQuest({ ...newQuest, description: e.target.value })}
        />
        <button onClick={handleAddQuest}>Add Quest</button>
      </div>
    </div>
  );
}

export default AdminQuestManager;

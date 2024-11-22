// components/Game/LevelProgression.js
import React from 'react';

const LevelProgression = () => {
  return (
    <div>
      <h3>Level Progression</h3>
      <p>Next level in 100 XP</p>
      <div className="progress-bar">
        <div className="progress" style={{ width: '30%' }}></div>
      </div>
    </div>
  );
};

export default LevelProgression;
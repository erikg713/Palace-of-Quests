import React from 'react';
import AdminQuestManager from './AdminQuestManager';
import AdminItemManager from './AdminItemManager';

function AdminPanel() {
  return (
    <div>
      <h2>Admin Panel</h2>
      <section>
        <h3>Manage Quests</h3>
        <AdminQuestManager />
      </section>
      <section>
        <h3>Manage Marketplace Items</h3>
        <AdminItemManager />
      </section>
    </div>
  );
}

export default AdminPanel;

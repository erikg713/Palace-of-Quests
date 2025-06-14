// Palace of Quests – Pi Network Metaverse Game Entry
// Handles Pi Network authentication, scene initialization, and error management

import { initScene, startGameLoop } from './scene';
import { piLogin, onPiUserChange } from './pi-network';
import { showToast, showError } from './utils/ui';

// App-wide state (exposed in dev mode for debugging)
const appState = {
  piUser: null,
  accessToken: null,
};

// --- Pi Network Authentication ---
async function authenticateWithPi() {
  try {
    const { user, token } = await piLogin();
    appState.piUser = user;
    appState.accessToken = token;
    showToast(`Welcome, ${user.username}!`);

    onPiUserChange((newUser) => {
      appState.piUser = newUser;
      showToast(newUser ? `Switched to ${newUser.username}` : 'User logged out.');
    });
  } catch (err) {
    showError('Pi Network authentication failed. Please open in Pi Browser and try again.');
    console.error('[Pi Network Auth Error]', err);
  }
}

// --- 3D Metaverse Scene Setup ---
(function initializeMetaverse() {
  try {
    initScene();
    requestAnimationFrame(startGameLoop);
  } catch (err) {
    showError('Failed to initialize the 3D environment.');
    console.error('[3D Scene Init Error]', err);
  }
})();

// --- UI Event Bindings ---
(function bindUIEvents() {
  const piConnectBtn = document.getElementById('piConnectBtn');
  if (piConnectBtn) {
    piConnectBtn.addEventListener('click', authenticateWithPi);
  }
})();

// --- Global Error Handling ---
window.addEventListener('error', (event) => {
  showError('An unexpected error occurred.');
  console.error('[Global Error]', event.error || event.message);
});

// --- Expose state for debugging (remove in production) ---
if (process.env.NODE_ENV !== 'production') {
  window.__APP_STATE__ = appState;
}

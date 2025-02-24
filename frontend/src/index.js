import React from "react";
import ReactDOM from "react-dom";
import ReactDOM from 'react-dom/client';
import App from './App';
import { UserProvider } from './context/UserContext';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <UserProvider>
    <App />
  </UserProvider>
);

ReactDOM.render(
  <React.StrictMode>
    <PalaceOfQuests />
  </React.StrictMode>,
  document.getElementById("root")
);

import React from 'react';
import ReactDOM from 'react-dom';
import './assets/styles/styles.css';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './styles/global.css';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

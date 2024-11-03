import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import Marketplace from './pages/Marketplace';
import Profile from './pages/Profile';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/marketplace" component={Marketplace} />
        <Route path="/profile" component={Profile} />
      </Switch>
    </Router>
  );
}

export default App;

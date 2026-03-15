import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

import './App.css';
function App() {
  return (
    <Router>
      <header className="app-header">
        <img src={process.env.PUBLIC_URL + '/octofitapp-small.svg'} alt="OctoFit Logo" className="app-logo" />
        <h1 style={{margin: 0, fontSize: '2rem', fontWeight: 700, letterSpacing: '2px'}}>OctoFit Tracker</h1>
        <nav style={{marginLeft: '2rem'}}>
          <Link to="/activities">Activities</Link>
          <Link to="/leaderboard">Leaderboard</Link>
          <Link to="/teams">Teams</Link>
          <Link to="/users">Users</Link>
          <Link to="/workouts">Workouts</Link>
        </nav>
      </header>
      <div className="container">
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={<div className="text-center mt-5"><h1 className="display-4">Welcome to OctoFit Tracker!</h1><p className="lead">Track your fitness, join teams, and compete on the leaderboard.</p></div>} />
        </Routes>
      </div>
    </Router>
  );
}
export default App;

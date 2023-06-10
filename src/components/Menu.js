import React from "react";
import { NavLink } from "react-router-dom";
import logo from './logo.svg';

export default function Menu() {
  return (
    <div className="menu">
      <div className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h2>ARTICLES SCIENTIFIQUES</h2>
      </div>
      <ul>
        <li>
          <NavLink
            to="/"
            className={({ isActive }) => (isActive ? "activelink" : undefined)}
          >
            Acceuil
          </NavLink>
        </li>
        <li>
          <NavLink
            to="/add"
            className={({ isActive }) => (isActive ? "activelink" : undefined)}
          >
            Ajouter un article
          </NavLink>
        </li>
        <li>
          <NavLink
            to="/list"
            className={({ isActive }) => (isActive ? "activelink" : undefined)}
          >
            Tous les articles
          </NavLink>
        </li>
      </ul>
    </div>
  );
}

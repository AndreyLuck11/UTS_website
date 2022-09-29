import React from 'react';
import './App.css';
import AppRouter from "./AppRouter";
import {BrowserRouter} from "react-router-dom";
import NavBar from "./UI/Navbar/NavBar";

function App() {
  return (
      <div>
          <BrowserRouter>
              <NavBar></NavBar>
              <AppRouter/>
          </BrowserRouter>
      </div>
  );
}

export default App;

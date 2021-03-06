import React, { Component } from 'react';
import pancake_intro from './components/static/pancake_intro.jpg';
import maple_intro from './components/static/maple_intro.jpg';
import { Link } from 'react-router-dom';
import './App.css';

class App extends Component {

  render() {

    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Pancake & Maple Welcome You!</h1>
        </header>

        <p className="App-intro">
          To get started, click on a kitty.
        </p>

        <Link to="/PanList">
          <button>
            <img src={ pancake_intro } className="Pancake-intro" alt="pan-intro" onClick={this.onClick}/>
          </button>
        </Link>

        <Link to="/MapleList">
          <button >
            <img src={ maple_intro } className="Maple-intro" alt="maple-intro" onClick={this.onClick}/>
          </button>
        </Link>

      </div>
    );
  }
}

export default App;

import React, { Component } from 'react';
import pancake_intro from './static/pancake_intro.jpg';
import maple_intro from './static/maple_intro.jpg';
import { Link } from 'react-router-dom';
import './App.css';

class App extends Component {
  onClick = (evt) => {
    evt.preventDefault();
  }

  render() {

    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Pancake & Maple Welcome You!</h1>
        </header>

        <p className="App-intro">
          To get started, click on a kitty.
        </p>

        <button>
          <img src={ pancake_intro } className="Pancake-intro" alt="pan-intro" onClick={this.onClick}/>
        </button>

        <button >
          <img src={ maple_intro } className="Maple-intro" alt="maple-intro" onClick={this.onClick}/>
        </button>

      </div>
    );
  }
}

export default App;

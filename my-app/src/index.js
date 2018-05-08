import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import App from './App';
import CatList from './components/CatList'
import PanFetch from './static/PanFetch.gif'
import './index.css';
import registerServiceWorker from './registerServiceWorker';
// import { Router, Route, Switch } from 'react-router';


ReactDOM.render(
	<Router>
    <div>
      <Route exact path="/" component={App} />
      <Route 
        path="/PanList" 
        render={(props) => (
          <CatList
            {...props}
            name='Pancake'
            power={ PanFetch }
          />
        )} 
      />
      <Route 
        path="/MapleList" 
        render={(props) => (
          <CatList 
            {...props} 
            name='Maple' 
          />
        )}
      />
    </div>
  </Router>, 
	document.getElementById('root'));
registerServiceWorker();

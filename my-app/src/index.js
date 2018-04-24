import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import App from './App';
import PanList from './components/PanList'
import  MapleList from './components/MapleList'
import './index.css';
import registerServiceWorker from './registerServiceWorker';
// import { Router, Route, Switch } from 'react-router';


ReactDOM.render(
	<Router>
      <div>
        <Route exact path="/" component={App} />
        <Route path="/PanList" component={PanList} />
        <Route path="/MapleList" component={MapleList} />
      </div>
  	</Router>, 
	document.getElementById('root'));
registerServiceWorker();

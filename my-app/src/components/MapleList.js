import React from 'react'
import { Link } from 'react-router-dom';

const MapleList = () => {
  return (
    <div className="nav">
      <ul>
        <li>list item</li>
        <li>list item</li>
      </ul>
      <Link to="/"><button>Back Home</button></Link>
    </div>
  )
}

export default MapleList

import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { Link } from 'react-router-dom';


class CatList extends Component {
  static propTypes = {
    name: PropTypes.string.isRequired
  }

  render() {
    return (
      <div className="nav">
        <ul>
          <li>{`Name: ${this.props.name}`}</li>
          <li>list item</li>
        </ul>
        <Link to="/"><button>Back Home</button></Link>
      </div>
    )
  }
}

export default CatList

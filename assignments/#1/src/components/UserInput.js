
import React from 'react';

import './UserInput.css';

export const UserInput = (props) => {
  return (
    <input
      className="UserInput" type='text'
      onChange={props.change} value={props.value} placeholder={props.placeholder} />)
}
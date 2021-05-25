
import React from 'react';
import './CharComponent.css';

export const CharComponent = (props) => {
  return <p onClick={props.click} className="CharComponent">{props.char}</p>
}
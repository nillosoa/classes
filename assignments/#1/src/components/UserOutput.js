
import React from 'react';

import './UserOutput.css';

export const UserOutput = (props) => {
  let text = props.children;
  for (let key in props) {
    if (!['children', 'style'].includes(key)) {
      text = text.replaceAll(`$${key}`, props[key] || props[`${key}Alt` || '']);
    }
  }
  return (
    <div>
      <p className="UserOutput" style={props.style}>{ text }</p>
    </div> );
}
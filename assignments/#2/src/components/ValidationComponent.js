
import React from 'react';

export const ValidationComponent = (props) => {
  if ( props.textLength < 4 ) {
  	return <p>Text too short</p>
  } else {
  	return <p>Text long enough</p>
  }
}
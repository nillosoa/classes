
import React from 'react';

import classes from './Input.css';


const input = ( props ) => {

  let inputElement = null;
  const inputClasses = [ classes.InputElement ];
  if ( props.invalid && props.shouldValidate && props.touched ) {
    inputClasses.push(classes.Invalid);
  }

  switch ( props.elementType ) {
    case ( 'textarea' ):
      inputElement = <textarea
        {...props.elementConfig}
        onChange={props.changed}
        value={props.value}
        className={inputClasses.join(' ')} />;
      break;
    case ( 'select' ):
      inputElement = (
        <select
          value={props.value}
          onChange={props.changed}
          className={inputClasses.join(' ')}>
          {
            props.elementConfig.options.map(option => (
              <option key={option.value} value={option.value}>{option.displayValue}</option>
            ))
          }
        </select>
      );
      break;
    case ( 'input' ): default:
      inputElement = <input
        {...props.elementConfig}
        value={props.value}
        onChange={props.changed}
        className={inputClasses.join(' ')} />;
      break;
  }

  return (
    <div className={classes.Input}>
      <label className={classes.Label}>{ props.label }</label>
      { inputElement }
    </div>
  );
};

export default input;


import React, { useEffect, useRef, useContext } from 'react';

import classes from './Cockpit.css';
import AuthContext from '../../context/auth-context';


const cockpit = (props) => {

  const toggleBtnRef = useRef(null);
  const authContext = useContext(AuthContext);

  useEffect(
    () => {
      console.log('[Cockpit.js] useEffect');
      // setTimeout(() => {
      //   alert('Saved data to cloud');
      // }, 1000);
      toggleBtnRef.current.click();
      return () => {
        console.log('[Cockpit.js] clean up work in useEffect');
      } }, []);

  let btnClass = '';
  if ( props.showPersons ) {
    btnClass = classes.Red;
  }

  const assignedClasses = [];
  if ( props.personsLength <= 2 ) {
    assignedClasses.push(classes.red);
  }

  if ( props.personsLength <= 1 ) {
    assignedClasses.push(classes.bold)
  }

  return (
    <div className={classes.Cockpit}>
      <h1>{props.appTitle}</h1>
      <p className={assignedClasses.join(' ')}>This is really working!</p>
      <button
        ref={toggleBtnRef}
        className={btnClass}
        onClick={props.clicked}>Switch name</button>
      <button onClick={authContext.login}>Log in</button>
      {
      // <AuthContext.Consumer>
      //   {context => <button onClick={context.login}>Log in</button>}
      // </AuthContext.Consumer>
      }
    </div> );
}

export default  React.memo(cockpit);
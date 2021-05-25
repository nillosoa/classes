
import React from 'react';

import classes from './Logo.css';
import burgerLogo from '../../assets/images/burger-logo.png';


const logo = ( props ) => (
  <div
    style={{height: props.height }} className={classes.Logo}>
    <img src={burgerLogo} alt="Burger Builder logo" />
  </div>
);

export default logo;

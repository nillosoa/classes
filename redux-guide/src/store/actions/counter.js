
import * as actionTypes from './actions';


export const increment = () => {
  return {
    type: actionTypes.INCREMENT
  };
};

export const decrement = () => {
  return {
    type: actionTypes.DECREMENT
  };
};

export const add = (val) => {
  return {
    val,
    type: actionTypes.ADD
  };
};

export const sub = (val) => {
  return {
    val,
    type: actionTypes.SUB
  };
};
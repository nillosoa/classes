
import * as actionTypes from './actions';


export const saveResult = (result) => {
  return {
    result,
    type: actionTypes.STORE_RESULT
  };
}

export const storeResult = (result) => {
  return (dispatch, getState) => {
    const oldCounter = getState().ctr.counter;
    console.log(oldCounter);
    setTimeout(() => {
      dispatch(saveResult(result));  }, 2000)
  }
};

export const deleteResult = (id) => {
  return {
    id,
    type: actionTypes.DELETE_RESULT
  };
};


import { updateObject } from '../utility';
import * as actionTypes from '../actions/actions';


const initialState = {
  results: []
};

const deleteResult = (state, action) => {
  const results = state.results.filter(res => res.id !== action.id);
  return updateObject(state, { results: results });
}

const reducer = ( state = initialState, action ) => {
  switch ( action.type ) {
    case actionTypes.STORE_RESULT:
      return updateObject(state, {
        results: state.results.concat({ id: new Date(), value: action.result })
      });
    case actionTypes.DELETE_RESULT:
      // const id = action.id;
      // const newArray = [ ...state.results ];
      // newArray.splice(id, 1);
      return deleteResult(state, action);
    default:
      return state
  }
}

export default reducer;

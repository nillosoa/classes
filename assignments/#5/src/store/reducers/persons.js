
import * as actionTypes from '../actions';


const initialState = {
    persons: []
};

const reducer = ( state = initialState, action ) => {
    switch ( action.type ) {
        case actionTypes.ADD_PERSON:
            return {
                ...state,
                persons: state.persons.concat({
                    id: Math.random(),
                    name: action.personData.name || 'Max',
                    age: action.personData.age || Math.floor( Math.random() * 40 )
                })
            }
        case actionTypes.DEL_PERSON:
            return {
                ...state,
                persons: state.persons.filter(id => id !== action.id)
            }
        default:
            return state;
    }
};

export default reducer;

import { createStore } from 'redux'; // manage the state

import {
    ADD_TEMPLATE
} from './actions';

const initialStore = {
    template: {
        data: {},
        templates: {},
        questions: {},
        firebase_object: {}
    }
};

const rootReducer = ( state = initialStore, action ) => {
    switch ( action.type ) {
        case ADD_TEMPLATE:
            return {
                ...state,
                template: action.event
            }
        default:
            return state
    }
};

export default createStore ( rootReducer );
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore } from 'redux';

import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import personsReducer from './store/reducers/persons';


const store = createStore(personsReducer);

const app = (
    <Provider
        store={store}> <App /> </Provider>
);

ReactDOM.render(app, document.getElementById('root'));
registerServiceWorker();

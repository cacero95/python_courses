import 'core-js/es/map';
import 'core-js/es/set';
import 'raf/polyfill';
import React from "react";
import Routes from './Routes';
import '../styles/styles.css';
import { Provider } from 'react-redux';
import store from '../redux/store';

const Dads = () => (
    <Provider store={store}>
        <Routes/>
    </Provider>
);
export default Dads;
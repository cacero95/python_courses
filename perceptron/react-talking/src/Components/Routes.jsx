import React from 'react';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Interpreter from './Pages/Interpreter';


const Routes = () => (
    <Router>
        <Switch>
            <Route path="/" component={Interpreter}></Route>
        </Switch>
    </Router>
);
export default Routes;
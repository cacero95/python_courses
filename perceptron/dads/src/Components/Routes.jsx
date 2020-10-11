import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Generator from "./Pages/Generator";
import Home from "./Pages/Home";
import firebase from '../firebase-config';
import { connect } from 'react-redux';
import {
    addTemplate
} from '../redux/actionCreators'

const Routes = ({ addTemplate }) => {
    const dba = firebase.database().ref('templates');
    dba.on( 'value', ( snapshot ) => {
        addTemplate({
            dba,
            data: snapshot.val()
        })
    })
    return (
        <div className="main_container">
            <Router>
                <Switch>
                    <Route path="/" exact component={Generator} />
                    <Route path="/home" component={Home} />
                </Switch>
            </Router>
        </div>
    )
}
const mapDispathToProps = {
    addTemplate
}
export default connect(null, mapDispathToProps)(Routes);
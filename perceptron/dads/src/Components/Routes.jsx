import React, { useEffect } from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Generator from "./Pages/Generator";
import Home from "./Pages/Home";
import firebase from '../firebase-config';
import { connect } from 'react-redux';
import {
    addTemplate
} from '../redux/actionCreators'
import Monitor from "./Pages/Monitor";
import Colombia from "./Pages/Colombia";

const Routes = ({ addTemplate }) => {
    const dba = firebase.database().ref('/');
    const templates = firebase.database().ref('templates');
    const questions = firebase.database().ref('Questions');

    dba.on( 'value', ( snapshot ) => {
        addTemplate({
            firebase_object: firebase,
            templates,
            questions,
            data: snapshot.val()
        })
    })
    useEffect(() => {
        if ( !firebase.auth().currentUser ) {
            firebase.auth().signInWithEmailAndPassword(
                'carlos@testing.com',
                'Xboxplaywi95'
            );
        }
    }, [])
    return (
        <div className="main_container" id="main_container">
            <Router>
                <Switch>
                    <Route path="/" exact component={Generator} />
                    <Route path="/home" component={Home} />
                    <Route path="/monitor" component={Monitor} />
                    <Route path="/colombia" component={Colombia} />
                    <Route path="/Colombia" component={Colombia} />
                </Switch>
            </Router>
        </div>
    )
}
const mapDispathToProps = {
    addTemplate
}
export default connect(null, mapDispathToProps)(Routes);
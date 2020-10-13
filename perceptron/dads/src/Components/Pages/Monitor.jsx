import React from 'react';
import { connect } from 'react-redux';

const Monitor = ({ firebase }) => {
    const { data } = firebase;
    return (
        <div></div>
    )
}

const mapStateToProps = ( state ) => ({
    firebase: state.template
})

export default connect(mapStateToProps, null)(Monitor);
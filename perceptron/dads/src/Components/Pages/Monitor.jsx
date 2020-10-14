import React from 'react';
import { connect } from 'react-redux';
import ChartGenerator from '../Atoms/ChartGenerator';
import MonitorTable from '../Atoms/MonitorTable';
const Monitor = ({ firebase }) => {
    const { data } = firebase;
    console.log(data);
    return (
        data.tracking ? (
            <div className="MonitorChart">
                <MonitorTable data = { data.tracking.monitor } />
                <br/>
                <ChartGenerator data = { data.tracking.monitor } />
            </div>
        ) : (
            <div>Loading...</div>
        )
    )
}

const mapStateToProps = ( state ) => ({
    firebase: state.template
})

export default connect(mapStateToProps, null)(Monitor);
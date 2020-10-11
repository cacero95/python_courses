import React from 'react';
import { connect } from 'react-redux';

const Home = ({ template }) => {
    const { data } = template;
    return (
        data ? (
            <div className="Editor_container">
                <div className="webPage">
                    <div 
                        dangerouslySetInnerHTML={ { __html: data.content } } 
                    />
                </div>
            </div>
        ) : (
            <div className="Editor_container">
                Cargando...
            </div>
        )
    )
}

const mapStateToProps = ( state ) => ({
    template: state.template
})

export default connect(mapStateToProps, null)(Home);
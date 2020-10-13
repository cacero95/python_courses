import React from 'react';
import { connect } from 'react-redux';

const Home = ({ template }) => {
    const { templates } = template.data;
    return (
        templates ? (
            <div className="Editor_container">
                <div className="webPage">
                    <div 
                        dangerouslySetInnerHTML={ { __html: templates.content } } 
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
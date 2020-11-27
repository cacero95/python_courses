import React, { Fragment } from 'react';
import industries from '../../../assets/industries.png';
import architecture from '../../../assets/architecture.png';
import young from '../../../assets/model_young.png';

const Intro = () => {
    return (
        <Fragment>
            <h2>
                Clasificación industrias
            </h2>
            <div className="industries_categorization">
                <img src = { industries } alt=""/>
            </div>
            <h2>
                Arquitectura ciudad inteligente
            </h2>
            <div className="architecture_smart">
                <img src = { architecture } alt=""/>
            </div>
            <h2>
                Modelo de madurez
            </h2>
            <div className = "model_young">
                <img src = { young } alt=""/>
            </div>
        </Fragment>
    )
}
export default Intro;
import React, { Fragment, useState } from 'react';
import levels from '../../../assets/level_young.svg';
import { connect } from 'react-redux';
import Proccesor_questions from './Proccesor_questions';

let scores = {
    seguridad: 0,
    movilidad: 0,
    emergencias: 0,
    salud: 0,
    servicios_publicos: 0,
    medio_ambiente: 0,
    educacion: 0,
    agricultura: 0,
    turismo: 0
};
// 27 questions
const Asks = ({ firebase }) => {
    const info = Proccesor_questions.build_data();
    const [ name_city, setName ] = useState('');
    const [ questions, setQuestions ] = useState({});
    
    const make_validations = ( key, value ) => {
        questions[ key ] = value;
        setQuestions({
            ...questions
        });
    }

    const build_input = ( info ) => {
        return info.type === 'select' ? (
            <select
                value = { questions[ info.key ] ? questions[ info.key ] : 'select'  }
                onChange = {
                    (e) => make_validations( info.key, e.target.value )
                }
            >
                <option value = "select">
                    Seleccionar
                </option>
                {
                    info.options.map(( element ) => {
                        return (
                            <option value = { element.value } 
                                key = { `${ element.label }` }
                            >
                                { element.label }
                            </option>
                        )
                    })
                }
            </select>
        ) : (
            <input
                type = { info.type }
                placeholder = {
                    info.type === 'number' ? 0 : 'Completar...'
                }
                value = { questions[ info.key ] ? questions[ info.key ] : '' }
                onChange = {
                    (e) => make_validations( info.key, e.target.value )
                }
            />
        );
    }

    const handleSend = () => {
        let validator = true;
        Object.keys( questions ).forEach((key, index) => {
            validator = !questions[key] || questions[key] === ''
            ? false : validator;
            const question_element = info.questions[ index ];
            const value_gain = question_element.validator( questions[ key ] );
            scores[ question_element.class_validator ] = scores[ question_element.class_validator ] + value_gain;
        });
        console.log( scores );
    }
    return (
        <Fragment>
            <h2>Medición de Percepción</h2>
            <div className = "levels_young">
                <img src = { levels } alt=""/>
            </div>
            <div className = "colombia_formulary">
                <div className="section_formulary">
                    <label>
                        Nombre de la ciudad
                    </label>
                    <input
                        type = "text"
                        value = { name_city }
                        onChange = {
                            (e) => setName( e.target.value )
                        }
                        placeholder = "Nombre"
                    />
                </div>
                {
                    info.questions.map((element) => {
                        return (
                            <div className="section_formulary" key = { element.key } id = { element.key }>
                                <label>
                                    { element.question }
                                </label>
                                { build_input( element ) }
                                {
                                    element.explanation ? (
                                        <div className = "explanation_ask">
                                            { element.explanation }
                                        </div>
                                    ) : (
                                        <Fragment></Fragment>
                                    )
                                }
                            </div>
                        )
                    })
                }
                {
                   Object.keys( questions ).length === info.questions.length
                   ? (
                        <button
                            onClick = { handleSend }
                        >
                            Enviar
                        </button>

                   ) : (
                       <Fragment></Fragment>
                   )
                }
            </div>
        </Fragment>
    )
}
const mapStateToProps = ( state ) => ({
    firebase: state.template
})
export default connect(mapStateToProps,null)(Asks);
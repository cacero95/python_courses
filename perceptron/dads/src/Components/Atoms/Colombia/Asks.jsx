import React, { Fragment, useState } from 'react';
import levels from '../../../assets/level_young.svg';
import Proccesor_validator from '../../../assets/resources/data.json';
import { connect } from 'react-redux';

let scores = {};
// 27 questions
const Asks = ({ firebase }) => {
    const info = Proccesor_validator;
    const [ name_city, setName ] = useState('');
    const [ questions, setQuestions ] = useState({});
    const make_validations = ( key, value ) => {
        questions[ key ] = value;
        setQuestions({
            ...questions
        });
    }
    const handleSend = () => {
        let validator = true;
        Object.keys( questions ).forEach((key, index) => {
            validator = !questions[key] && questions[key] === ''
            ? false : validator;
            const question_element = info.questions[ index ];
            scores[ question_element.class_validator ] = question_element.validator( questions[key] );
        });
        if ( validator ) {

        }
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
                                <input
                                    type = "text"
                                    value = { questions[ element.key ] ? questions[ element.key ] : '' }
                                    onChange = {
                                        (e) => make_validations( element.key, e.target.value )
                                    }
                                    placeholder = "Completar"
                                />
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
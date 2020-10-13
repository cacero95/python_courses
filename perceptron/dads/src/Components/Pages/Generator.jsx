import React, { useState } from 'react';
import CKEditor from 'ckeditor4-react';
import { connect } from 'react-redux';

const Generator = ({ history, firebase }) => {
    const { templates, data } = firebase;
    const [ content, setContent ] = useState('');
    const handleChange = ( event ) => {
        setContent( event.editor.getData() );
    }
    const handleClick = () => {
        if ( content !== '' ) {
            templates.set({
                title: 'main',
                content
            });
            history.push("/home");
        }        
    }
    return (
        <div className="Editor_container">
            <CKEditor
                onChange = { handleChange }
                data = { data.templates ? data.templates.content : <p>Cargando....</p> }
            />
            <button id="upload_state" onClick = { handleClick }>
                Cargar
            </button>
        </div>
    )
}

const mapStateToProps = ( state ) => ({
    firebase: state.template
})


export default connect(mapStateToProps, null)(Generator);
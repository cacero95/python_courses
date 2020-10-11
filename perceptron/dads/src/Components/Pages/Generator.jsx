import React, { useState } from 'react';
import CKEditor from 'ckeditor4-react';
import { connect } from 'react-redux';

const Generator = ({ history, firebase }) => {
    const [ content, setContent ] = useState('');
    const handleChange = ( event ) => {
        setContent( event.editor.getData() );
    }
    const handleClick = () => {
        if ( content !== '' ) {
            firebase.dba.set({
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
                data = { firebase.data ? firebase.data.content : <p>Cargando....</p> }
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
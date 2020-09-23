import React, { Component } from 'react';
import axios from 'axios';
import qs from 'qs';

const localUrl = "http://localhost:8000/";
class Interpreter extends Component {

    state = {
        phrase:''
    }

    handleChange = (event) => {
        this.setState({
            phrase: event.target.value
        })
    }
    show_message = (id, styles, message) => {
        let element = document.getElementById(id)
        element.className = '';
        element.classList.add(styles);
        element.innerHTML = message
    }
    handleClick = (event) => {
        if ( event.keyCode === 13 && this.state.phrase !== '' ) {
            axios({
                method: 'post',
                url: `${localUrl}interpreter/`,
                data: qs.stringify({
                    phrase: this.state.phrase
                }),
                headers: {
                    'content-type': 'application/x-www-form-urlencoded;charset=utf-8'
                }
            }).then((resp)=> {
                const data  = resp.data;
                switch (data.out) {
                    case 'positive':
                        this.show_message(
                            'show_message',
                            'positive', 
                            `El comentario '${data.message}' es positivo`
                        );
                        break;
                    case 'negative':
                        this.show_message(
                            'show_message',
                            'negative', 
                            `El comentario '${data.message}' es negativo`
                        );
                        break;
                    default:
                        this.show_message(
                            'show_message',
                            'neutral',
                            `El comentario '${data.message}' es neutral`
                        );
                        break;
                            
                }
            }).catch(err=>{
                this.show_message(
                    'show_message',
                    'negative',
                    `Por favor revisar ${err.message}`
                );
            })
        }
    }
    render() {
        return(
            <div id="input_container">
                <span id="show_message">Hola como estas</span>
                <div id="input_content">
                    <div id="type_input">
                        <input 
                            type="text"
                            onChange={this.handleChange} 
                            placeholder="Digite la frase" 
                            value={this.state.phrase}
                            onKeyUp={this.handleClick} 
                        />
                    </div>
                </div>
            </div>
        )
    }
}

export default Interpreter;
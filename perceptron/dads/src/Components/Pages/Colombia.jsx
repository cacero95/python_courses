import React, { Fragment, useEffect, useState } from 'react';
import logo from '../../assets/LOGO_COLOMBIA.svg';
import ideas from '../../assets/IDEAS.svg';
import Asks from '../Atoms/Colombia/Asks';
import Intro from '../Atoms/Colombia/Intro';
const Colombia = () => {
    const [ intro, setIntro ] = useState( true );
    useEffect(()=> {
        document.getElementById('main_container').style.background = '#ffffff';
    }, [])
    return (
        <div className = "colombia_container">
            <div className="colombia_head">
                <div>
                    <img src = { logo } alt=""/>
                </div>
                <div>
                    <img src = { ideas } alt=""/>
                </div>
            </div>
            <div className="colombia_body">
                <div className="colombia_content">
                    {
                        intro ? (
                            <Fragment>
                                <button id = "colombia_request" onClick = { () => setIntro( false ) }>
                                    IR A ENCUESTA
                                </button>
                                <Intro
                                    handleClick = { setIntro }
                                />
                            </Fragment>
                        ) : (
                            <Fragment>
                                <button id = "colombia_request" onClick = { () => setIntro( true ) }>
                                    VOLVER
                                </button>
                                <Asks
                                    handleClick = { setIntro }
                                />
                            </Fragment>
                        )
                    }
                </div>
            </div>
        </div>
    )
}

export default Colombia;
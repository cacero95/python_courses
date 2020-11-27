import React from 'react';

const boolean_validator = (resp) => {
    return resp === 'true' ? 100 : 0
}

const build_data = () => {
    return {
        "questions":[
            {
                "question": "¿ Cual es el índice de criminalidad en la ciudad?",
                "key": "criminal_index",
                validator: (resp) => {
                    if ( resp > 80 ) {
                        return 0 // muy alto
                    }
                    else if ( resp > 60 ) {
                        return 40 // alto
                    }
                    else if ( resp > 40 ) {
                        return 60 // medio
                    }
                    else if ( resp > 20 ) {
                        return 60 // bajo
                    }
                    return 100 // muy bajo
                },
                "class_validator": "seguridad",
                "type": "number"
            },
            {
                "question": "¿Hay algún sistema que permita notificar alguna estación de policía en caso de robo?",
                "key": "security_system",
                validator: boolean_validator,
                "class_validator": "seguridad",
                "type": "select",
                "options": [
                   {
                       "label": "si",
                       "value": true
                   },
                   {
                       "label": "no",
                       "value": false
                   }
                ]
            },
            {
                "question": "En promedio cuanto se demora la respuesta de una estación de policía en caso de algún delito ( responder en minutos )?",
                "key": "criminal_time",
                validator: (resp) => {
                    if ( resp > 5.6 ) {
                        return 0
                    }
                    else if ( resp > 2.5 ) {
                        return 50
                    }
                    return 100
                },
                "class_validator": "seguridad",
                "type": "number"
            },
            {
                "question": "¿Hay algún sistema de información que permita informar a los conductores la condición del tráfico en la ciudad?",
                "key": "traffic_information",
                validator: boolean_validator,
                "class_validator": "movilidad",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                 ]
            },
            {
                "question": "¿Existe algún sistema inteligente de semaforización que permita agilizar el tráfico ?",
                "key": "intelligent_traffic",
                validator: boolean_validator,
                "class_validator": "movilidad",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                 ]
            },
            {
                "question": "¿En la ciudad se maneja el metro como medio de transporte?",
                "key": "metro",
                validator: boolean_validator,
                "class_validator": "movilidad",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                 ]
            },
            {
                "question": "¿El sistema de semaforización de la ciudad está adaptado para darle prioridad a las sistemas de emergencia?",
                "key": "emergency_system",
                validator: boolean_validator,
                "class_validator": "emergencias",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                 ]
            },
            {
                "question": "¿Existe un sistema de vigilancia que permita detectar emergencias en la ciudad, que requieran atención de personal capacitado?.",
                "key": "emergency_detect",
                validator: boolean_validator,
                "class_validator": "emergencias",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                 ]
            },
            {
                "question": "¿Cual es el índice de accidentes o siniestros en la ciudad?",
                "key": "accident_index",
                validator: ( resp ) => {
                    if ( resp > 5.6 ) {
                        return 0
                    }
                    else if ( resp > 2.5 ) {
                        return 50
                    }
                    return 100
                },
                "class_validator": "emergencias",
                "type": "number"
            },
            {
                "question": "¿El acceso al historial médico de una persona está disponible para todas las entidades médicas, de tal manera que la misma pueda recibir atención de manera rápida?",
                "key": "mediacal_history",
                validator: boolean_validator,
                "class_validator": "salud",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                 ]
            },
            {
                "question": "¿Cual categoría promedio tienen las entidades médicas en la ciudad?",
                "key": "medical_category",
                validator: (resp) => {
                    if ( resp === 1 ) {
                        return 0
                    }
                    else if ( resp === 2 ) {
                        return 50
                    }
                    return resp === 3 ? 75 : 100
                },
                "class_validator": "salud",
                explanation: (
                    <ul className = "explain_healt">
                        <li>
                            <div>
                                <span>
                                    Categoría 1
                                </span>
                                <span>
                                    Puesto de salud, posta de salud o consultorio con profesionales de salud no médicos.
                                </span>
                            </div>
                        </li>
                        <li>
                            <div>
                                <span>
                                    Categoría 2
                                </span>
                                <span>
                                    Puesto de salud o posta de salud (con médico). Además de los consultorios médicos (con médicos con o sin especialidad).
                                </span>
                            </div>
                        </li>
                        <li>
                            <div>
                                <span>
                                    Categoría 3
                                </span>
                                <span>
                                    Corresponde a los centros de salud, centros médicos, centros médicos especializados y policlínicos.
                                </span>
                            </div>
                        </li>
                        <li>
                            <div>
                                <span>
                                    Categoría 4
                                </span>
                                <span>
                                    Agrupan los centros de salud y los centros médicos con camas de internamiento.
                                </span>
                            </div>
                        </li>
                    </ul>
                ),
                "type": "select",
                "options": [
                    {
                        "label": "Categoria 1",
                        "value": 1
                    },
                    {
                        "label": "Categoria 2",
                        "value": 2
                    },
                    {
                        "label": "Categoria 3",
                        "value": 3
                    },
                    {
                        "label": "Categoria 4",
                        "value": 4
                    }
                ]
            },
            {
                "question": "En caso de un accidente grave que necesite un proceso de alto riesgo ( transfusión, operación, etc. ), ¿la ciudad puede responder bajo sus capacidades?",
                "key": "medical_capabilities",
                validator: boolean_validator,
                "class_validator": "salud",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                 ]
            },
            {
                "question": "¿Cuál es el porcentaje del terreno de la ciudad que cubre el transporte público (75%)?",
                "key": "public_transport",
                validator: (resp) => {
                    return resp
                },
                "class_validator": "servicios_publicos",
                "type": "number"
            },
            {
                "question": "¿Existe un sistema de información que permita informar el estado del transporte y así mismo mejorar la experiencia del usuario al momento de usar el servicio?",
                "key": "transport_qa",
                validator: boolean_validator,
                "class_validator": "servicios_publicos",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                 ]
            },
            {
                "question": "¿Cuál es el índice de personas en porcentaje que prefieren usar el pago electrónico en la ciudad ?",
                "key": "electronical_pay",
                validator: (resp) => {
                    return resp
                },
                "class_validator": "servicios_publicos",
                "type": "number"
            },
            {
                "question": "¿En la ciudad se manejan herramientas que permitan reutilizar residuos?",
                "key": "waste_usefull",
                validator: boolean_validator,
                "class_validator": "medio_ambiente",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                 ]
            },
            {
                "question": "¿Cuál es el porcentaje de estaciones de calidad del aire que cumplen en la ciudad según el SIAC?",
                "key": "air_qa",
                validator: (resp) => {
                    return resp
                },
                "class_validator": "medio_ambiente",
                "type": "number"
            },
            {
                "question": "¿En la ciudad manejan herramientas para poder manejar los recursos naturales?",
                "key": "natural_resources",
                validator: boolean_validator,
                "class_validator": "medio_ambiente",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                ]
            },
            {
                "question": "¿ hasta qué nivel de educación está disponible para los ciudadanos ?.",
                "key": "education_level",
                validator: ( resp ) => {
                    if ( resp === 3 ) {
                        return 100;
                    }
                    return resp <= 1 ? 0 : 50;
                },
                "class_validator": "educacion",
                "type": "select",
                "options": [
                    {
                        "label": "Clase 1",
                        "value": 1
                    },
                    {
                        "label": "Clase 2",
                        "value": 2
                    },
                    {
                        "label": "Clase 3",
                        "value": 3
                    }
                ]
            },
            {
                "question": "¿ Existe la posibilidad de que un estudiante pueda acceder a los contenidos académicos de su institución de manera virtual ?",
                "key": "virtual_education",
                validator: boolean_validator,
                "class_validator": "educacion",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                ]
            },
            {
                "question": "¿ El gobierno realiza iniciativas que promuevan la participación estudiantil, con el objetivo de generar educación en algún tema en específico ?",
                "key": "student_participation",
                validator: boolean_validator,
                "class_validator": "educacion",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                ]
            },
            {
                "question": "¿ Existen herramientas que permitan gestionar los cultivos en la ciudad ?",
                "key": "cultives_management",
                validator: boolean_validator,
                "class_validator": "agricultura",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                ]
            },
            {
                "question": "¿ Existe alguna herramienta que permita generar la comunicación entre agricultores y distribuidores ( supermercados) ?",
                "key": "supermarkets",
                validator: boolean_validator,
                "class_validator": "agricultura",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                ]
            },
            {
                "question": "¿ Existen herramientas en la ciudad que permitan proteger los cultivos o huertas que proveen a la ciudad ?.",
                "key": "cultives_protect",
                validator: boolean_validator,
                "class_validator": "agricultura",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                ]
            },
            {
                "question": "¿ Cual es el índice en porcentaje de turismo en la ciudad anualmente?",
                "key": "turistic_porcentages",
                validator: (resp) => {
                    if ( resp > 3000000 ) { // bogota 4.515.932
                        return 100
                    }
                    return resp > 2000000 ? 50 : 0
                },
                "class_validator": "turismo",
                "type": "number"
            },
            {
                "question": "¿ Existe alguna herramienta que permita dar a conocer los servicios y los costos de estos al turista antes de realizar el viaje ?",
                "key": "cost_services",
                validator: boolean_validator,
                "class_validator": "turismo",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                ]
            },
            {
                "question": "¿ La ciudad maneja herramientas que permitan publicitar y dar a conocer sus servicios y la cultura ?",
                "key": "publish_culture",
                validator: boolean_validator,
                "class_validator": "turismo",
                "type": "select",
                "options": [
                    {
                        "label": "si",
                        "value": true
                    },
                    {
                        "label": "no",
                        "value": false
                    }
                ]
            }
        ]
    }
}
export default { build_data }
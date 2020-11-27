import React, { Fragment } from 'react'

const BackUp = () => {
    return (
        <Fragment>
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
                <div className="section_formulary">
                    <label>
                        ¿Cual es el índice de criminalidad en la ciudad?
                    </label>
                    <input
                        type = "text"
                        value = { asks.criminal ? asks.criminal : '' }
                        onChange = {
                            (e) => make_validations( { criminal: e.target.value } )
                        }
                        placeholder = "Nombre"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿Hay algún sistema que permita notificar alguna estación de policía en caso de robo?
                    </label>
                    <input
                        type = "text"
                        value = { asks.criminal_system ? asks.criminal_system : '' }
                        onChange = {
                            (e) => make_validations( { criminal_system: e.target.value } )
                        }
                        placeholder = "Nombre"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿En promedio cuanto se demora la respuesta de una estación de policía en caso de algún delito ( responder en minutos )?
                    </label>
                    <input
                        type = "text"
                        value = { asks.criminal_time ? asks.criminal_time : '' }
                        onChange = {
                            (e) => make_validations( { criminal_time: e.target.value } )
                        }
                        placeholder = "Nombre"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿Hay algún sistema de información que permita informar a los conductores la condición del tráfico en la ciudad?
                    </label>
                    <input
                        type = "text"
                        value = { asks.traffic_data ? asks.traffic_data : '' }
                        onChange = {
                            (e) => make_validations( { traffic_data: e.target.value } )
                        }
                        placeholder = "Nombre"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿Existe algún sistema inteligente de semaforización que permita agilizar el tráfico?
                    </label>
                    <input
                        type = "text"
                        value = { asks.signal_data ? asks.signal_data : '' }
                        onChange = {
                            (e) => make_validations( { signal_data:e.target.value } )
                        }
                        placeholder = "Nombre"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿En la ciudad se maneja el metro como medio de transporte?
                    </label>
                    <input
                        type = "text"
                        value = { asks.metro ? asks.metro : '' }
                        onChange = {
                            (e) => make_validations( { metro:e.target.value } )
                        }
                        placeholder = "Nombre"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿El sistema de semaforización de la ciudad está adaptado para darle prioridad a las sistemas de emergencia?
                    </label>
                    <input
                        type = "text"
                        value = { asks.alert_systems ? asks.alert_systems : '' }
                        onChange = {
                            (e) => make_validations( { alert_systems:e.target.value } )
                        }
                        placeholder = "Nombre"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿Existe un sistema de vigilancia que permita detectar emergencias en la ciudad, que requieran atención de personal capacitado?
                    </label>
                    <input
                        type = "text"
                        value = { asks.surveillance_detect? asks.surveillance_detect : '' }
                        onChange = {
                            (e) => make_validations( { surveillance_detect: e.target.value } )
                        }
                        placeholder = "Nombre"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿Cual es el índice de accidentes o siniestros en la ciudad?
                    </label>
                    <input
                        type = "text"
                        value = { asks.survivol_index ? asks.survivol_index : '' }
                        onChange = {
                            (e) => make_validations( { survivol_index: e.target.value } )
                        }
                        placeholder = "Nombre"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿El acceso al historial médico de una persona está disponible para todas las entidades médicas, de tal manera que la misma pueda recibir atención de manera rápida?
                    </label>
                    <input
                        type = "text"
                        value = { asks.medic_history ? asks.medic_history : '' }
                        onChange = {
                            (e) => make_validations( { medic_history: e.target.value } )
                        }
                        placeholder = "Nombre"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿Cual categoría promedio tienen las entidades médicas en la ciudad?
                    </label>
                    <input
                        type = "text"
                        value = { asks.medical_category ? asks.medical_category : '' }
                        onChange = {
                            (e) => make_validations( { medical_category: e.target.value } )
                        }
                        placeholder = "Procentaje"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        En caso de un accidente grave que necesite un proceso de alto riesgo ( transfusión, operación, etc. ), ¿la ciudad puede responder bajo sus capacidades?
                    </label>
                    <input
                        type = "text"
                        value = { asks.tranfusion_risk ? asks.tranfusion_risk : '' }
                        onChange = {
                            (e) => make_validations( { tranfusion_risk: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿Cuál es el porcentaje del terreno de la ciudad que cubre el transporte público (75%)?.
                    </label>
                    <input
                        type = "text"
                        value = { asks.public_transport ? asks.public_transport : '' }
                        onChange = {
                            (e) => make_validations( { public_transport: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿Existe un sistema de información que permita informar el estado del transporte y así mismo mejorar la experiencia del usuario al momento de usar el servicio?
                    </label>
                    <input
                        type = "text"
                        value = { asks.info_system ? asks.info_system : '' }
                        onChange = {
                            (e) => make_validations( { info_system: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿Cuál es el índice de personas en porcentaje que prefieren usar el pago electrónico en la ciudad ?
                    </label>
                    <input
                        type = "text"
                        value = { asks.electronic_pay ? asks.electronic_pay : '' }
                        onChange = {
                            (e) => make_validations( { electronic_pay: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿En la ciudad se manejan herramientas que permitan reutilizar residuos?
                    </label>
                    <input
                        type = "text"
                        value = { asks.waste ? asks.waste : '' }
                        onChange = {
                            (e) => make_validations( { waste: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿Cuál es el porcentaje de estaciones de calidad del aire que cumplen en la ciudad según el SIAC?
                    </label>
                    <input
                        type = "text"
                        value = { asks.air_qa ? asks.air_qa : '' }
                        onChange = {
                            (e) => make_validations( { air_qa: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿En la ciudad manejan herramientas para poder manejar los recursos naturales?
                    </label>
                    <input
                        type = "text"
                        value = { asks.natural_resources ? asks.natural_resources : '' }
                        onChange = {
                            (e) => make_validations( { natural_resources: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿ hasta qué nivel de educación está disponible para los ciudadanos ?
                    </label>
                    <input
                        type = "text"
                        value = { asks.education_level ? asks.education_level : '' }
                        onChange = {
                            (e) => make_validations( { education_level: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿ Existe la posibilidad de que un estudiante pueda acceder a los contenidos académicos de su institución de manera virtual ?
                    </label>
                    <input
                        type = "text"
                        value = { asks.virtual_education ? asks.virtual_education : '' }
                        onChange = {
                            (e) => make_validations( { virtual_education: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿ El gobierno realiza iniciativas que promuevan la participación estudiantil, con el objetivo de generar educación en algún tema en específico ?
                    </label>
                    <input
                        type = "text"
                        value = { asks.student_participation ? asks.student_participation : '' }
                        onChange = {
                            (e) => make_validations( { student_participation: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿ Existen herramientas que permitan gestionar los cultivos en la ciudad ?
                    </label>
                    <input
                        type = "text"
                        value = { asks.cultives_management ? asks.cultives_management : '' }
                        onChange = {
                            (e) => make_validations( { cultives_management: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿ Existe alguna herramienta que permita generar la comunicación entre agricultores y distribuidores ( supermercados ) ?  
                    </label>
                    <input
                        type = "text"
                        value = { asks.supermarkets ? asks.supermarkets : '' }
                        onChange = {
                            (e) => make_validations( { supermarkets: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿ Existen herramientas en la ciudad que permitan proteger los cultivos o huertas que proveen a la ciudad ?
                    </label>
                    <input
                        type = "text"
                        value = { asks.cultives_protect ? asks.cultives_protect : '' }
                        onChange = {
                            (e) => make_validations( { cultives_protect: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿ Cual es el índice en porcentaje de turismo en la ciudad ?
                    </label>
                    <input
                        type = "text"
                        value = { asks.turistic_porcentages ? asks.turistic_porcentages : '' }
                        onChange = {
                            (e) => make_validations( { turistic_porcentages: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿ Existe alguna herramienta que permita dar a conocer los servicios y los costos de estos al turista antes de realizar el viaje ?
                    </label>
                    <input
                        type = "text"
                        value = { asks.turistic_costs ? asks.turistic_costs : '' }
                        onChange = {
                            (e) => make_validations( { turistic_costs: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿ La ciudad maneja herramientas que permitan publicitar y dar a conocer sus servicios y la cultura ?
                    </label>
                    <input
                        type = "text"
                        value = { asks.turistic_publich ? asks.turistic_publich : '' }
                        onChange = {
                            (e) => make_validations( { turistic_publich: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
                <div className="section_formulary">
                    <label>
                        ¿ La ciudad maneja herramientas que permitan publicitar y dar a conocer sus servicios y la cultura ?
                    </label>
                    <input
                        type = "text"
                        value = { asks.turistic_publich ? asks.turistic_publich : '' }
                        onChange = {
                            (e) => make_validations( { turistic_publich: e.target.value } )
                        }
                        placeholder = "completar"
                    />
                </div>
        </Fragment>
    )
}
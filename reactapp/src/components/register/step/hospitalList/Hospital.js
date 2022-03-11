import React from 'react';
const Hospital = ({hospital, handleHospitals}) => {

    return (
        <React.Fragment>
            <div>
                <h3>Hospital : {hospital.hospital_name}</h3>
                <h3>Hospital ID :{hospital.hospital_id}</h3>
                <h4>Hospital address : {hospital.hospital_address1}</h4>
                <h4>Hospital city : {hospital.hospital_city}</h4>
                <h4>Hospital state : {hospital.hospital_state}</h4>
                <h4>Hospital zipcode : {hospital.hospital_zipcode}</h4>
                <button onClick={()=>{ handleHospitals(hospital.hospital_id);
                                    alert("your appointment has been approved") }}>
                    Make an appointment
                </button>
            </div>
        </React.Fragment>
    )
}
export default Hospital;
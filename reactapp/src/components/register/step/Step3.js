import React, {useState,useEffect } from 'react';
import Hospital from './hospitalList/Hospital';
const Step3 = ({prevStep, nextStep, handleChange, values}) =>{
    const [ hospitalList, setHospitalList ] = useState([]);
    useEffect(()=>{
        const getHospital = async () =>{
            const hospitalListFromServer = await fetchHospital();
            setHospitalList(hospitalListFromServer);
        }
        getHospital();
    },[])

    //fetchHospital
    const fetchHospital = async () =>{
    const res = await fetch(`http://127.0.0.1:8000/api/hospitalDetail/zipcode/${values.zipcode}`)
    const data = await res.json()
    console.log(data)
    return data
    }
    return(
        <React.Fragment>
            {hospitalList.map( (hospital) => (
                <Hospital
                    key ={hospital.hospital_id}
                    hospital = {hospital}
                    handleChange={handleChange}
                />
            )
            )}
            <button onClick={prevStep}>
                Previous Step
            </button>
            <button onClick={nextStep}>
                Confirm
            </button>
        </React.Fragment>
    )
}

export default Step3;
import React, {useState,useEffect } from 'react';
import Hospital from './hospitalList/Hospital';
const Step3 = ({prevStep, nextStep, values, handleHospital}) =>{

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
    const data = await res.json();
    console.log("data : "+data);
    return data
    }
    const handleHospitals = async(input) =>{
        return await  handleHospital(input);
    }
    return(
        <React.Fragment>
            <div>
            { hospitalList.length===0 ? ("Sorry, No Hospital on that zipcode.") :
                ( hospitalList.map( (hospital) => (
                    <Hospital
                    key ={hospital.hospital_id}
                    hospital = {hospital}
                    handleHospitals={handleHospitals}
                    />)
            ))}
            </div>
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
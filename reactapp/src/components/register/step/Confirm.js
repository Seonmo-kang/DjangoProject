import React, {useEffect, useState} from "react";

//Step 4 ( Confirm page. last step )
const Confirm = ({prevStep, values}) =>{
    // const [cookie, setCookie, removeCookie] = useCookies(['cookie-name']);
    const [vaccine, setVaccine] = useState([]);
    const [vaccineType, setVaccineType] = useState([]);
    const vaccineContext = () => {
        switch (values.vaccine) {
            case "fd":
                setVaccine(["First Dose"]);
                break;
            case "bd":
                setVaccine(["Boost Dose"]);
                break;
            case "ad":
                setVaccine(["Additional Dose"]);
                break;
            default:;
        }
    }
    const vaccineTypeContext = () => {
        switch (values.vaccineType) {
            case "pf":
                setVaccineType(["Pfizer"]);
                break;
            case "js":
                setVaccineType(["Janssen"]);
                break;
            case "all":
                setVaccineType(["All"]);
                break;
            default:
                ;
        }
    }

    let _csrfToken = null;
    const getCsrfToken = async () => {
        if(_csrfToken === null ){
            const response = await fetch('http://localhost:8000/api/getCSRF',{
                method : "GET",
                credentials: 'omit',
            })
            const data = await response.json();
            _csrfToken = data.csrfToken;
        }
        return _csrfToken;
    }

    const submitData = async () =>{
        const response = await fetch('http://localhost:8000/api/info/register/',{
            method: 'POST',
            headers: {
                'X-CSRFToken': _csrfToken,
                "Content-Type": "application/json",
                "Accept": 'application/json'
                 },
            // credentials: 'include',
            body: JSON.stringify({"values": values})
        })
        .then( response => {
            if(response.ok){
                console.log("Post is success");
                alert("Post is submitted.");
                this.props.history.push('/');
            };

        });

    }

    useEffect(()=>{
        vaccineTypeContext();
        vaccineContext();
        getCsrfToken();
    },[])


    return (
        <React.Fragment>
        <div>confirm page</div>
        <ul>
            <li>firstName: {values.firstName}</li>
            <li>lastName: {values.lastName}</li>
            <li>Birth Day: {values.birthOfDate}</li>
            <li>Zipcode: {values.zipcode}</li>
            <li>State: {values.state}</li>
            <li>Consent Acknowledge{values.consentAck}</li>
            <li>Hospital: {values.hospital}</li>
            <li>Vaccine: {vaccine}</li>
            <li>Vaccine Type: {vaccineType}</li>
        </ul>
        <button onClick={prevStep}>
            Previous Step
        </button>
        <button onClick={submitData}>
            Submit
        </button>
        </React.Fragment>
    )
}
export default Confirm;
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import PropTypes from 'prop-types';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';

//import "react-datepicker/dist/react-datepicker.css";
//import DatePicker from 'react-datepicker';

// import TextField from '@mui/material/TextField';
// import IconButton from '@mui/material/IconButton';
// import MenuIcon from '@mui/icons-material/Menu';


const Step1 = ({nextStep, handleChange,handleChecked ,values}) => {

    const continueAction = e =>{
        e.preventDefault();
        console.log(values);


        nextStep();
    }

    return (
        <React.Fragment>
            <Box sx={{ flexGrow: 1 }}>
                <AppBar position="static">
                    <Toolbar>Registeration form</Toolbar>
                </AppBar>
            </Box>
            <div>Step 1</div>
            <Box>
                <label>birth of date :
                    <input
                        type="date"
                        placeholder="mm/dd/yyyy"
                        value={values.birthOfDate}
                        onChange={handleChange('birthOfDate')}
                    />
                </label>
            </Box>
            <Box>
                <label>Zipcode :
                    <input
                        type="text"
                        placeholder="Zip code"
                        value={values.zipcode}
                        onChange={handleChange('zipcode')}
                    />
                </label>
            </Box>
            <Box>
                <label>State :
                    <input
                        type="text"
                        placeholder="Zip code"
                        value={values.state}
                        onChange={handleChange('state')}
                    />
                </label>
            </Box>
            <Box>
                <label>Vaccine :
                    <select defaultValue={ values.vaccine } onChange={handleChange('vaccine')}>
                        <option value="fd">First Dose</option>
                        <option value="bd">Booster Dose</option>
                        <option value="ad">Additional Dose</option>
                    </select>
                </label>
            </Box>

            <Box>
                <label>VaccineType :
                    <select defaultValue={values.vaccineType} onChange={handleChange('vaccineType')}>
                        <option value="pf">pfizer</option>
                        <option value="js">janssen</option>
                        <option value="all">both</option>
                    </select>
                </label>
            </Box>
            <Box>
                <label>Consent Acknowledge :
                <input type='checkbox' onChange={handleChecked}/>
                </label>
            </Box>
            <button>
                <Link to='/'>
                    Go back Home
                </Link>
            </button>
            <button
                onClick ={continueAction}>
                Continue
            </button>
        </React.Fragment>
    )
}
Step1.propTypes ={
    zipcode: PropTypes.number
}
export default Step1;
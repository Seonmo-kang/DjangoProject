import React, {Component} from 'react';
import Box from '@mui/material/Box';
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
const Step2 = ({nextStep, prevStep,handleChange ,values}) => {

    return(
        <React.Fragment>
            <Box sx={{ flexGrow: 1 }}>
                <AppBar position="static">
                    <Toolbar>Registeration form {values.step}</Toolbar>
                </AppBar>
            </Box>
            <div>Step 2</div>
            <Box>
                <label>First Name :
                    <input
                        type="text"
                        placeholder="First (Given) Name"
                        value={values.firstName}
                        onChange={handleChange('firstName')}
                    />
                </label>
            </Box>
            <Box>
                <label>Last Name :
                    <input
                        type="text"
                        placeholder="Last Name"
                        value={values.lastName}
                        onChange={handleChange('lastName')}
                    />
                </label>
            </Box>
            <button onClick={prevStep}>
                Previous Step
            </button>
            <button onClick={nextStep}>
                Continue
            </button>
        </React.Fragment>
    )
}

export default Step2;
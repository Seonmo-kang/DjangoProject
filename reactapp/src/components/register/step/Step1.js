import React, {Component} from 'react';

import DatePicker from 'react-datepicker';

import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import TextField from '@mui/material/TextField';
import "react-datepicker/dist/react-datepicker.css";
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
// = ({nextStep,handleChange,handleDate,values}) =>
class Step1 extends React.Component {
    constructor(props) {
        super(props);
        this.state ={
            date : new Date(),
        }
    }
    continue = e => {
        e.preventDefault();
        this.props.nextStep();
    };
    onDate = (date) =>{
        this.setState({date:date});
    }
    render() {
        const {values} = this.props;
        return (
                <React.Fragment>
                    <Box sx={{ flexGrow: 1 }}>
                    <AppBar position="static">
                        <Toolbar>"Registeration form"</Toolbar>
                    </AppBar>
                    </Box>
                    <Box sx={{ flexGrow: 1 }}>
                    <DatePicker
                        id="birthDate"
                        selected={this.onDate}
                        onChange={ this.onDate }
                        dateFormat = "MM/dd/yyyy"
                    />
                    {/*<TextField*/}
                    {/*    id="date"*/}
                    {/*    margin ="normal"*/}
                    {/*    label="Choose your birth date"*/}
                    {/*    type="date"*/}
                    {/*    defaultValue={values.birthOfDate}*/}
                    {/*    onChange={values.handleDate}*/}
                    {/*    InputLabelProps={{*/}
                    {/*        shrink: true,*/}
                    {/*    }}*/}
                    {/*/>*/}
                    </Box>
                    <Button
                        label="Continue"
                        onClick ={this.continue}

                    />
                </React.Fragment>
        );
    }
}
export default Step1;
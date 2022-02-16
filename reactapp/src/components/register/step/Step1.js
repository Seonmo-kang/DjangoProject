import React, {Component} from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import TextField from '@mui/material/TextField';
import IconButton from '@mui/material/IconButton';
// import MenuIcon from '@mui/icons-material/Menu';

class Step1 extends Component {
    constructor(props) {
        super(props);
    }
    continue = e =>{
        e.preventDefault();
        this.props.nextStep();
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
                    <TextField
                        hintText="Enter your birth date"
                    />
                    <Button
                        label="Continue"
                        primary={true}
                        onClick ={this.continue}
                    />
                </React.Fragment>
        );
    }
}
export default Step1;
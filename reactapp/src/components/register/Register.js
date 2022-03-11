import React from "react";
import Step1 from "./step/Step1";
import Step2 from "./step/Step2";
import Step3 from "./step/Step3";
import Confirm from "./step/Confirm";

class Register extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            step: 1,
            firstName: '',
            lastName: '',
            birthOfDate: '',
            zipcode: '',
            state: '',
            vaccine: 'fd',
            vaccineType: 'all',
            consentAck: false,
            hospital:''
        }

    }
    //go back to previous step
    prevStep = () =>{
        const { step } =this.state;

        this.setState({step: step-1});
    }
    //go to next step
    nextStep = () =>{
        const { step, firstName, lastName, birthOfDate,zipcode, vaccine, vaccineType,hospital } =this.state;

        if(step===1&&(!birthOfDate||!zipcode||!vaccine||!vaccineType)){
            alert("Step1 - Please type all input.");
            return ;
        }

       if(step===2&&(!firstName||!lastName)){
               alert("Step2 - Please type all input.");
               return;
           }
       if(step===3&&(!hospital)){
           alert("Step3 - Please select your hospital.");
           return ;
       }
        this.setState({step: step+1});
    }
    // handle field change
    handleChange = input => e => {
        this.setState({ [input]: e.target.value });
        console.log(this.state);
    }
    // handle ConsentAck change
    consentChange = e =>{
        this.setState({consentAck: e.currentTarget.checked});
        console.log(this.state);
    }
    handleHospital = id => {
        this.setState( {hospital : id});
        console.log(this.state);
    }

    render() {
        const {step} =this.state;
        const { birthOfDate, zipcode, firstName, lastName, state, hospital,vaccine, vaccineType, consentAck} = this.state;
        const values ={ birthOfDate, zipcode, firstName,lastName,hospital,state,vaccine, vaccineType, consentAck };

            switch(step){
                case 1:
                    return(<Step1
                        nextStep={this.nextStep}
                        handleChange={this.handleChange}
                        handleChecked ={this.consentChange}
                        values={values}
                    />
                )
                case 2:
                    return(<Step2
                        prevStep={this.prevStep}
                        nextStep={this.nextStep}
                        handleChange={this.handleChange}
                        values={values}
                        />
                )
                case 3:
                    return(<Step3
                        prevStep={this.prevStep}
                        nextStep={this.nextStep}
                        handleChange={this.handleChange}
                        handleHospital={this.handleHospital}
                        values={values}
                        />
                    )
                case 4:
                    return(<Confirm
                        prevStep={this.prevStep}
                        nextStep={this.nextStep}
                        values={values}
                            />)
                default: ;
            }
    }
}
export default Register;
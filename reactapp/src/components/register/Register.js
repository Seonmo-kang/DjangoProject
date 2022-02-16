import React, {useState} from "react";
import Step1 from "./step/Step1";
import Step2 from "./step/Step2";
import Step3 from "./step/Step3";

class Register extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            step:1,
            birthOfDate: '',
            zipcode:'',
            vaccine:'',
            vaccineType:'',
            consentAck: false
        }
    }
    //go back to previous step
    prevStep = () =>{
        const { step } =this.state;
        this.setState({step: step-1});
    }
    //go to next step
    nextStep = () =>{
        const { step } =this.state;
        this.setState({step: step+1});
    }
    // handle field change
    handleChange = input => e => {
        this.setState({ [input]: e.target.value });
    }

    render() {
        const {step} =this.state;
        const { birthOfDate, zipcode, vaccine, vaccineType, consentAck} = this.state;
        const values ={ birthOfDate, zipcode, vaccine, vaccineType, consentAck };

            switch(step){
                case 1:
                    return(<Step1
                        nextStep={this.nextStep}
                        handleChange={this.handleChange}
                        values={values}
                    />
                )
                case 2:
                    return(<Step2
                        prevStep={this.prevStep}
                        nextStep={this.nextStep}
                        values={values}
                        />
                )
                case 3:
                    return(<Step3
                        prevStep={this.prevStep}
                        nextStep={this.nextStep}
                        values={values}
                        />
                    )
                // case 4:
                //     return(<Confirm
                //         prevStep={this.prevStep}
                //         nextStep={this.nextStep}
                //         values={values}
                //             />)
                default: ;
            }
    }
}
export default Register;
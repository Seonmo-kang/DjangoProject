import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component{

    constructor(props) {
        super(props);
        this.state ={
            data:[],
            loaded:true,
            placeholder: "Loading"
        };
    }
    componentDidMount() {
        fetch("../../../appFolder/info")
            .then(response=>{
                if(response.status>400){
                    return this.setState(()=>{
                        return {placeholder: "Something wrong!"};
                    });
                }
                return response.json();
            })
            .then(data=>{
                this.setState(()=>{
                    return{
                        data,
                        loaded: true
                    };
                });
            });
    }
    render() {
        return(
                <ul>
                    {this.state.data.map(info=>{
                        return (
                            <>
                            <li>{info.info_index}</li>
                            <li>{info.info_dateOfBirth}</li>
                            <li>{info.info_zipCode}</li>
                            <li>{info.info_vaccine}</li>
                            <li>{info.info_vaccineType}</li>
                            <li>{info.info_consentAck}</li>
                            </>
                        );
                    })}
                </ul>
        );
    }
}
export default App;
const container = document.getElementById("app");
render(<App/>,container);
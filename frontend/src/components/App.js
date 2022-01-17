import React, { Component } from "react";
import render from "react-dom";

class App extends Component{
    constructor(props) {
        super(props);
        this.state ={
            data:[],
            loaded:false,
            placeholder: "Loading"
        };
    }
    componentDidMount() {
        fetch("frontend/info")
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
                            <li key={info.info_index}>
                                {info.info_dateOfBirth} <br/>
                                {info.info_zipCode} <br/>
                                {info.info_vaccine} <br/>
                                {info.info_vaccineType} <br/>
                                {info.info_consentAck}
                            </li>
                        );
                    })}
                </ul>
        );
    }
}
export default App;
const container = document.getElementById("App");
render(<App/>,container);
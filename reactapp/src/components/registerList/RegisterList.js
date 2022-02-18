import React from "react";

const API_HOST = 'http://localhost:8000';

class RegisterList extends React.Component{
    constructor(props) {
        super(props);
        this.state ={
            data:[],
            loaded:true,
            placeholder: "Loading"
        };
    }
    componentDidMount() {
        fetch('http://localhost:8000/appFolder/info')
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
                        <div key={info.info_index}>
                            <li>User #{info.info_index}</li>
                            <li>Birth of date : {info.info_dateOfBirth}</li>
                            <li>Zip code : {info.info_zipCode}</li>
                            <li>Vaccine : {info.info_vaccine}</li>
                            <li>Type : {info.info_vaccineType}</li>
                            <li>Consent :{info.info_consentAck}</li>
                        </div>
                    );
                })}
            </ul>
        );
    }
}
export default RegisterList;
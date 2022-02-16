import React from "react";
import { Link } from "react-router-dom";

class Home extends React.Component{
    render() {
        return (
            <React.Fragment>
            <h2>This is home page</h2>
            <Link to='/register'>Register</Link>
            <br/>
            <Link to='/registerList'>RegisterList</Link>
            </React.Fragment>
        );
    }
}
export default Home
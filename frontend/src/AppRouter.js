import React from "react";
import {BrowserRouter} from "react-router-dom";
import App from "./components/App";

class AppRouter extends React.Component{
    render(){
        return(
            <div>
                <BrowserRouter>
                    <App/>
                </BrowserRouter>
            </div>
        )
    }
}
const container = document.getElementById("AppRouter");
render(<AppRouter/>,container);


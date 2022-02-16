import React, { Component } from "react";
import { render } from "react-dom";
import {Routes,Route} from "react-router-dom";
import Register from "./register/Register";
import Home from "./structure/home/Home";
import NotFound from "./structure/notFound/NotFound";

class App extends Component{

    render() {
        return (
                <Routes>
                    <Route path="/" exact element={<Home />}/>
                    <Route path="/register" exact={true} element={<Register />}/>
                    <Route path="*" element={<NotFound />}/>
                </Routes>
        );
    }
}
export default App;
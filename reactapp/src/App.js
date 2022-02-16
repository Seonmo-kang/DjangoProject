import React from "react";
import {Routes,Route} from "react-router-dom";
import './App.css';
import RegisterList from "./components/registerList/RegisterList";
import Register from "./components/register/Register";
import Home from "./components/home/Home";

class App extends React.Component{
  render(){
    return (
        <Routes>
            <Route path='/registerlist' element={<RegisterList/>}/>
            <Route path='/register' element={<Register/>}/>
            <Route path='/' element={<Home />}/>
        </Routes>
    )
  }
}

export default App;

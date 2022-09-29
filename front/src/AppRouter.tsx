import React from 'react';
import {Route, Routes} from "react-router";
import EventsList from "./pages/EventsList/EventsList";
import HomePage from "./pages/HomePage/HomePage";

const AppRouter = () => {
    return (
        <div>
            <Routes>
                <Route path='/' element={<HomePage/>}/>
                <Route path='/events' element={<EventsList/>}/>
            </Routes>
        </div>
    );
};

export default AppRouter;

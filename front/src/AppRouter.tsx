import React from 'react';
import {Route, Routes} from "react-router";
import EventsList from "./pages/EventsList/EventsList";
import HomePage from "./pages/HomePage/HomePage";
import CreateEventPage from "./pages/CreateEventPage/CreateEventPage";

const AppRouter = () => {
    return (
        <div>
            <Routes>
                <Route path='/' element={<HomePage/>}/>
                <Route path='/events' element={<EventsList/>}/>
                <Route path='/admin/creat-event' element={<CreateEventPage/>}/>
            </Routes>
        </div>
    );
};

export default AppRouter;

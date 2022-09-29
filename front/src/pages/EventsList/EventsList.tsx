import React, {useEffect, useState} from 'react';
import './EventsList.scss'
import NavBar from "../../UI/Navbar/NavBar";
import {useFetching} from "../../hooks/useFetching";
import EventsService from "../../API/EventsService";
import EventCard from "../../components/EventCard/EventCard";
import {EventList} from "../../types/eventsInterface";

const EventsList = () => {

    const [events, setEvents] = useState<EventList>();

    const [fetchEvents, isLoading, error] = useFetching( async () => {
        const respons = await EventsService.getAll();
        console.log(respons.data)
        setEvents(respons.data);
    })

    useEffect(() => {
        fetchEvents();
    }, [])

    // function renderItems() {
    //     events?.map(item => {
    //         return  <EventCard></EventCard>
    //     })
    // }

    return (
        <div className="event-list">
            {events?.map(item => {
                return <EventCard event={item} />
            })}
        </div>
    );
};

export default EventsList;

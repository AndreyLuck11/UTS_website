import React from 'react';
import './EventCard.scss'
import {EventPrev} from "../../types/eventsInterface";
import {useNavigate} from "react-router";

interface EventCardProps {
    event: EventPrev;
}

const EventCard = ({event}: EventCardProps) => {

    const navigate = useNavigate();

    return (
        <div className="event-card" onClick={() => {window.open( `${event.url}`, '_blank');}}>
            <div className="event-card__title">{event.title}</div>
            <div className="event-card__d-p-wrapper">
                <div className="event-card__date"><span>Дата проведения:</span>
                    {event.date_of_event_start} - {event.date_of_event_end}
                </div>
                <div className="event-card__point"><span>Место проведения:</span>{event.location}</div>
            </div>
        </div>
    );
};

export default EventCard;

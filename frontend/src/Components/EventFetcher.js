import { useState } from 'react';

const EventFetcher = () => {
    const [events, setEvents] = useState([]);

    const fetchEvents = async () => {
        try {
            const response = await fetch('http://localhost:5000/events');
            const data = await response.json();

            setEvents(data);
        } catch (error) {
            console.error('Error:', error);
        }
    }

    return (
        <div>
            <button onClick={fetchEvents}></button>
            {events.map((event, index) => (
                <div key={index}>
                    <p>Player ID: {event.player_id}</p>
                    <p>Player Type: {event.event_type}</p>
                    <p>Player Date: {JSON.stringify(event.event_data)}</p>
                    <p>Player ID: {new Date(event.timestamp).toString()}</p>
                </div>
            ))}
        </div>
    );
}

export default EventFetcher;

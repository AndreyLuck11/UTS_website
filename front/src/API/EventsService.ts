import axios from "axios";
import {EventList} from "../types/eventsInterface";

export default class EventsService {
    static async getAll() {
        return await axios.get<EventList>('/api/v1/event');
    }
}

export type EventList = EventPrev[]

export interface EventPrev {
    id: number
    title: string
    date_of_event_start: string
    image_url: any
    cat: Cat
    date_of_event_end: string
    location: string
    url: string
}

export interface Cat {
    id: number
    name: string
}

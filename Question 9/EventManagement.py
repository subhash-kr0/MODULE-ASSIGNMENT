class Event:
    _id_counter = 1  # Class-level attribute to generate unique IDs
    
    def __init__(self, name, date, time, location):
        self._id = Event._id_counter  # Unique ID
        Event._id_counter += 1
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self._attendees = []  # Private attribute for the list of attendees

    def add_attendee(self, attendee_name):
        self._attendees.append(attendee_name)
        print(f"Added attendee: {attendee_name} to event: {self.name}")

    def remove_attendee(self, attendee_name):
        if attendee_name in self._attendees:
            self._attendees.remove(attendee_name)
            print(f"Removed attendee: {attendee_name} from event: {self.name}")
        else:
            print(f"Attendee: {attendee_name} not found in event: {self.name}")

    def get_total_attendees(self):
        return len(self._attendees)

    def get_id(self):
        return self._id

    def __str__(self):
        return f"Event '{self.name}' on {self.date} at {self.time} in {self.location} with {self.get_total_attendees()} attendees."


class PrivateEvent(Event):
    def __init__(self, name, date, time, location, invite_only=True):
        super().__init__(name, date, time, location)
        self.invite_only = invite_only

    def __str__(self):
        invite_str = " (Invite Only)" if self.invite_only else ""
        return super().__str__() + invite_str


class PublicEvent(Event):
    def __init__(self, name, date, time, location, max_capacity):
        super().__init__(name, date, time, location)
        self.max_capacity = max_capacity

    def add_attendee(self, attendee_name):
        if self.get_total_attendees() < self.max_capacity:
            super().add_attendee(attendee_name)
        else:
            print(f"Cannot add attendee: {attendee_name}. Event: {self.name} has reached its maximum capacity of {self.max_capacity}.")

    def __str__(self):
        return super().__str__() + f" (Max Capacity: {self.max_capacity})"


class EventManager:
    def __init__(self):
        self.events = []

    def create_event(self, event):
        self.events.append(event)
        print(f"Created: {event}")

    def add_attendee(self, event_id, attendee_name):
        for event in self.events:
            if event.get_id() == event_id:
                event.add_attendee(attendee_name)
                return
        print(f"Event with ID {event_id} not found.")

    def remove_attendee(self, event_id, attendee_name):
        for event in self.events:
            if event.get_id() == event_id:
                event.remove_attendee(attendee_name)
                return
        print(f"Event with ID {event_id} not found.")

    def display_events(self):
        print("Events:")
        for event in self.events:
            print(event)


# Testing the Event Management System

# Create the event manager
event_manager = EventManager()

# Create events
private_event = PrivateEvent(name="Birthday Party", date="2024-08-01", time="18:00", location="John's House")
public_event = PublicEvent(name="Concert", date="2024-08-05", time="20:00", location="City Park", max_capacity=100)
event_manager.create_event(private_event)
event_manager.create_event(public_event)

# Display events
event_manager.display_events()

# Add and manage attendees
event_manager.add_attendee(private_event.get_id(), "Alice")
event_manager.add_attendee(private_event.get_id(), "Bob")
event_manager.add_attendee(public_event.get_id(), "Charlie")
event_manager.add_attendee(public_event.get_id(), "Dave")

# Trying to add more attendees beyond the max capacity
for i in range(101):
    event_manager.add_attendee(public_event.get_id(), f"Attendee{i+1}")

# Remove attendees
event_manager.remove_attendee(private_event.get_id(), "Bob")
event_manager.remove_attendee(public_event.get_id(), "Dave")

# Display events after updates
event_manager.display_events()

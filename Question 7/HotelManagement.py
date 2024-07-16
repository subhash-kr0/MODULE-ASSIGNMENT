class Room:
    _id_counter = 1  # Class-level attribute to generate unique IDs
    
    def __init__(self, room_number, room_type, rate):
        self._id = Room._id_counter  # Unique ID
        Room._id_counter += 1
        self.room_number = room_number
        self.room_type = room_type
        self.rate = rate
        self._is_available = True  # Private attribute for availability

    def book_room(self):
        if self._is_available:
            self._is_available = False
            print(f"Room {self.room_number} is booked.")
        else:
            print(f"Room {self.room_number} is already booked.")

    def check_in(self):
        if not self._is_available:
            print(f"Room {self.room_number} is now occupied.")
        else:
            print(f"Room {self.room_number} is not booked yet.")

    def check_out(self):
        if not self._is_available:
            self._is_available = True
            print(f"Room {self.room_number} is now available.")
        else:
            print(f"Room {self.room_number} is already available.")

    def get_availability(self):
        return self._is_available

    def get_id(self):
        return self._id

    def __str__(self):
        availability = "Available" if self._is_available else "Occupied"
        return f"Room {self.room_number} ({self.room_type}): ${self.rate:.2f} per night - {availability}"


class SuiteRoom(Room):
    def __init__(self, room_number, rate, has_living_room=True):
        super().__init__(room_number, "Suite", rate)
        self.has_living_room = has_living_room

    def __str__(self):
        living_room_str = " with Living Room" if self.has_living_room else ""
        return super().__str__() + living_room_str


class StandardRoom(Room):
    def __init__(self, room_number, rate, has_double_bed=True):
        super().__init__(room_number, "Standard", rate)
        self.has_double_bed = has_double_bed

    def __str__(self):
        bed_str = " with Double Bed" if self.has_double_bed else " with Single Bed"
        return super().__str__() + bed_str


class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)
        print(f"Added: {room}")

    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                room.book_room()
                return
        print(f"Room {room_number} not found.")

    def check_in(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                room.check_in()
                return
        print(f"Room {room_number} not found.")

    def check_out(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                room.check_out()
                return
        print(f"Room {room_number} not found.")

    def display_rooms(self):
        print("Rooms:")
        for room in self.rooms:
            print(room)


# Testing the Hotel Management System

# Create the hotel
hotel = Hotel()

# Add rooms
suite1 = SuiteRoom(room_number=101, rate=200.00, has_living_room=True)
standard1 = StandardRoom(room_number=102, rate=100.00, has_double_bed=True)
standard2 = StandardRoom(room_number=103, rate=90.00, has_double_bed=False)
hotel.add_room(suite1)
hotel.add_room(standard1)
hotel.add_room(standard2)

# Display rooms
hotel.display_rooms()

# Book and manage rooms
hotel.book_room(101)
hotel.check_in(101)
hotel.check_out(101)
hotel.book_room(102)
hotel.book_room(102)  # Try booking an already booked room
hotel.check_out(102)

# Display rooms after updates
hotel.display_rooms()

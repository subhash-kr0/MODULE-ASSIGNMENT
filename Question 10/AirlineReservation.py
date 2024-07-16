class Flight:
    _id_counter = 1  # Class-level attribute to generate unique IDs

    def __init__(self, flight_number, departure_airport, arrival_airport, departure_time, arrival_time, available_seats):
        self._id = Flight._id_counter  # Unique ID
        Flight._id_counter += 1
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self._available_seats = available_seats  # Private attribute for available seats
        self._reserved_seats = 0  # Private attribute for reserved seats

    def book_seat(self):
        if self._available_seats > 0:
            self._available_seats -= 1
            self._reserved_seats += 1
            print(f"Seat booked on flight {self.flight_number}.")
        else:
            print(f"No available seats on flight {self.flight_number}.")

    def cancel_reservation(self):
        if self._reserved_seats > 0:
            self._available_seats += 1
            self._reserved_seats -= 1
            print(f"Reservation cancelled on flight {self.flight_number}.")
        else:
            print(f"No reservations to cancel on flight {self.flight_number}.")

    def get_remaining_seats(self):
        return self._available_seats

    def get_id(self):
        return self._id

    def __str__(self):
        return f"Flight {self.flight_number} from {self.departure_airport} to {self.arrival_airport}, departs at {self.departure_time}, arrives at {self.arrival_time}, available seats: {self._available_seats}"


class DomesticFlight(Flight):
    def __init__(self, flight_number, departure_airport, arrival_airport, departure_time, arrival_time, available_seats, in_flight_meal=False):
        super().__init__(flight_number, departure_airport, arrival_airport, departure_time, arrival_time, available_seats)
        self.in_flight_meal = in_flight_meal

    def __str__(self):
        meal_str = "with in-flight meal" if self.in_flight_meal else "without in-flight meal"
        return super().__str__() + f", {meal_str}"


class InternationalFlight(Flight):
    def __init__(self, flight_number, departure_airport, arrival_airport, departure_time, arrival_time, available_seats, visa_required=True):
        super().__init__(flight_number, departure_airport, arrival_airport, departure_time, arrival_time, available_seats)
        self.visa_required = visa_required

    def __str__(self):
        visa_str = "Visa required" if self.visa_required else "No visa required"
        return super().__str__() + f", {visa_str}"


class AirlineReservationSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)
        print(f"Added: {flight}")

    def book_seat(self, flight_id):
        for flight in self.flights:
            if flight.get_id() == flight_id:
                flight.book_seat()
                return
        print(f"Flight with ID {flight_id} not found.")

    def cancel_reservation(self, flight_id):
        for flight in self.flights:
            if flight.get_id() == flight_id:
                flight.cancel_reservation()
                return
        print(f"Flight with ID {flight_id} not found.")

    def display_flights(self):
        print("Flights:")
        for flight in self.flights:
            print(flight)


# Testing the Airline Reservation System

# Create the airline reservation system
airline_system = AirlineReservationSystem()

# Create flights
domestic_flight = DomesticFlight(flight_number="DL123", departure_airport="JFK", arrival_airport="LAX", departure_time="08:00", arrival_time="11:00", available_seats=150, in_flight_meal=True)
international_flight = InternationalFlight(flight_number="AF456", departure_airport="JFK", arrival_airport="CDG", departure_time="18:00", arrival_time="06:00", available_seats=200, visa_required=True)
airline_system.add_flight(domestic_flight)
airline_system.add_flight(international_flight)

# Display flights
airline_system.display_flights()

# Book and manage seats
airline_system.book_seat(domestic_flight.get_id())
airline_system.book_seat(international_flight.get_id())
airline_system.book_seat(international_flight.get_id())  # Book another seat on the same flight

# Cancel reservations
airline_system.cancel_reservation(domestic_flight.get_id())
airline_system.cancel_reservation(international_flight.get_id())

# Display flights after updates
airline_system.display_flights()

from flight_booking import FlightBooking
from hotel_reservation import HotelReservation
from car_rental import CarRental

# Facade for travel booking that simplifies interaction with multiple subsystems

class TravelBookingFacade:
    def __init__(self):
        self.flight_booking = FlightBooking()
        self.hotel_reservation = HotelReservation()
        self.car_rental = CarRental()

    def book_trip(self, trip_details):
        print("Starting the trip booking process...\n")

        # Step 1: Book Flight
        self.flight_booking.search(trip_details['origin'], trip_details['destination'], trip_details['date'])
        self.flight_booking.book(trip_details['flight_id'])
        
        # Step 2: Book Hotel
        self.hotel_reservation.search(trip_details['city'], trip_details['check_in_date'], trip_details['check_out_date'])
        self.hotel_reservation.book(trip_details['hotel_id'])
        
        # Step 3: Book Car
        self.car_rental.search(trip_details['city'], trip_details['from_date'], trip_details['to_date'])
        self.car_rental.book(trip_details['car_id'])

        print("\nTrip booking completed!")

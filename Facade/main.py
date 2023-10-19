from travel_booking_facade import TravelBookingFacade

def main():
    # Sample trip details
    trip_details = {
        'origin': 'New York',
        'destination': 'Los Angeles',
        'date': '2023-11-05',
        'flight_id': 'FL123',
        'city': 'Los Angeles',
        'check_in_date': '2023-11-05',
        'check_out_date': '2023-11-10',
        'hotel_id': 'HT789',
        'from_date': '2023-11-05',
        'to_date': '2023-11-10',
        'car_id': 'CR456'
    }

    # Create an instance of the facade
    travel_facade = TravelBookingFacade()

    # Use the facade to book the trip
    travel_facade.book_trip(trip_details)

if __name__ == "__main__":
    main()

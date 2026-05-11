class FlightData:
    def __init__(self, price, origin, destination, out_date, return_date):
        self.price = price
        self.origin = origin
        self.destination = destination
        self.out_date = out_date
        self.return_date = return_date

    def find_cheapest_flight(self, all_flights):
        if not all_flights:
            print("No flight data")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
        first_flight = all_flights[0]
        lowest_price = first_flight["price"]
        origin = first_flight["flights"][0]["departure_airport"]["id"]
        destination = first_flight["flights"][-1]["arrival_airport"]["id"]
        out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
        return_date = first_flight["flights"][0]["arrival_airport"]["time"].split(" ")[0]
        cheapest_flight = (lowest_price, origin, destination, out_date, return_date)

        for flight in all_flights:
            try:
                price = flight.get('price')
            except KeyError:
                print("No price available for flight.")
                continue
            if price < lowest_price:
                lowest_price = price
                origin = flight["flights"][0]["departure_airport"]["id"]
                destination = flight["flights"][0]["arrival_airport"]["id"]
                out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
                return_date = flight["flights"][0]["arrival_airport"]["time"].split(" ")[0]
                cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

        return cheapest_flight

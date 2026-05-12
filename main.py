from dotenv import load_dotenv
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch
from flight_data import FlightData

load_dotenv()

dataManager = DataManager()
flightSearcher = FlightSearch()
notificationManager = NotificationManager()

departure_id = input("Departing airport IATA Code: ")
sheet_data = dataManager.get_data()

for ticket in sheet_data['tickets']:
    print(f"Searching for flight from {departure_id} to {ticket['iataCode']}")
    out_date = input("When do you plan to depart? (YYYY-MM-DD) ")
    return_date = input("When do you plan to return? (YYYY-MM-DD) ")
    flight_data = FlightData(ticket.get('lowestPrice'), departure_id, ticket.get('iataCode'), out_date, return_date)
    flights = flightSearcher.search_flight(departure_id, ticket.get('iataCode'), out_date, return_date)
    cheapest_flight = flight_data.find_cheapest_flight(flights)
    if cheapest_flight.price < ticket['lowestPrice'] and cheapest_flight.price != 'N/A':
        print(f'Lower price found to {ticket['city']}')
        print(f'R${cheapest_flight.price}')
        dataManager.update_data(ticket['id'], cheapest_flight.price)
        notificationManager.send_msg(cheapest_flight)
    print("-------------------")
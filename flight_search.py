import os
from dotenv import load_dotenv
from requests_cache import CachedSession

load_dotenv()
class FlightSearch:
    def __init__(self):
        self.url = os.getenv('SERPAPI_URL')
        self.session = CachedSession('flight_search_cache')

    def search_flight(self, departure_id, arrival_id,out_date, return_date):
        search_params = {
            'engine' : 'google_flights',
            'api_key' : os.getenv('SERPAPI_API_KEY'),
            'departure_id' : departure_id,
            'arrival_id' : arrival_id,
            'outbound_date' : out_date,
            'return_date' : return_date,
            'gl' : 'br',
            'hl' : 'pt-br',
            'currency' : 'BRL',
        }

        res = self.session.get(url = self.url, params = search_params)
        data = res.json()
        all_flights = data['best_flights'] + data['other_flights']
        return all_flights
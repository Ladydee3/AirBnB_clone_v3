#!/usr/bin/python3
""" place view """
from flask import Flask, jsonify, request, abort
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)

@app.route('/api/v1/places_search', methods=['POST'])
def search_places():
    if not request.is_json:
        abort(400, description="Not a JSON")
    
    search_criteria = request.get_json()
    
    if not search_criteria:
        places = storage.all(Place).values()
        return jsonify([place.to_dict() for place in places])
    
    states = search_criteria.get('states', [])
    cities = search_criteria.get('cities', [])
    amenities = search_criteria.get('amenities', [])
    
    places = set()
    
    if states:
        for state_id in states:
            state = storage.get(State, state_id)
            if state:
                for city in state.cities:
                    for place in city.places:
                        places.add(place)
    
    if cities:
        for city_id in cities:
            city = storage.get(City, city_id)
            if city:
                for place in city.places:
                    places.add(place)
    
    if not states and not cities:
        places = storage.all(Place).values()
    
    if amenities:
        amenities_set = set(amenities)
        filtered_places = []
        for place in places:
            place_amenities = {amenity.id for amenity in place.amenities}
            if amenities_set.issubset(place_amenities):
                filtered_places.append(place)
        places = filtered_places
    
    return jsonify([place.to_dict() for place in places])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


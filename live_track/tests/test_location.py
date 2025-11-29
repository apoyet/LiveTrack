from model.location import Location

def test_location_to_dict():
    loc = Location("Accor Arena", "Paris", "France")
    assert loc.to_dict() == {
        "venue": "Accor Arena",
        "city": "Paris",
        "country": "France"
    }

def test_location_from_dict():
    data = {"venue": "O2 Arena", "city": "London", "country": "UK"}
    loc = Location.from_dict(data)
    assert loc.city == "London"

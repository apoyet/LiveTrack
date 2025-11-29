from model.artist import Artist
from model.location import Location
from model.concert import Concert

def test_concert_serialization():
    artist = Artist("Metallica")
    loc = Location("Stade de France", "Paris", "France")
    c = Concert(artist, "2025-11-28", loc)

    d = c.to_dict()
    assert d["artist"]["name"] == "Metallica"
    assert d["location"]["city"] == "Paris"

def test_concert_deserialization():
    data = {
        "artist": {"name": "Muse"},
        "date": "2025-10-01",
        "location": {"venue": "O2", "city": "London", "country": "UK"}
    }
    c = Concert.from_dict(data)
    assert c.artist.name == "Muse"

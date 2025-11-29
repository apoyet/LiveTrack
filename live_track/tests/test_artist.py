from model.artist import Artist

def test_artist_to_dict():
    a = Artist("Daft Punk")
    assert a.to_dict() == {"name": "Daft Punk"}

def test_artist_from_dict():
    data = {"name": "Muse"}
    a = Artist.from_dict(data)
    assert a.name == "Muse"

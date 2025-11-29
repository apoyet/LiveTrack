import os
from model.concert_store import ConcertStore
from model.artist import Artist
from model.location import Location
from model.concert import Concert

def test_store_add_and_load(tmp_path):
    filename = tmp_path / "concerts.json"
    store = ConcertStore(filename=str(filename))

    c = Concert(
        Artist("Muse"),
        "2025-09-12",
        Location("O2", "London", "UK")
    )

    store.add_concert(c)

    # Reload
    store2 = ConcertStore(filename=str(filename))
    assert len(store2.concerts) == 1
    assert store2.concerts[0].artist.name == "Muse"

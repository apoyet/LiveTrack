from __future__ import annotations
from typing import Dict, Any
from model.artist import Artist
from model.location import Location

class Concert:
    """
    Represents a concert attended by the user.

    Parameters
    ----------
    artist : Artist
        Artist or band performing.
    date : str
        Date of the concert.
    location : Location
        Location object describing where the event took place.

    Attributes
    ----------
    artist : Artist
        Concert artist.
    date : str
        Concert date.
    location : Location
        Concert location.
    """

    def __init__(self, artist: Artist, date: str, location: Location) -> None:
        self.artist: Artist = artist
        self.date: str = date
        self.location: Location = location

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Concert object into a serializable dictionary.

        Returns
        -------
        dict
            Dictionary containing artist, date, and location.
        """
        return {
            "artist": self.artist.to_dict(),
            "date": self.date,
            "location": self.location.to_dict()
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Concert":
        """
        Create a Concert instance from a dictionary.

        Parameters
        ----------
        data : dict
            Dictionary representing a serialized concert.

        Returns
        -------
        Concert
        """
        artist = Artist.from_dict(data["artist"])
        location = Location.from_dict(data["location"])
        return Concert(artist=artist, date=data["date"], location=location)

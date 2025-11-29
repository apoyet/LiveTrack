from __future__ import annotations
from typing import Dict, Any, Optional

class Location:
    """
    Represents the location of a concert.

    Parameters
    ----------
    venue : str
        Name of the venue (e.g., 'Accor Arena').
    city : str
        City where the concert took place.
    country : str, optional
        Country of the concert (default: None).

    Attributes
    ----------
    venue : str
        Venue name.
    city : str
        City name.
    country : str or None
        Country name.
    """

    def __init__(self, venue: str, city: str, country: Optional[str] = None) -> None:
        self.venue: str = venue
        self.city: str = city
        self.country: Optional[str] = country

    def to_dict(self) -> Dict[str, Optional[str]]:
        """
        Convert the Location object into a serializable dictionary.

        Returns
        -------
        dict
            Dictionary containing `venue`, `city`, and `country`.
        """
        return {
            "venue": self.venue,
            "city": self.city,
            "country": self.country,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Location":
        """
        Create a Location instance from a dictionary.

        Parameters
        ----------
        data : dict
            Dictionary with location information.

        Returns
        -------
        Location
        """
        return Location(
            venue=data["venue"],
            city=data["city"],
            country=data.get("country"),
        )

from __future__ import annotations
from typing import Dict, Any

class Artist:
    """
    Represents a musical artist or band.

    Parameters
    ----------
    name : str
        Name of the artist or band.

    Attributes
    ----------
    name : str
        Artist name.
    """

    def __init__(self, name: str) -> None:
        self.name: str = name

    def to_dict(self) -> Dict[str, str]:
        """
        Convert the Artist object into a serializable dictionary.

        Returns
        -------
        dict
            Dictionary containing `name`.
        """
        return {"name": self.name}

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Artist":
        """
        Create an Artist instance from a dictionary.

        Parameters
        ----------
        data : dict
            Dictionary containing an artist definition.

        Returns
        -------
        Artist
        """
        return Artist(name=data["name"])

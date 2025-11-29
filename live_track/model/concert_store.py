from __future__ import annotations
from typing import List
import json
from model.concert import Concert

class ConcertStore:
    """
    Stores and manages the list of concerts using a JSON file.

    Parameters
    ----------
    filename : str, optional
        JSON file used for persistence (default: 'concerts.json').

    Attributes
    ----------
    filename : str
        Path to the storage file.
    concerts : list of Concert
        Loaded concerts.
    """

    def __init__(self, filename: str = "concerts.json") -> None:
        self.filename: str = filename
        self.concerts: List[Concert] = self.load()

    def load(self) -> List[Concert]:
        """
        Load concerts from a JSON file.

        Returns
        -------
        list of Concert
        """
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [Concert.from_dict(c) for c in data]
        except FileNotFoundError:
            return []

    def save(self) -> None:
        """
        Save all concerts to the JSON file.

        Returns
        -------
        None
        """
        with open(self.filename, "w") as f:
            json.dump(
                [c.to_dict() for c in self.concerts],
                f,
                indent=4
            )

    def add_concert(self, concert: Concert) -> None:
        """
        Add a concert and save the updated list.

        Parameters
        ----------
        concert : Concert

        Returns
        -------
        None
        """
        self.concerts.append(concert)
        self.save()

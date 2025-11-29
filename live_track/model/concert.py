import datetime

class Concert:
    """
    Represents a concert attended by the user.

    Parameters
    ----------
    artist : str
        Name of the artist or band.
    date : str
        Date of the concert (free format, e.g., '2025-11-12').
    location : str
        Location of the concert (venue, city, country, etc.).

    Attributes
    ----------
    artist : str
        Artist name.
    date : str
        Concert date.
    location : str
        Concert location.
    """

    def __init__(self, artist: str, date: datetime.date, location: str):
        self.artist = artist
        self.date = date
        self.location = location

    def to_dict(self) -> dict:
        """
        Convert the Concert object into a serializable dictionary.

        Returns
        -------
        dict
            Dictionary containing `artist`, `date`, and `location`.
        """
        return {
            "artist": self.artist,
            "date": self.date,
            "location": self.location}

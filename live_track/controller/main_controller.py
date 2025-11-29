from __future__ import annotations
from typing import TYPE_CHECKING
from model.artist import Artist
from model.location import Location
from model.concert import Concert

if TYPE_CHECKING:
    from view.main_view import MainView
    from model.concert_store import ConcertStore


class MainController:
    """
    Main controller connecting the view and the model.

    Parameters
    ----------
    view : MainView
        The Tkinter GUI responsible for user interaction.
    store : ConcertStore
        Data storage layer for concert persistence.
    """

    def __init__(self, view: "MainView", store: "ConcertStore") -> None:
        self.view: MainView = view
        self.store: ConcertStore = store

        self.view.add_button.config(command=self.add_concert)
        self.refresh_list()

    def add_concert(self) -> None:
        """
        Read user input, create domain objects (Artist, Location, Concert),
        store them, and refresh the displayed list.

        Returns
        -------
        None
        """
        artist_name = self.view.artist_entry.get()
        venue = self.view.venue_entry.get()
        city = self.view.city_entry.get()
        country = self.view.country_entry.get()
        date = self.view.date_entry.get()

        artist = Artist(name=artist_name)
        location = Location(venue=venue, city=city, country=country or None)
        concert = Concert(artist=artist, date=date, location=location)

        self.store.add_concert(concert)
        self.refresh_list()
        self.view.clear_form()

    def refresh_list(self) -> None:
        """
        Refresh the GUI listbox with all stored concerts.

        Returns
        -------
        None
        """
        self.view.concert_list.delete(0, "end")
        for c in self.store.concerts:
            display = (
                f"{c.date} — {c.artist.name} — "
                f"{c.location.venue}, {c.location.city}"
                f"{' (' + c.location.country + ')' if c.location.country else ''}"
            )
            self.view.concert_list.insert("end", display)

from __future__ import annotations
from typing import Any
import tkinter as tk
from tkinter import ttk


class MainView(tk.Frame):
    """
    Tkinter graphical interface for the Concert Tracker application.
    """

    def __init__(self, master: Any = None) -> None:
        super().__init__(master)
        self.master = master

        self.master.title("Concert Tracker")
        self.pack(fill="both", expand=True)

        # Labels + Entries
        self.artist_label = ttk.Label(self, text="Artist:")
        self.artist_entry = ttk.Entry(self)

        self.venue_label = ttk.Label(self, text="Venue:")
        self.venue_entry = ttk.Entry(self)

        self.city_label = ttk.Label(self, text="City:")
        self.city_entry = ttk.Entry(self)

        self.country_label = ttk.Label(self, text="Country:")
        self.country_entry = ttk.Entry(self)

        self.date_label = ttk.Label(self, text="Date:")
        self.date_entry = ttk.Entry(self)

        # Button
        self.add_button = ttk.Button(self, text="Add Concert")

        # Listbox
        self.concert_list = tk.Listbox(self, height=12, width=60)

        self._place_widgets()

    def _place_widgets(self) -> None:
        """
        Position all GUI components using the Tkinter grid manager.

        Returns
        -------
        None
        """
        self.artist_label.grid(row=0, column=0, sticky="e")
        self.artist_entry.grid(row=0, column=1)

        self.venue_label.grid(row=1, column=0, sticky="e")
        self.venue_entry.grid(row=1, column=1)

        self.city_label.grid(row=2, column=0, sticky="e")
        self.city_entry.grid(row=2, column=1)

        self.country_label.grid(row=3, column=0, sticky="e")
        self.country_entry.grid(row=3, column=1)

        self.date_label.grid(row=4, column=0, sticky="e")
        self.date_entry.grid(row=4, column=1)

        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.concert_list.grid(row=6, column=0, columnspan=2, pady=10)

    def clear_form(self) -> None:
        """
        Reset all text entry fields after a concert is added.

        Returns
        -------
        None
        """
        self.artist_entry.delete(0, "end")
        self.venue_entry.delete(0, "end")
        self.city_entry.delete(0, "end")
        self.country_entry.delete(0, "end")
        self.date_entry.delete(0, "end")

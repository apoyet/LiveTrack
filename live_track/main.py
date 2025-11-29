from __future__ import annotations
import tkinter as tk

from model.concert_store import ConcertStore
from view.main_view import MainView
from controller.main_controller import MainController


def main() -> None:
    """
    Entry point of the Concert Tracker application.

    Returns
    -------
    None
    """
    root = tk.Tk()

    view = MainView(master=root)
    store = ConcertStore()
    MainController(view=view, store=store)

    root.mainloop()


if __name__ == "__main__":
    main()

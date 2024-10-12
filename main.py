import tkinter as tk
from tkinter import filedialog
from library import Library
from reader import Reader

class EPUBReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EPUB Reader")
        self.root.geometry("1920x1080")

        # Library view (for file selection)
        self.library = Library(self)
        self.reader = None

        self.show_library()

    def show_library(self):
        """ Show the library view for loading EPUB files. """
        self.library.pack(fill="both", expand=True)

    def open_reader(self, epub_file):
        """ Show the reader view with the selected EPUB file. """
        if self.reader is not None:
            self.reader.destroy()  # Close the previous reader if open

        self.reader = Reader(self, epub_file)
        self.reader.pack(fill="both", expand=True)

        self.library.pack_forget()  # Hide the library view

if __name__ == "__main__":
    root = tk.Tk()
    app = EPUBReaderApp(root)
    root.mainloop()

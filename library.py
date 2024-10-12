import tkinter as tk
from tkinter import filedialog

class Library(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app

        # Create Open button to load EPUB files
        self.open_button = tk.Button(self, text="Open EPUB File", command=self.open_epub)
        self.open_button.pack(pady=20)

    def open_epub(self):
        """ Opens a file dialog to select EPUB files. """
        epub_file = filedialog.askopenfilename(
            title="Open EPUB File", 
            filetypes=(("EPUB files", "*.epub"),)
        )
        if epub_file:
            self.app.open_reader(epub_file)

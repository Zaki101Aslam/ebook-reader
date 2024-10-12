import tkinter as tk
import fitz  # PyMuPDF

class Reader(tk.Frame):
    def __init__(self, app, epub_file):
        super().__init__(app.root)
        self.app = app
        self.epub_file = epub_file
        self.current_page = 0

        # Set up layout: Page content display and control buttons
        self.content_text = tk.Text(self, wrap=tk.WORD)
        self.content_text.pack(fill="both", expand=True, padx=20, pady=20)

        self.load_epub()

        # Navigation buttons
        self.prev_button = tk.Button(self, text="Previous", command=self.prev_page)
        self.prev_button.pack(side="left", padx=10, pady=10)

        self.next_button = tk.Button(self, text="Next", command=self.next_page)
        self.next_button.pack(side="right", padx=10, pady=10)

    def load_epub(self):
        """ Loads the EPUB file and displays the content of the first page. """
        self.doc = fitz.open(self.epub_file)  # Open the EPUB file with PyMuPDF
        self.show_page(self.current_page)

    def show_page(self, page_num):
        """ Displays the content of the selected page. """
        if page_num < 0 or page_num >= self.doc.page_count:
            return  # Avoid out-of-bounds pages

        page = self.doc.load_page(page_num)
        text = page.get_text("text")  # Extract page text
        self.content_text.delete(1.0, tk.END)  # Clear previous text
        self.content_text.insert(tk.END, text)  # Insert new text

    def next_page(self):
        """ Go to the next page. """
        if self.current_page < self.doc.page_count - 1:
            self.current_page += 1
            self.show_page(self.current_page)

    def prev_page(self):
        """ Go to the previous page. """
        if self.current_page > 0:
            self.current_page -= 1
            self.show_page(self.current_page)

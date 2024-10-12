import tkinter as tk

class PageFlipAnimation:
    def __init__(self, reader):
        self.reader = reader  # Reference to the reader (main application)
    
    def flip_page(self, forward=True):
        """ Simulate a page flip effect when navigating pages. """
        # Create a temporary canvas overlay for the animation
        canvas = tk.Canvas(self.reader, width=self.reader.winfo_width(), height=self.reader.winfo_height())
        canvas.place(x=0, y=0)
        
        # Define animation settings (adjust speed by changing range and delay)
        if forward:
            for i in range(100, -1, -10):  # Page flip forward effect
                canvas.delete("all")
                canvas.create_rectangle(i, 0, self.reader.winfo_width(), self.reader.winfo_height(), fill="gray")
                canvas.update()
                canvas.after(20)  # Delay between steps
        else:
            for i in range(0, 101, 10):  # Page flip backward effect
                canvas.delete("all")
                canvas.create_rectangle(i, 0, self.reader.winfo_width(), self.reader.winfo_height(), fill="gray")
                canvas.update()
                canvas.after(20)
        
        # Remove canvas once the animation is complete
        canvas.destroy()

# Example of how to use this in your reader.py file:
# In the Reader class, initialize an instance of PageFlipAnimation:
#
# self.animator = PageFlipAnimation(self)
#
# And call it in your next_page() and prev_page() methods like so:
#
# def next_page(self):
#     self.animator.flip_page(forward=True)
#     if self.current_page < self.doc.page_count - 1:
#         self.current_page += 1
#         self.show_page(self.current_page)
#
# def prev_page(self):
#     self.animator.flip_page(forward=False)
#     if self.current_page > 0:
#         self.current_page -= 1
#         self.show_page(self.current_page)

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Foodie App")
        self.geometry("400x700")

        # Create the header with navigation buttons
        self.header = tk.Frame(self, bg="lightblue", height=50)
        self.header.pack(fill="x", side="top")

        self.home_button = tk.Button(self.header, text="Home", command=self.show_home)
        self.home_button.pack(side="left", padx=10, pady=10)

        self.message_button = tk.Button(self.header, text="Message", command=self.show_message)
        self.message_button.pack(side="left", padx=10, pady=10)

        self.me_button = tk.Button(self.header, text="Me", command=self.show_me)
        self.me_button.pack(side="left", padx=10, pady=10)

        # Create a container for switching between frames
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Dictionary to store the pages
        self.pages = {}

        # Add pages to the dictionary
        for Page in (HomePage, MessagePage, MePage, RestaurantDetailPage, OptionDetailPage):
            page_name = Page.__name__
            page = Page(parent=self.container, controller=self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky="nsew")

        # Show the home page initially
        self.show_home()

    def show_home(self):
        self.pages["HomePage"].tkraise()

    def show_message(self):
        self.pages["MessagePage"].tkraise()

    def show_me(self):
        self.pages["MePage"].tkraise()

    def show_restaurant_detail(self, restaurant_name):
        self.pages["RestaurantDetailPage"].set_restaurant(restaurant_name)
        self.pages["RestaurantDetailPage"].tkraise()

    def show_option_detail(self, option_text):
        self.pages["OptionDetailPage"].set_option(option_text)
        self.pages["OptionDetailPage"].tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Create content for the Home page
        tk.Label(self, text="Home Page", font=("Helvetica", 18)).pack(pady=10)
        tk.Label(self, text="Find delicious food options here", font=("Helvetica", 14)).pack()

        # Add a placeholder image (replace with an actual image)
        canvas = tk.Canvas(self, width=300, height=200)
        canvas.pack(pady=10)
        canvas.create_rectangle(50, 50, 250, 150, fill="gray")  # Placeholder for image

        # Display restaurant list
        self.restaurant_list = [
            {"name": "Thai Spice", "rating": 3.5, "distance": "8.9 km"},
            {"name": "Sushi Master", "rating": 4.8, "distance": "3.2 km"},
            {"name": "Pizza Palace", "rating": 4.2, "distance": "5.4 km"}
        ]

        for restaurant in self.restaurant_list:
            self.create_restaurant_button(restaurant)

    def create_restaurant_button(self, restaurant):
        button = ttk.Button(self, text=f"{restaurant['name']} - {restaurant['rating']}⭐ - {restaurant['distance']}",
                            command=lambda: self.controller.show_restaurant_detail(restaurant['name']))
        button.pack(pady=5, fill="x")

class RestaurantDetailPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.restaurant_name = tk.StringVar()

        # Restaurant name label
        self.restaurant_label = tk.Label(self, textvariable=self.restaurant_name, font=("Helvetica", 18))
        self.restaurant_label.pack(pady=10)

        # Sample menu items
        self.menu_items = [
            {"name": "Pad Thai", "price": 12},
            {"name": "Green Curry", "price": 10},
            {"name": "Spring Rolls", "price": 5}
        ]

        # Display menu items
        self.menu_frame = tk.Frame(self)
        self.menu_frame.pack()

        self.create_menu_items()

        # Back button to return to home page
        back_button = ttk.Button(self, text="Back", command=self.controller.show_home)
        back_button.pack(pady=20)

    def create_menu_items(self):
        for item in self.menu_items:
            label = tk.Label(self.menu_frame, text=f"{item['name']} - ${item['price']}")
            label.pack(pady=5)

    def set_restaurant(self, name):
        self.restaurant_name.set(name)

class MessagePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Title label for Message page
        tk.Label(self, text="Messages", font=("Helvetica", 18)).pack(pady=10)

        # Create a text box to simulate a chat interface
        chat_box = tk.Text(self, wrap="word", bg="#f0f0f0", font=("Helvetica", 12), height=25, width=50)
        chat_box.pack(padx=10, pady=10)

        # Simulate chat content
        chat_box.insert("end", "Customer service: Hi there! How can I help you today?\n")
        chat_box.insert("end", "\n")
        chat_box.insert("end", "Customer: I'm looking for a Thai restaurant near my office.\n")
        chat_box.insert("end", "\n")
        chat_box.insert("end", "Searching for Thai food\n")
        chat_box.insert("end", "\n")
        chat_box.insert("end", "Customer service: There is one opposite your office.\n")
        chat_box.insert("end", "Customer: Thank you.\n")

        # Disable the chat box so users cannot edit it
        chat_box.config(state="disabled")

class MePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="My Profile", font=("Helvetica", 18)).pack(pady=10)

        # Create options
        options = {
            "History": "No history",
            "Locations": "No locations saved",
            "Payment Method": "Credit Card: xxxx1357",
            "Invite Friend": "You have one friend",
            "Contact": "12345678"
        }
        for option in options:
            button = ttk.Button(self, text=option, command=lambda opt=option: self.controller.show_option_detail(options[opt]))
            button.pack(pady=5, fill="x")

class OptionDetailPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.option_text = tk.StringVar()

        # Display the selected option's information
        self.option_label = tk.Label(self, textvariable=self.option_text, font=("Helvetica", 18))
        self.option_label.pack(pady=20)

        # Back button to return to the Me page
        back_button = ttk.Button(self, text="Back", command=self.controller.show_me)
        back_button.pack(pady=20)

    def set_option(self, option_text):
        self.option_text.set(option_text)

if __name__ == "__main__":
    app = App()
    app.mainloop()

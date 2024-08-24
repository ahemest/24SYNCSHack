import tkinter as tk
from tkinter import ttk

class FoodApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Restaurant Finder")
        self.geometry("400x600")

        # Create the main container frame
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Create a dictionary to hold the different pages
        self.frames = {}

        # Add both the HomePage and RestaurantDetailPage to the frames dictionary
        for F in (HomePage, RestaurantDetailPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the home page initially
        self.show_frame("HomePage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()

    def show_restaurant_detail(self, restaurant_info):
        """Show the restaurant detail page with the provided restaurant info"""
        detail_page = self.frames["RestaurantDetailPage"]
        detail_page.display_restaurant_info(restaurant_info)
        self.show_frame("RestaurantDetailPage")


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Title for the home page
        tk.Label(self, text="Restaurants Nearby", font=("Helvetica", 18)).pack(pady=10)

        # Sample restaurant list
        restaurants = [
            {"name": "Thai Spice", "rating": 3.5, "distance": "8.9 km"},
            {"name": "Sushi Master", "rating": 4.8, "distance": "3.2 km"},
            {"name": "Pizza Palace", "rating": 4.2, "distance": "5.4 km"}
        ]

        # Create buttons for each restaurant
        for restaurant in restaurants:
            button_text = f"{restaurant['name']} - {restaurant['rating']}⭐ - {restaurant['distance']}"
            button = ttk.Button(self, text=button_text, command=lambda r=restaurant: self.controller.show_restaurant_detail(r))
            button.pack(pady=5, fill="x")


class RestaurantDetailPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Restaurant name label
        self.restaurant_name_label = tk.Label(self, text="", font=("Helvetica", 18))
        self.restaurant_name_label.pack(pady=10)

        # Restaurant details placeholder
        self.details_label = tk.Label(self, text="", font=("Helvetica", 14))
        self.details_label.pack(pady=5)

        # Back button to return to the home page
        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=20)

    def display_restaurant_info(self, restaurant_info):
        """Update the restaurant details based on the selected restaurant"""
        name = restaurant_info["name"]
        rating = restaurant_info["rating"]
        distance = restaurant_info["distance"]

        self.restaurant_name_label.config(text=name)
        self.details_label.config(text=f"Rating: {rating}⭐\nDistance: {distance}")


if __name__ == "__main__":
    app = FoodApp()
    app.mainloop()

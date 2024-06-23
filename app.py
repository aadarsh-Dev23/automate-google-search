import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

# Define the path to the chromedriver executable
CHROMEDRIVER_PATH = r"C:\Users\aadar\Downloads\influx_test\chromedriver.exe"

# Function to perform the search
def perform_search():
    search_query = search_entry.get()
    
    # Check if the chromedriver executable exists
    if not os.path.exists(CHROMEDRIVER_PATH):
        print(f"Error: Chromedriver not found at {CHROMEDRIVER_PATH}")
        return

    # Create a Service object with the chromedriver path
    service = Service(CHROMEDRIVER_PATH)
    
    # Initialize the Chrome webdriver with the service object
    try:
        driver = webdriver.Chrome(service=service)
    except Exception as e:
        print(f"Error initializing the Chrome driver: {e}")
        return

    try:
        # Perform search operation
        driver.get("http://www.google.com")
        search_box = driver.find_element(By.NAME, "q")  # Google search box
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        
        # Optionally, wait for some time to view the results
        time.sleep(30)  # Adjust the wait time as needed
        
    except Exception as e:
        print(f"Error during search operation: {e}")
    finally:
        # Close the driver after a short wait
        driver.quit()

# Initialize the GUI application
root = tk.Tk()
root.title("Search Application")

# Add entry widget for search query
search_entry = tk.Entry(root, width=50)
search_entry.pack(pady=10)

# Add a button to perform the search
search_button = tk.Button(root, text="Search", command=perform_search)
search_button.pack(pady=10)

root.mainloop()

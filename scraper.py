import requests
from bs4 import BeautifulSoup
import tkinter as tk

def scrape_website():
    # Get the URL from the input field
    url = url_entry.get()

    # Send a GET request to the website
    response = requests.get(url)

    # Create a BeautifulSoup object by passing the response content and a parser (e.g., 'html.parser')
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find specific elements on the webpage using BeautifulSoup's selectors
    # For example, let's find all the links (anchor tags) on the page
    links = soup.find_all('a')

    # Clear the result text widget
    result_text.delete('1.0', tk.END)

    # Iterate over the found links and append their text and URLs to the result text widget
    for link in links:
        link_text = link.text.strip()
        link_url = link['href']
        result_text.insert(tk.END, f"Link Text: {link_text}\n")
        result_text.insert(tk.END, f"Link URL: {link_url}\n")
        result_text.insert(tk.END, "-------------------\n")

# Create the main window
window = tk.Tk()
window.title("Web Scraper")

# Create a label and an entry field for the URL
url_label = tk.Label(window, text="URL:")
url_label.pack()

url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Create a button to initiate the web scraping
scrape_button = tk.Button(window, text="Scrape", command=scrape_website)
scrape_button.pack()

# Create a text widget to display the scraped results
result_text = tk.Text(window, width=80, height=20)
result_text.pack()

# Start the GUI main loop
window.mainloop()
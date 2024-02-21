# This is a sample Python script.

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import time
import webbrowser


def open_url(url):
    """Opens a given URL in the default web browser."""
    try:
        webbrowser.open(url, new=2)  # new=2 opens in a new tab, if possible
        print(f"Opened {url} in web browser")
    except Exception as e:
        print(f"Error opening {url}: {e}")


def schedule_link_opening(urls, days):
    """Schedules opening of URLs in a web browser once a day for a given number of days."""
    for day in range(days):
        print(f"Day {day + 1}/{days}")
        for url in urls:
            open_url(url)
        if day < days - 1:  # Wait until the next day if it's not the last day
            time.sleep(86400)  # Wait for 24 hours


def main():
    urls_input = input("Enter URLs separated by space: ")
    urls = urls_input.split()
    days = int(input("Enter the number of days: "))

    schedule_link_opening(urls, days)


if __name__ == "__main__":
    main()


# Import pytube
from pytube import YouTube

# URL input
URL = input("Enter your URL: ")

# Create YouTube Object
yt = YouTube(URL)

# Select quality
stream = yt.streams.get_highest_resolution()

# Download
stream.download()

# Print data
print("Download completed")
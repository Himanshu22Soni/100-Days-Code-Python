# Command Line Utility in python.

from pytube import YouTube


def Download(link, save_path, filename):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(save_path, filename=filename)
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
save_path = input("Enter the directory to save the video: ")
filename = input("Enter the filename: ")
Download(link, save_path, filename)

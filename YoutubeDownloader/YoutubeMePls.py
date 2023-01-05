from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Error in downloading youtube video")
    print("Download has completed!")

link = input("Put your youtube link here!! URL: ")
Download(link)
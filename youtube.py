import youtube_dl

# options = {
#     'format': 'bestaudio/best',  # choice of quality
#     'extractaudio': True,        # only keep the audio
#     'audioformat': "mp3",        # convert to mp3
#     'outtmpl': '%(id)s',         # name the file the ID of the video
#     'noplaylist': True,          # only download single song, not playlist
#     'listformats': True,         # print a list of the formats to stdout and exit
# }

options = {
    "nocheckcertificate": True,
    "format": "bestvideo+bestaudio",
    "outtmpl": "/Users/kalyan.limkar/Music/Videos/%(artist)s/%(album)s/%(title)s.%(ext)s",
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4'
    }]
}

with youtube_dl.YoutubeDL(options) as ydl:
    # meta = ydl.extract_info(
    # "https://www.youtube.com/watch?v=XXYlFuWEuKI", download=True)
    ydl.download(["https://www.youtube.com/watch?v=XXYlFuWEuKI"])

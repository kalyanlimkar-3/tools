import youtube_dl

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
    ydl.download(["https://www.youtube.com/watch?v=XXYlFuWEuKI"])

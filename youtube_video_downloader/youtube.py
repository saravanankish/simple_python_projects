import pytube

link = input("Enter the youtube link: \n")
yt = pytube.YouTube(link)
strem = yt.streams.first()
strem.download()

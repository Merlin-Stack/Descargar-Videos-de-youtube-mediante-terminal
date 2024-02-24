from os import path, rename
from pytube import YouTube as yt

def descargar_video():
    descarga_video = path.expanduser("~/Videos")
    descarga_audio = path.expanduser("~/Música")
    link = input("Inserte el enlace del video: ")
    youtube = yt(link)
    
    formato = input("¿Será en (a)audio o (v)video ? ").lower()
    
    if formato == "v":
        youtube.streams.get_highest_resolution().download(descarga_video)
    elif formato == "a":
        video = youtube.streams.first()
        downloaded_file = video.download(descarga_audio)
        base, ext = path.splitext(downloaded_file)
        new_file = base + '.mp3'
        rename(downloaded_file, new_file)
    else:
        print("Formato no válido. Por favor, elija '(a)audio o (v)video '.")

    print("Descarga completa!")

if __name__ == "__main__":
    while True:
        descargar_video()
        opcion = input("¿Deseas hacer otra descarga? (si/no): ").lower()
        if opcion != "si":
            break

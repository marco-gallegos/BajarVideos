import peewee
import os
# constantes
extensiones = [
    ".mp4",
    ".mkv",
    ".avi"
]
file_name = "out.txt"
destination_dir = "convertidos"


for extension in extensiones:
    # comand = os.system(str(f"dir /B *{extension}"))
    comand = os.system(str(f"dir /B *{extension} > {file_name}"))

file = open(file_name,"r")
video_files = file.readlines()
file.close()

os.system(str(f"del {file_name}"))
os.system(str(f"mkdir {destination_dir}"))

for video in video_files:
    video = video.replace("\n", "")
    destination_name = video[:-4]
    os.system(str('ffmpeg -i "{}" -c:v libx265 -crf 30 "{}/{}.mp4"'.format(video, destination_dir, destination_name)))



import peewee
import os
import argparse
# constantes
extensiones = [
    ".mp4",
    ".mkv",
    ".avi"
]

parser = argparse.ArgumentParser()
# parser.add_argument("-v", "--verbose", help="Mostrar información de depuración", action="store_true")
parser.add_argument("-d", "--directory", help="Ruta absoluta del directorio de trabajo")
args = parser.parse_args()


if not args.directory:
    print("se necesita un directorio de trabajo argumento -d --directory")
    exit()

#variables iniciales
file_name = str(f"{args.directory}\\out.txt")
destination_dir = str(f"{args.directory}\\convertidos")

for extension in extensiones:
    comand_string = str(f"dir /B {args.directory}\\*{extension} >> {file_name}")
    comand = os.system(comand_string)

file = open(file_name,"r")
video_files = file.readlines()
file.close()

os.system(str(f"del {file_name}"))
os.system(str(f"mkdir {destination_dir}"))

for video in video_files:
    video = video.replace("\n", "")
    destination_name = video[:-4]
    os.system(str(f"ffmpeg -i \"{args.directory}\\{video}\" -c:v libx265 -crf 30 \"{destination_dir}\\{destination_name}.mp4\""))



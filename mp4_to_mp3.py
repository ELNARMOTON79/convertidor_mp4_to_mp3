import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def seleccionar_video():
    ruta_video = filedialog.askopenfilename(filetypes=[("Archivos MP4", "*.mp4")])
    if ruta_video:
        entrada_video.set(ruta_video)

def seleccionar_destino():
    ruta_audio = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Archivos MP3", "*.mp3")])
    if ruta_audio:
        salida_audio.set(ruta_audio)

def convertir():
    ruta_video = entrada_video.get()
    ruta_audio = salida_audio.get()
    if ruta_video and ruta_audio:
        video = VideoFileClip(ruta_video)
        video.audio.write_audiofile(ruta_audio)
        resultado.set("Conversión completada con éxito!")
    else:
        resultado.set("Por favor selecciona el video y el destino.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Convertidor de MP4 a MP3")

entrada_video = tk.StringVar()
salida_audio = tk.StringVar()
resultado = tk.StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Selecciona el video MP4:").grid(row=0, column=0, pady=5)
tk.Entry(frame, textvariable=entrada_video, width=50).grid(row=0, column=1, pady=5)
tk.Button(frame, text="Buscar", command=seleccionar_video).grid(row=0, column=2, pady=5)

tk.Label(frame, text="Selecciona el destino del MP3:").grid(row=1, column=0, pady=5)
tk.Entry(frame, textvariable=salida_audio, width=50).grid(row=1, column=1, pady=5)
tk.Button(frame, text="Guardar", command=seleccionar_destino).grid(row=1, column=2, pady=5)

tk.Button(frame, text="Convertir", command=convertir).grid(row=2, columnspan=3, pady=10)
tk.Button(frame, text="Salir", command=root.quit).grid(row=4, columnspan=3, pady=10)

tk.Label(frame, textvariable=resultado).grid(row=3, columnspan=3, pady=10)

root.mainloop()

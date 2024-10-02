from tkinter import Tk, Label, filedialog, Button, Frame, Spinbox, StringVar
from tkinter import ttk
from VideoC import VideoConvertor


class Ui(Tk):
    def __init__(self):
        super().__init__()  # Initialize the Tk class
        self.folder_selected = ""
        self.window()
        self.button_folder_selector()
        self.params = {
            'width': 640,
            "height": 480,
            'vcodec': 'libx265',
            'crf': 23,
            'acodec': 'aac',
            'preset': 'ultrafast',
            'tune': 'fastdecode',
            'y': None
        }
        self.video = VideoConvertor()

    def window(self):
        self.title("My Tkinter App")
        self.geometry("300x200")

    def button_folder_selector(self):
        Button(self, text="Choose your file",
               command=self.set_folder_selector).grid(row=0, column=1)

    def set_folder_selector(self):
        self.folder_selected = filedialog.askdirectory()
        self.rezolution()
        self.vcodec()
        self.acodec()
        self.quality()
        self.compress()

    def rezolution(self):
        frame = Frame(self)
        frame.grid(row=1, column=0, columnspan=2)
        Label(frame, text="width=").grid(row=1, column=0)
        self.width_var = StringVar(value=str(self.params['width']))
        self.w = ttk.Combobox(frame, width=8, values=(
          '640', '1280', '1366', '1600', '1980', '2560', '3840'))
        self.w.grid(row=1, column=1)
        self.w.current(0)
        Label(frame, text="height=").grid(row=2, column=0)
        self.height_var = StringVar(value=str(self.params['height']))
        self.h =  ttk.Combobox(frame, width=8, values=(
          '480', '720', '768', '900', '1080', '1440', '2160'))
        self.h.grid(row=2, column=1)
        self.h.current(0)
    def vcodec(self):
        frame = Frame(self)
        frame.grid(row=2, column=0, columnspan=3)
        Label(frame, text="vcodec=").grid(row=3, column=0)
        codec_chose = ttk.Combobox(frame, width=8, values=(
            'libx265', 'libx264', 'libvpx', 'libvpx-vp9', 'libtheora', 'libaom-av1'))
        codec_chose.grid(row=3, column=1)
        codec_chose.current(0)
        self.params['vcodec'] = codec_chose.get()

    def acodec(self):
        frame = Frame(self)
        frame.grid(row=3, column=0, columnspan=3)
        Label(frame, text="acodec=").grid(row=4, column=0)
        codec_chose = ttk.Combobox(frame, width=8, values=(
            'aac', 'libmp3lame', 'libvorbis', 'libopus', 'flac', 'alac', 'pcm_s16le'))
        codec_chose.grid(row=4, column=1)
        codec_chose.current(0)
        self.params['acodec'] = codec_chose.get()

    def quality(self):
        frame = Frame(self)
        frame.grid(row=4, column=0, columnspan=2)
        Label(frame, text="quality=").grid(row=5, column=0)
        self.crf_var = StringVar(value=str(self.params['crf']))
        self.s = Spinbox(frame, from_=0, to=100, width=8,
                         textvariable=self.crf_var)
        self.s.grid(row=5, column=1)

    def compress(self):
        Button(self, text="compress",
               command=self.test).grid(row=5, column=0)

    def test(self):
        self.params['width'] = int(self.width_var.get())
        self.params['height'] = int(self.height_var.get())
        self.params['crf'] = int(self.crf_var.get())
        self.video.convertVideo(self.folder_selected, self.params)

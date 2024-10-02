import os
import ffmpeg
from concurrent.futures import ThreadPoolExecutor


class VideoConvertor:
    def __init__(self):
        self.path_and_video = []
        self.width = 1280
        self.heigth = 780

    def convertVideo(self, video_path, params):
        contents = os.listdir(video_path)
        for item in contents:
            c = video_path+'/'+item
            if os.path.isdir(c):
                self.convertVideo(c, params)
            elif os.path.isfile(c):
                input_video_path = self.get_video_name(c)
                if len(input_video_path)>0:
                    if input_video_path[1] == '.mp4' or input_video_path[1] == '.mov' or input_video_path[1] == '.mkv':
                        o = video_path+'/'+' '+input_video_path[0]+'.mp4'
                        self.path_and_video.append([c, o])
                        self.convert_video(c, o, params)

    def get_video_name(self, video_path):
        basename = os.path.basename(video_path)
        video_format = ['.mp4', '.mov', '.mkv']
        video_name = []
        for vf in video_format:
            if vf in basename:
                v = basename.split(vf)[0]
                video_name.append(v)
                video_name.append(vf)
                break
        return video_name

    def convert_video(self, input_path, output_path, params):
        try:
            input_stream = ffmpeg.input(input_path)
            video = input_stream.video
            audio = input_stream.audio
            if 'width' in params and 'height' in params:
                self.width = params['width']
                self.heigth = params['height']
                scaled_video = video.filter(
                    'scale', self.width, self.heigth)
                audio = input_stream.audio
                del params['width'], params['height']
            else:
                scaled_video = video.filter(
                    'scale', self.width, self.heigth)
            ffmpeg.output(scaled_video, audio, output_path,
                          **params).run(overwrite_output=True)
            os.remove(input_path)
            os.rename(output_path, input_path)
        except ffmpeg.Error as e:
            print(f"Error converting video: {e.stderr}")

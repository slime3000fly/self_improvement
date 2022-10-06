
from moviepy.editor import *
clip = VideoFileClip('logo.mp4', False, True, 200000, (720, 1080))
clip.preview()
exec(open('main.py').read())
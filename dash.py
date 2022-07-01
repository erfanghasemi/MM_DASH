import ffmpeg_streaming

# Generate DASH files for Movies

video = ffmpeg_streaming.input('/home/erfan/Projects/DASH/TheGodfather.mp4')

dash = video.dash(ffmpeg_streaming.Formats.h264())
dash.auto_generate_representations()
dash.output("/home/erfan/Projects/DASH/TheGodfather/TheGodfather.mpd")

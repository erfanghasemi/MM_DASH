import ffmpeg_streaming

# Generate DASH files for Movies

video = ffmpeg_streaming.input('/home/erfan/Projects/DASH/The Godfather.mp4')

_144p  = ffmpeg_streaming.Representation(ffmpeg_streaming.Size(256, 144), ffmpeg_streaming.Bitrate(95 * 1024, 64 * 1024))
_240p  = ffmpeg_streaming.Representation(ffmpeg_streaming.Size(426, 240), ffmpeg_streaming.Bitrate(150 * 1024, 94 * 1024))
_360p  = ffmpeg_streaming.Representation(ffmpeg_streaming.Size(640, 360), ffmpeg_streaming.Bitrate(276 * 1024, 128 * 1024))
_480p  = ffmpeg_streaming.Representation(ffmpeg_streaming.Size(854, 480), ffmpeg_streaming.Bitrate(750 * 1024, 192 * 1024))


dash = video.dash(ffmpeg_streaming.Formats.h264())
dash.representations(_144p, _240p, _360p, _480p)
dash.output("'/home/erfan/Projects/DASH/The Godfather")

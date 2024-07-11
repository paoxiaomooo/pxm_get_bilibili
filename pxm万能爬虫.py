import yt_dlp


def list_formats(url):
    ydl_opts = {
        'listformats': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_video(url, format_code):
    ydl_opts = {
        'format': format_code,
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
video_url = input("请输入视频网址")
list_formats(video_url)
format_code = input("请输入你选择的格式代码: ")

# 下载视频
download_video(video_url, format_code)

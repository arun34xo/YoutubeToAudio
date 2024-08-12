#!/usr/bin/env python3
import yt_dlp
import os
import glob

def download_video_as_audio(url, output_path = 'output.mp3'):
	ydl_opts = {
		'format': 'bestaudio/best',
		'outtmpl': 'temp.%(ext)s',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '320',
		}],
	}
	
	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		info_dict = ydl.extract_info(url, download = True)
	
	downloaded_file = glob.glob('temp.*')[0]
	
	os.rename('temp.mp3', output_path)
	print(f"Converted to MP3 and saved as {output_path}")
	
if __name__ == "__main__":
	url = input("Enter the YouTube video URL to be converted: ")
	download_video_as_audio(url) 

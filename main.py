import os	
import random
import requests
import ctypes
ctypes.windll.kernel32.SetConsoleTitleA("Gay TikTok downloader")




os.system('cls && title [TikTok Video Downloader]')
downloaded = 0
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
if not os.path.exists('Downloads'):
    os.makedirs('Downloads')





def main():
	video_url = input('Enter TikTok Video URL: (if india use vpn cuz gay)')
	download_w_wm(video_url)

def download_w_wm(url):
	response = requests.get(url,headers = HEADERS).text
	if(requests.get(url,headers = HEADERS).status_code == 200):
		ctypes.windll.kernel32.SetConsoleTitleA(f"Downloading{url}")
		download_url_list = response.split('urls":["')[1]
		download_url = download_url_list.split('"]')[0]

		count = str(downloaded)
		print(count)

		name_downn = response.split('pageUrl":"/@')[1]
		name = name_downn.split('video')[0].replace("/", "_")
		fin_name = name+"is gay_"+count+".mp4"

		video_download_resp = requests.get(download_url)
		print(video_download_resp.status_code)

		if(video_download_resp.status_code == 200):
			with open(f"Downloads/{fin_name}","wb") as gL:
				gL.write(video_download_resp.content)
			print(f'Downloaded (with watermark ooops): .\\Downloaded\\{fin_name}')
			
       

downloaded += 1
print()


if __name__ == "__main__":
    main()
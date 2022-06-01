from pytube import YouTube

url = 'https://www.youtube.com/watch?v=7BXJIjfJCsA'
my_video = YouTube(url)

print("*********************Video Title************************")
#get Video Title
print(my_video.title)

print("********************Tumbnail Image***********************")
#get Thumbnail Image
print(my_video.thumbnail_url)

print("********************Download video*************************")
#get all the stream resolution for the 
for stream in my_video.streams:
    print(stream)

#set stream resolution
my_video = my_video.streams.get_highest_resolution()

#Download video
my_video.download()
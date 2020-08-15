from pytube import YouTube

LInk=input('Enter Link here : ')
yt=YouTube(LInk)
videos=yt.streams.all()
i=1
for video in videos:
    print(f'{i} {video}')
    i += 1
st_n=input('Enter Stream Number')
if st_n > 0:
    video=videos[int(st_n)-1]
    video.download()
    print('Downloaded')
else:
    print('Please provide valid stream number')
import json
from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch5'
}

ydl = YoutubeDL(options)
search_result = ydl.extract_info('that girl', False)
print(type(search_result))
# with open('file.txt', 'w') as file:
#     file.write(json.dumps(search_result))
a = search_result["entries"]
# with open('fileee.txt','w') as file:
#     file.write(json.dumps(a[0]))
for i in range(0,5):
    b = a[i]
    print(b["webpage_url"])
for e in range(0,5):
    c = a[i]
    print(c["title"])
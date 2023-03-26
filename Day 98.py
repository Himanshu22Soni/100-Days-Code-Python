# Multiprocessing in Python.

import multiprocessing
import requests


def downloadImage(url, name):
    print("Downloading image")
    res = requests.get(url)
    open(f"C:/Users/hp/Desktop/pics/img{name}.jpg", "wb").write(res.content)
    print("Downloaded image")


url = "https://picsum.photos/2000/3000"
processes = []

for i in range(1, 6):
    p = multiprocessing.Process(target=downloadImage, args=[url, i])
    p.start()
    processes.append(p)

for pr in processes:
    pr.join()

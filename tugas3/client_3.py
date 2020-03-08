import threading
import logging
import requests
import datetime
import os


def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}")
        fp = open(f"{namafile}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


if __name__=='__main__':

    threads = []
    gambar = [ 
        'https://myrepro.files.wordpress.com/2015/10/wpid-wallpaper-pemandangan-pantai-jpg.jpeg', 
        'https://myrepro.files.wordpress.com/2015/10/wpid-wallpaper-pemandangan-air-terjun-jpg.jpeg',
        'https://upload.wikimedia.org/wikipedia/commons/6/65/Pemandangan_alam.jpg'
    ]
    
    for i in gambar:
        t = threading.Thread(target=download_gambar,args=(i,))
        threads.append(t)
        t.start()


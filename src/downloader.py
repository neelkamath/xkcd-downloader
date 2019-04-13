#!/usr/bin/env python3

import os
import os.path
import re
import requests
import urllib.request
import click
import multiprocessing
import threading
from config import Config
from threading import Thread, Lock
import sys

CONFIG_NAME = ".xkcd-config.json"
URL = "http://xkcd.com/info.0.json"  # Link to the latest xkcd comic.
NUM_XKCD_COMIC = "num"

num_downloadable = 0  # Number of comics to be downloaded at this session
num_downloaded = 0  # Number of comics that currently downloaded at this session


def download_comic(job, config, mutex):
    global num_downloadable
    global num_downloaded

    for comic in job:
        mutex.acquire()
        if num_downloadable - num_downloaded == 0:
            percentage = 100
        else:
            num_downloaded = num_downloaded + 1
            percentage = (num_downloaded / num_downloadable) * 100

        print("Progress: {}% ".format(round(percentage, 2)), end="\r")
        mutex.release()

        site = "http://xkcd.com/{}/info.0.json".format(comic)
        data = requests.get(site)
        if data.status_code != 200:
            continue
        data = data.json()
        if not re.search(r".jpg|.png$", data["img"]):
            continue
        months = {1: "January", 2: "February", 3: "March", 4: "April",
                  5: "May", 6: "June", 7: "July", 8: "August", 9: "September",
                  10: "October", 11: "November", 12: "December"}
        m = months[int(data["month"])]
        m = "{}-{}".format(data["month"], m)
        newDir = "{}/{}/{}".format(config.directory, data["year"], m)
        if not os.path.isdir(newDir):
            os.makedirs(newDir)

        title = re.sub(r"/|\\|\:|\*|\?|\"|<|>|\|", "", data["safe_title"])
        ext = data["img"][len(data["img"]) - 4:]
        name = "{}/{}-{}{}".format(newDir, comic, title, ext)
        urllib.request.urlretrieve(data["img"], name)

        mutex.acquire()
        config.set_succeeded(comic)
        config.commit()
        mutex.release()


def chunks(l, n):

    # Break list l as n sized lists.
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i + n]


@click.command()
@click.option('-d', '--directory', default='./')
@click.option('-v', '--verbose', is_flag=True)
def main(directory, verbose):
    global num_downloadable

    num_cores = multiprocessing.cpu_count()
    config = Config(CONFIG_NAME)
    config.directory = directory
    config.commit()

    if not os.path.isdir(config.directory):
        os.makedirs(config.directory)

    data = requests.get(URL).json()
    num_xkcd_comic = data[NUM_XKCD_COMIC]

    mutex_num_download = Lock()
    jobs = list(set(range(num_xkcd_comic)) - set(config.get_succeeded_list(num_xkcd_comic)))
    num_downloadable = len(jobs)

    if num_downloadable == 0:
        print("All Clear :>")
        sys.exit(1)

    if verbose:
        print("{} comics to be downloaded".format(num_downloadable))

    for job in chunks(jobs, num_downloadable // num_cores):
        t = Thread(target=download_comic, args=(job, config, mutex_num_download))
        t.start()

    for thread in threading.enumerate():
        if thread is not threading.currentThread():
            thread.join()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from geek_time import download_video_by_cid
from geek_time import fetch_my_column

if __name__ == "__main__":
    fetch_my_column()
    cid = int(input("input video column id\n> "))
    size = 100
    download_video_by_cid(cid, 100)

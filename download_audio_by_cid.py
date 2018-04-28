#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from geek_time import download_audio_by_cid
from geek_time import fetch_my_column

if __name__ == "__main__":
    fetch_my_column()
    cid = int(input("input audio column id\n> "))
    size = 100
    download_audio_by_cid(cid, 100)

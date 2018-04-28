# GeekTime 下载极客时间音视频
---

### [下载《极客时间》音视频（一）](http://iosdevlog.com/2018/04/19/time.html)
### [下载《极客时间》音视频（二）](http://iosdevlog.com/python/2018/04/26/geektime.html)
### [下载《极客时间》音视频（三）](http://iosdevlog.com/2018/04/28/geek-time.html)

---

# screenshot

![download](./screenshot/download.png)

# useage

1. login <http://geekbang.org> from chrome first

2. work on python3 virtualenv

```bash
(geektime) pip install -r requirements.txt
(geektime) python download_audio.py
(geektime) python download_audio_by_cid.py
login 'http://geekbang.org' from chrome first
...
id = 78  type = other  column_title = 架构师
id = 50  type = audio  column_title = 邱岳的产品手记
id = 77  type = video  column_title = 9 小时搞定微信小程序开发
input audio column id
> 50
...
100%[===========================================================>]   1.87K  --.-KB/s    in 0s
...
...
...
(geektime) python download_video_by_cid.py
login 'http://geekbang.org' from chrome first
...
id = 78  type = other  column_title = 架构师
id = 50  type = audio  column_title = 邱岳的产品手记
id = 77  type = video  column_title = 9 小时搞定微信小程序开发
input audio column id
> 77 
...
第91讲___小程序之性能优化
{"hd":{"size":172783023,"url
libavutil      55. 78.100 / 55. 78.100
libavcodec     57.107.100 / 57.107.100
libavformat    57. 83.100 / 57. 83.100
libavdevice    57. 10.100 / 57. 10.100
libavfilter     6.107.100 /  6.107.100
libavresample   3.  7.  0 /  3.  7.  0
libswscale      4.  8.100 /  4.  8.100
libswresample   2.  9.100 /  2.  9.100
libpostproc    54.  7.100 / 54.  7.100
...
```

## issue
---

* How do I install Python 3.6 using apt-get?

> Ubuntu 14.04 and 16.04

If you are using Ubuntu 14.04 or 16.04, you can use Felix Krull's deadsnakes PPA at https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa:

```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.6
```

Alternatively, you can use J Fernyhough's PPA at https://launchpad.net/~jonathonf/+archive/ubuntu/python-3.6:

```bash
$ sudo add-apt-repository ppa:jonathonf/python-3.6
$ sudo apt-get update
$ sudo apt-get install python3.6
```

> Ubuntu 16.10 and 17.04

If you are using Ubuntu 16.10 or 17.04, then Python 3.6 is in the universe repository, so you can just run:

```bash
$ sudo apt-get update
$ sudo apt-get install python3.6
```

After installation for Ubuntu 14.04, 16.04, 16.10 and 17.04
To invoke the Python 3.6 interpreter, run python3.6.

> Ubuntu 17.10

Ubuntu 17.10 already comes with Python 3.6 as default. Just run python3 to invoke it.

<https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-apt-get>

* fatal error: Python.h: No such file or director

> install python*-dev

```bash
$ sudo apt install python-dev
$ sudo apt install python3-dev
$ sudo apt install python3.6-dev
```

* sqlite3.OperationalError: no such column: secure

Chrome 66 has changed the name of the column secure to is_secure in the cookies table. It seems that it's simple to fix this by changing the database query in L118 of __init__.py, but I'm not sure that's enough.

> [Chrome 66 SQLite schema change](https://bitbucket.org/richardpenman/browsercookie/issues/26/chrome-66-sqlite-schema-change)

* The encoder 'aac' is experimental but experimental codecs are not enabled, add '-strict -2' if you want to use it.

> change ffmpeg command in **geek_time.py** to +144 line

```
ffmpeg -i ***.m3u8 -strict -2 ***.mp4
```


# License
---

GeekTime is released under the MIT license. See LICENSE for details.

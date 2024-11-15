# yt_formatter v1.0

This tool allows you to directly download publicly accessible YouTube videos to a specified directory on your local machine in a specified format. This allows you to download videos or seamlessly extract audio from any video on the platform. 

First, you must clone the repository and navigate into the resulting directory

```bash
git clone https://github.com/justinciocoi/yt_formatter && cd yt_formatter
```

In order to download the necessary dependencies, run:

```bash
pip install -r scripts/requirements.txt
```

within the yt_formatter directory.

Next, make sure the shell script in the scripts directory is made exectuable using the following command

```bash
chmod +x scripts/yt_format.sh
```

Now, running the python script `ytformat.py` will open the application window with fields for youtube URL, file extension, and directory. This allows you to download youtube content in a variety of formats directly to your machine in a directory of your choosing. This tool uses yt-dlp and ffmpeg extensively to achieve the goal of fetching data from youtube and file conversion operations. 

With python installed on your machine, run the following in your terminal to launch the application

```bash
python3 ytformat.py
```

This application was developed for and tested on macOS Sonoma 14.4

![](https://i.imgur.com/hOCqsep.png)

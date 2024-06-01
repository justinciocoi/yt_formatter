#!/bin/zsh
# yt_format.sh - Download video from URL and convert it to specified format.

# Ensure correct number of arguments is passed
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <format>"
    exit 1
fi

url=$1
format=$2
filename=$(yt-dlp --get-filename -o '%(title)s.%(ext)s' "$url")

# Download the video
yt-dlp -o '%(title)s.%(ext)s' "$url"

# Convert the downloaded file
ffmpeg -i "$filename" "$filename.$format"

# Remove the original file
rm "$filename"


ffmpeg -framerate 30 -i "!assembly/%%05d.png" -c:v libx264 -pix_fmt yuv420p BGA2.mp4 -y
ffmpeg -i BGA2.mp4 -i youtubeyoutube.mp3 -c:v copy -c:a copy DEMO2.mp4 -y
ffmpeg -i DEMO2.mp4 -vf "scale=(iw*sar)*min(512/(iw*sar)\,512/ih):ih*min(512/(iw*sar)\,512/ih), pad=512:512:(512-iw*min(512/iw\,512/ih))/2:(512-ih*min(512/iw\,512/ih))/2" -c:a copy DEMODEMO2.mp4 -y 
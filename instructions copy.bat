ffmpeg -framerate 30 -i "!assembly_cc/%%05d.png" -c:v libx264 -pix_fmt yuv420p BGA3.mp4 -y
ffmpeg -i BGA3.mp4 -i youtube_real.mp3 -c:v copy -c:a copy DEMO3.mp4 -y
ffmpeg -i BGA3.mp4 -i silence.mp3 -c:v copy -c:a copy DEMO3_SILENT.mp4 -y
ffmpeg -i DEMO3.mp4 -vf "scale=(iw*sar)*min(512/(iw*sar)\,512/ih):ih*min(512/(iw*sar)\,512/ih), pad=512:512:(512-iw*min(512/iw\,512/ih))/2:(512-ih*min(512/iw\,512/ih))/2" -c:a copy DEMODEMO3.mp4 -y 
ffmpeg -i DEMO3_SILENT.mp4 -vf "scale=(iw*sar)*min(512/(iw*sar)\,512/ih):ih*min(512/(iw*sar)\,512/ih), pad=512:512:(512-iw*min(512/iw\,512/ih))/2:(512-ih*min(512/iw\,512/ih))/2" -c:a copy DEMODEMO3_SILENT.mp4 -y 
ffmpeg -i DEMODEMO3.mp4 henceforth_bga.mpg -y
ffmpeg -i DEMODEMO3_SILENT.mp4 henceforth_bga_with_silence.mpg -y
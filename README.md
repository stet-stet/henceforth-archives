# henceforth-archives
Code used to create background animations(BGA) for "henceforth", my "BMS OF FIGHTERS XVII" submission.

## Dependencies

- tensorflow
- tensorflow_hub
- PIL
- numpy
- matplotlib
- IPython

You also need pictures to style-transfer.

## Explanations

- `transfer.py`: loads style transfer model from tensorflow hub, and style-transfers a single image.
- `transfer-folder.py`: loads style transfer model from tensorflow hub, and style-transfers all images in a folder.
  - `python transfer-folder.py (input folder) (style image) (output)`
- `assemble.py`: copies designated frames into `./!assembly`.
  - `assemble_script.sh`: script for designating frames
- `color_correct.py`: performs denoising to all frames in a folder.
- `instructions.bat` and `instructions copy.bat`: assembles the image into a 30fps video and encodes the video into correct format.
- `cmd.txt`: command for letterboxing the BGA so that it has a aspect ratio of 1:1.

## The end result
[【BOFXVII】 Henceforth / Qyubey feat. Juudenki 【BGA】](https://youtu.be/W7L2fCaU5io)


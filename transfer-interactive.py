import tensorflow as tf
import numpy as np
import PIL.Image
import tensorflow_hub as hub
import os 
from tqdm import tqdm

hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/1')

def tensor_to_image(tensor):
  tensor = tensor*255
  tensor = np.array(tensor, dtype=np.uint8)
  if np.ndim(tensor)>3:
    assert tensor.shape[0] == 1
    tensor = tensor[0]
  return PIL.Image.fromarray(tensor)

def load_img(path_to_img):
  max_dim = 512
  img = tf.io.read_file(path_to_img)
  img = tf.image.decode_image(img, channels=3)
  img = tf.image.convert_image_dtype(img, tf.float32)

  shape = tf.cast(tf.shape(img)[:-1], tf.float32)
  long_dim = max(shape)
  scale = max_dim / long_dim

  new_shape = tf.cast(shape * scale, tf.int32)

  img = tf.image.resize(img, new_shape)
  img = img[tf.newaxis, :]
  return img

def do(content_filename,style_filename):
    content = load_img(content_filename)
    style = load_img(style_filename)
    stylized_image = hub_module(tf.constant(content), tf.constant(style))[0]
    return tensor_to_image(stylized_image)

def save_stylized_image(content_filename,style_filename,output_filename):
    im = do(content_filename,style_filename)
    im.save(output_filename)

if __name__=="__main__":
    # print(sys.argv[0] + " (content) (style) (output)")
    com = "A"
    while com.upper() != "C":
      if com.upper() != "H":
        os.system("cls")
      print(
      """
      ================= Style Transfer(v 0.0.1) ================= 

      원하시는 커맨드를 입력하신 후 Enter를 눌러주세요!
      [H]: Help
      [C]: Convert

      """)
      com = input("")

      if com.upper() == "C":
        sysargv1 = input("style transfer를 적용하실 이미지가 모여있는 폴더 경로를 입력해주세요(입력 후 Enter)\n")
        sysargv2 = input("style을 따 올 이미지를 입력해주세요(입력 후 Enter)\n")
        print("완성된 이미지들을 저장하실 폴더를 입력해주세요. (파일명은 같게 유지되어 나오며, 겹치는 경우 자동으로 덮어씌워지니 조심해주세요!)")
        print("예시) 'input'이라는 폴더의 01.jpg 02.png 03.JPEG를 style transfer해 'output'이라는 폴더에 넣는 경우, 이 폴더에는 01.jpg 02.png 03.JPEG라는 이름의 파일이 새로 생길 것이고, 그 내용물은 원래의 01jpg 02.png 03.JPEG를 style transfer한 게 됩니다.")
        sysargv3 = input("(입력 후 Enter)\n")
        sysargv1 = sysargv1.strip()
        sysargv2 = sysargv2.strip()
        sysargv3 = sysargv3.strip()
        os.makedirs(sysargv3, exist_ok=True)
        for root, dirs, files in os.walk(sysargv1):
          print("현재 보고 있는 폴더: "+str(root))
          tqdm_bar = tqdm(files)
          for file in tqdm_bar:
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
              inpath = root + '/' + file
              outpath = sysargv3 + '/' + file
              tqdm_bar.set_description(f"query: {inpath} to {outpath}")
              save_stylized_image(inpath, sysargv2, outpath)
        exit(0)
      else:
        print("""

        ===== 도움말 =====
        
        style transfer란, 그 이름 그대로 어떠한 이미지의 "style"을 "transfer"해 주는 알고리즘/기술/모델입니다.
        스타일을 전환할 이미지(A라고 합시다)와 스타일의 원형이 되는 이미지(B라고 합시다)를 받아서, A이미지를 B스타일로 바꾸어줍니다. 

        이를테면, 다음과 같이 사용하실 수 있습니다.
        영상을 프레임별로 쪼갠다 -> 본 프로그램을 이용하여 

        본 프로그램은 지정하신 폴더 내의 모든 이미지에 style transfer를 적용하여, 512p의 아웃풋 이미지를 만듭니다.

        문의: Discord stetstet#0698; Twitter @QyubeySan; e-mail qyubeychama@gmail.com

        """)


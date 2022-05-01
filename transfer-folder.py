import tensorflow as tf
import IPython.display as display
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12,12)
mpl.rcParams['axes.grid'] = False
import numpy as np
import PIL.Image
import time
import functools
import tensorflow_hub as hub
import sys 
import os 

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

def imshow(image, title=None):
  if len(image.shape) > 3:
    image = tf.squeeze(image, axis=0)

  plt.imshow(image)
  if title:
    plt.title(title)

def do(content_filename,style_filename):
    content = load_img(content_filename)
    style = load_img(style_filename)
    stylized_image = hub_module(tf.constant(content), tf.constant(style))[0]
    return tensor_to_image(stylized_image)

def save_stylized_image(content_filename,style_filename,output_filename):
    im = do(content_filename,style_filename)
    im.save(output_filename)

if __name__=="__main__":
    if len(sys.argv) <= 3:
        print(sys.argv[0] + " (content) (style) (output)")
    else:
        os.makedirs(sys.argv[3],exist_ok=True)
        for root, dirs, files in os.walk(sys.argv[1]):
          for file in files:
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
              inpath = root + '/' + file
              outpath = sys.argv[3] + '/' + file
              save_stylized_image(inpath,sys.argv[2],outpath)
              print(f"query: {inpath} to {outpath}")
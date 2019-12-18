from PIL import Image
import torch as t
from torchvision import transforms
import numpy as np 
import matplotlib.pyplot as plt 
from func import *


pic1 = Image.open('src/img.jpg')
pic2 = Image.open('src/img2.jpg')
pic3 = Image.open('src/img3.jpg')
pic4 = Image.open('src/img4.jpg')


out_img = Hiso_spec(pic2, pic1)
out_img.save('result1/1.jpg')

out_img = Hiso_spec(pic1, pic2)
out_img.save('result1/2.jpg')

out_img = Hiso_spec(pic3, pic4)
out_img.save('result1/3.jpg')

out_img = Hiso_spec(pic4, pic3)
out_img.save('result1/4.jpg')

out_img = Hiso_spec(pic1, pic3)
out_img.save('result1/5.jpg')

out_img = Hiso_spec(pic3, pic1)
out_img.save('result1/6.jpg')
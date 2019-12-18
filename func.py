from PIL import Image
import torch as t
from torchvision import transforms
import numpy as np 
import matplotlib.pyplot as plt 

loader = transforms.Compose([
    transforms.ToTensor()])  
DEVICE = t.device("cuda" if t.cuda.is_available() else "cpu") # 让torch判断是否使用GPU，建议使用GPU环境，因为会快很多

def equ(img):
    count = np.array([np.sum([img==i]) for i in range(256)])
    N = np.sum(count)
    count = count / N
    F = np.array([np.sum(count[:i]) for i in range(256)])
    F = F[img] *255
    return Image.fromarray(F.astype('uint8'))

def equ_rgb(img):
    output = np.zeros_like(img)
    for channel in range(img.shape[2]):
        count = np.array([np.sum([img[:,:,channel]==i]) for i in range(256)])
        count = count / np.sum(count)
        F = np.array([np.sum(count[:i]) for i in range(256)])
        output[:,:,channel] = F[img[:,:,channel]]*255
    return Image.fromarray(output.astype('uint8'))


def equ_rgb_pure(img):
    output = t.zeros_like(img)
    F = t.zeros([3,256]).to(DEVICE)
    for channel in range(img.shape[0]):
        count = t.tensor([t.sum(img[channel,:,:]==i)for i in range(256)]).float()
        count = count / t.sum(count)
        F[channel] = t.tensor([t.sum(count[:i]) for i in range(256)])
    return (F*255).long()


def Hiso_spec(img, ref):
    img = loader(img).to(DEVICE)*255
    ref = loader(ref).to(DEVICE)*255
    out_img = t.zeros_like(img)
    #print(img.dtype)
    F1 = equ_rgb_pure(img)
    F2 = equ_rgb_pure(ref)
    img = img.long()
    ref = ref.long()
    equed_input =[F1[i][img[i,:,:]] for i in range(3)]
    F2_1 = [t.tensor([F2[c][F2[c]<=i].shape[0]-1 for i in range(256)]) for c in range(3)]
    print(F2[0],F2_1[0])
    for c in range(img.shape[0]):
        out_img[c] = F2_1[c][img[c]]
    return transforms.ToPILImage()(out_img.cpu()/255)
import numpy as np
from PIL import Image
import time

def nearest(image, target_size):
    """
    Nearest Neighbour interpolate for RGB  image

    :param image: rgb image
    :param target_size: tuple = (height, width)
    :return: None
    """
    if target_size[0] < image.shape[0] or target_size[1] < image.shape[1]:
        raise ValueError("target image must bigger than input image")
    # 1：按照尺寸创建目标图像
    target_image = np.zeros(shape=(target_size[0], target_size[1], 3))
    # 2:计算height和width的缩放因子
    alpha_h = target_size[0] / image.shape[0]
    alpha_w = target_size[1] / image.shape[1]

    for tar_x in range(target_image.shape[0] - 1):
        for tar_y in range(target_image.shape[1] - 1):
            # 3:计算目标图像人任一像素点
            # target_image[tar_x,tar_y]需要从原始图像
            # 的哪个确定的像素点image[src_x, xrc_y]取值
            # 也就是计算坐标的映射关系
            src_x = round(tar_x / alpha_h)
            src_y = round(tar_y / alpha_w)

            # 4：对目标图像的任一像素点赋值
            target_image[tar_x, tar_y] = image[src_x-1, src_y-1]

    return target_image


path = 'donwsampling.bmp'
image = Image.open(path)
image = np.array(image)

start_time=time.time()
target = nearest(image, (2160, 3840))
end_time=time.time()
target = Image.fromarray(target.astype('uint8')).convert('RGB')
target.save('mostnearest.bmp', 'bmp')
print("time cost = ",end_time-start_time," s")
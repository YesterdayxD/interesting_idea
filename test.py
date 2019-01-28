# from PIL import Image
# # #
# # # im_path = "C:/Users/limk/Desktop/interesting_idea/images/crop001001a.png"
# # # im = Image.open(im_path)
# # # width, height = im.size
# # # # 宽高
# # # print(im.size, width, height)
# # # # 格式，以及格式的详细描述
# # # print(im.format, im.format_description)
# # #
# # # im.save("C:/Users/limk/Desktop/interesting_idea/images/crop001001a.png")
# # # im.show()

# import cv2
# cv2.imread("C:/Users/limk/Desktop/interesting_idea/images/crop001001a.png")

import numpy as np

with open("C:/Users/limk/Desktop/interesting_idea/pos_feature.npy", "rb") as f:
    a = np.load(f)
    print(a)
    print(type(a))
    print(a.shape)

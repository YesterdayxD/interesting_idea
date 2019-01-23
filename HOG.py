import os
import time

import cv2
import numpy as np


def calc_hist(mag, angle, bin_size=9):
    hist = np.zeros((bin_size,), dtype=np.int32)

    bin_step = 180 // bin_size
    bins = (angle // bin_step).flatten()
    flat_mag = mag.flatten()
    for i, m in zip(bins, flat_mag):
        hist[i] += m
    return hist


def l2_norm(cells):
    block = cells.flatten().astype(np.float32)
    norm_factor = np.sqrt(np.sum(block ** 2) + 1e-6)
    block /= norm_factor
    return block


def calc_hog(gray):
    dx = cv2.Sobel(gray, cv2.CV_16S, 1, 0)
    dy = cv2.Sobel(gray, cv2.CV_16S, 0, 1)
    sigma = 1e-3
    angle = np.int32(np.arctan(dy / (dx + sigma)) * 180 / np.pi) + 90
    dx = cv2.convertScaleAbs(dx)
    dy = cv2.convertScaleAbs(dy)
    mag = cv2.addWeighted(dx, 0.5, dy, 0.5, 0)

    print('angle\n', angle[:8, :8])
    print('mag\n', mag[:8, :8])

    cell_size = 8
    bin_size = 9
    img_h, img_w = gray.shape[:2]
    cell_h, cell_w = (img_h // cell_size, img_w // cell_size)

    cells = np.zeros((cell_h, cell_w, bin_size), dtype=np.int32)
    for i in range(cell_h):
        cell_row = cell_size * i
        for j in range(cell_w):
            cell_col = cell_size * j
            cells[i, j] = calc_hist(
                mag[cell_row:cell_row + cell_size,
                cell_col:cell_col + cell_size],
                angle[cell_row:cell_row + cell_size,
                cell_col:cell_col + cell_size],
                bin_size=bin_size)

    block_size = 2
    block_h, block_w = (cell_h - block_size + 1, cell_w - block_size + 1)
    blocks = np.zeros((block_h, block_w, block_size * block_size * bin_size),
                      dtype=np.float32)
    for i in range(block_h):
        for j in range(block_w):
            blocks[i, j] = l2_norm(cells[i:i + block_size, j:j + block_size])

    return blocks.flatten()


def main():
    SHOWTIME = 0
    img = cv2.imread(
        "C:/Users/limk/Desktop/interesting_idea/images/crop001001f.jpg")
    # crop001001f.png
    # dva.jpg
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # gray=cv2.COLOR_BGR2GRAY(img)
    print(gray.shape)
    cv2.imshow("img", gray)
    a = calc_hog(gray)
    print(len(a))

    cv2.waitKey(SHOWTIME)
    cv2.destroyWindow("img")


def extract_feature():
    dir_path = "C:/Users/limk/Desktop/interesting_idea/test_64x128_H96/"
    sample_dir = {"1": "pos", "2": "neg"}
    for k, v in sample_dir.items():
        path = dir_path + v + "/"
        for root, dirs, files in os.walk(path):
            # print(len(files))
            # print(files)
            with open("{}_feature.npy".format(v), "wb") as f:

                for f_name in files:
                    start_time = time.time()
                    img = cv2.imread(path + f_name)
                    # TODO(limk):reshape the size of image
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    feature_vector = calc_hog(gray)
                    # f.write(str(feature_vector))
                    # f.write("\n")
                    print(feature_vector.shape)
                    np.save(f, feature_vector)
                    end_time = time.time() - start_time
                    print(
                        "It is extracting feature on image {}. It costs {}s.".format(
                            f_name, end_time))


if __name__ == "__main__":
    # main()
    extract_feature()
    pass
# https://www.jianshu.com/p/ed21c357ec12

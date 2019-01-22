import numpy as np 
def calc_hist(mag,angle,bin_size=9):
    hist=np.zeros((bin_size,),dtype=np.int32)

    bin_step=180//bin_size
    bins=(angle//bin_step).flatten()
    flat_mag=mag.flatten()
    for i,m in zip(bins,flat_mag):
        hist[i]+=m
    return hist

cell_size=8
bin_size=9
img_h,img_w=gray.shape[:2]
cell_h,cell_w=(img_h//cell_h,img_w//cell_w)

cells=np.zeros((cell_h,cell_w,bin_size),dtype=np.int32)
for i in range(cell_h):
    cell_row=cell_size*i
    for j in range(cell_w):
        cell_col=cell_size*j
        cell[i,j]=calc_hist(mag[],angle[],bin_size=bin_size)
    pass
https://www.jianshu.com/p/ed21c357ec12
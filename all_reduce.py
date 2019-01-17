# 模拟ring reduce

import multiprocessing
import random
import time


# 伪代码
# 同时启动多个进程
# 各个进程模拟处理的状态 向自己下方的进程发送已完成的状态
# 各个进程只有收到上个进程的状态才会继续模拟处理的状态，否则会继续等待上个进程
# 直到收到消息才会继续进行，同时每个进程报告自己的处理状态
def single_part(init_random_method=random.randint(0, 4), recv_flag=1):
    a = init_random_method
    if recv_flag == 1:
        # 模拟处理状态
        time.sleep(a)
        #给自己下家进程发送消息  通知下家可以开始

        recv_flag == 0
    else:
        pass
    return print(a)


if __name__ == '__main__':
    single_part()

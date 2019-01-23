import random
from multiprocessing import Process, Queue
from time import sleep, time


def f(q_f, q_b, last_name, next_name, init_random=random.randint(0, 7)):
    step = 0
    while q_f.get() == 1:
        start_time = time()
        a = init_random
        sleep(a)
        step += 1
        print(q_f.qsize(), q_b.qsize())
        end_time = time() - start_time
        print("now step %d" % step,
              "| receive %s data and computing...." % last_name,
              "send data to %s" % next_name, "||cost time %d s" % end_time)
        # print('send data to %s'%q_b.__name__)
        if step == 10:
            break
        q_b.put(1)


def ring_reduce(num_node):
    Q_L = [Queue(maxsize=1) for i in range(0, num_node)]
    for i in range(num_node):
        Q_L[i].put(1)
    P_L = []
    for i in range(num_node):
        last_index = (i - 1 + num_node) % num_node
        next_index = (i + 1 + num_node) % num_node
        last_name = "node" + str(last_index)
        next_name = "node" + str(next_index)

        p = Process(target=f, args=(
            Q_L[last_index], Q_L[next_index], last_name, next_name))
        P_L.append(p)

    for i in range(num_node):
        P_L[i].start()
    for i in range(num_node):
        P_L[i].join()


if __name__ == '__main__':
    ring_reduce(8)
    #    q12,q23,q31=Queue(maxsize=1),Queue(maxsize=1),Queue(maxsize=1)
    #    q12.put(1)
    #    q23.put(1)
    #    q31.put(1)
    #
    #    p1 = Process(target=f, args=(q31,q12,"node3","node2"))
    #    p2 = Process(target=f, args=(q12,q23,"node1","node3"))
    #    p3 = Process(target=f, args=(q23,q31,"node2","node1",3))
    #    p1.start()
    #    p2.start()
    #    p3.start()
    #    p1.join()
    #    p2.join()
    #    p3.join()
    print("end")

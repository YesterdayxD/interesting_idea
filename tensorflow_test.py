import tensorflow as tf 
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--ps','-p',required=False,default='172.0.0.1:2222',type=str)
parser.add_argument('--worker','-w',required=False,default='172.0.0.1:2222',type=str)
args=parser.parse_args()
print(args.ps)
print(args.worker)

ps_spec= args.ps.split(',')
worker_spec= args.worker.split(',')
print(ps_spec)
print(worker_spec)


gpu_config = tf.ConfigProto(log_device_placement=True)
gpu_config.gpu_opitions.allow_growth=Ture
print(gpu_config)
from tensorflow.python.client import device_lib
 
print(device_lib.list_local_devices())

with tf.device('/cpu:0'):
    a=tf.constant(1,dtype=tf.float16)
    b=tf.constant(1,dtype=tf.float16)
with tf.device('/cpu:0'):
    c=b+a
with tf.Session(config=gpu_config) as sess:
    print(sess.run(c))
    

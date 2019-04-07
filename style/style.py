import tensorflow as tf
slim= tf.contrib.slim
print("finished!!!")
def arg_scope(weight_decay=0.0005):
    with slim.arg_scope([slim.conv2d,slim.fully_connected,slim.conv2d_transpose],
    activation=None,
    weight_regularizer=slim.l2_regularizer(weight_decay),
    biases_initilizer=tf.zeros_initializer()):
        with slim.arg_scope([slim.conv2d,slim.conv2d_transpose],padding='SAME') as arg_sc:
            return arg_sc
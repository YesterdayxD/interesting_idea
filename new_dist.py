from __future__ import absolute_import, division, print_function

import tensorflow as tf
import os
print(tf.__version__)

os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'

strategy = tf.contrib.distribute.MirroredStrategy(devices=['/device:CPU:0', '/device:GPU:0', '/device:GPU:1'])

with strategy.scope():
  inputs = tf.keras.layers.Input(shape=(1,))
  predictions = tf.keras.layers.Dense(1)(inputs)
  model = tf.keras.models.Model(inputs=inputs, outputs=predictions)
  model.compile(loss='mse',
                optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.2))

train_dataset = tf.data.Dataset.from_tensors(([1.], [1.])).repeat(10000).batch(10)
print(type(train_dataset))

# model.fit(train_dataset, epochs=5, steps_per_epoch=10)
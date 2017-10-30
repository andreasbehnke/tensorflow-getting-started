import os
import tensorflow as tf

with tf.Session() as sess:

    node1 = tf.constant(3.0, dtype=tf.float32, name="node1")
    node2 = tf.constant(4.0, name="node2")
    node3 = tf.add(node1, node2, name="node3")
    sess.run(node3)

    file_writer = tf.summary.FileWriter('tensorflow-logs', sess.graph)
    file_writer.close()

os.system("tensorboard --logdir tensorflow-logs")

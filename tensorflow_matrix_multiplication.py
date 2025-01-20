import tensorflow as tf

matrix1 = tf.constant([[5, 6], [7, 8]])
matrix2 = tf.constant([[9, 10], [11, 12]])
result = tf.matmul(matrix1, matrix2)

print(result)


# coding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np

class FastText(object):
    """ Implementation of the fasttext model. """
    def __init__(self, num_classes, embedding_dim, size_vocab, learning_rate):
        """Init the model with default parameters/hyperparameters."""
        self.num_classes = num_classes
        self.embedding_dim = embedding_dim
        self.size_vocab = size_vocab
        self.learning_rate = learning_rate
        
    def build_graph(self):
        """build the whole computation graph."""
        self.declare_placeholders()
        self.declare_variables()
        logit = self.inference()
        self.optimize(logit)
        self.predict(logit)
        self.compute_accuracy()
        
    def declare_placeholders(self): # Code from tutorial
        """ Declare the place holders here. Use tf.name_scope when possible."""
        # Label Tensor
        self.correct_label = tf.placeholder(tf.float32, shape=[self.num_classes, 1])
        # Sentence Tensor
        self.input_sens = tf.placeholder(tf.int32, shape=[None])
        
    def declare_variables(self):
        """ Declare the variables here. Use tf.name_scope when possible."""
        self.embeddings = tf.Variable(tf.random_uniform([self.size_vocab, self.embedding_dim], -1.0 / self.embedding_dim, 1.0 / self.embedding_dim))  # num_words * 10
        self.W = tf.Variable(tf.random_uniform([self.num_classes, self.embedding_dim], -1.0 / self.embedding_dim, 1.0 / self.embedding_dim))  # 3 * 10
        self.b = tf.Variable(tf.random_uniform([self.num_classes, 1], -1.0, 1.0))
        # self.embeddings = tf.Variable(tf.random_uniform([self.size_vocab, self.embedding_dim], -1.0, 1.0), name='embedding')

    def inference(self):
        """Compute the logit"""
        embed_new = tf.nn.embedding_lookup(self.embeddings, self.input_sens)  # Most of the code from the tutorial
        tmp = tf.reduce_mean(embed_new, 0)
        reshape =  tf.reshape(tmp, [self.embedding_dim, 1])
        return tf.matmul(self.W, reshape) + self.b

    def optimize(self, logit): # Help from tutor
        """Compute the logit. logit = W * h + b, where h is the mean of the word embedding in a sentence.
           Optionally you can also compute softmax(logit) here.
        """
        self.y =  tf.nn.softmax( logit, dim = 0)


    def compute_accuracy(self):
        """Evaluate the accuracy of the model against a test/validation set"""
        correct_prediction = tf.equal(self.prediction, tf.argmax(self.correct_label, 0))
        self.accuracy = tf.cast(correct_prediction, tf.float32, name = 'accuracy')
        
    def predict(self, logit):
        """ Predict label based on logit """
        self.prediction = tf.argmax(logit, 0)
    
    def loss(self, y):
        """Compute the cross entropy, given the logit."""
        self.cross_entropy= tf.reduce_mean(-tf.reduce_sum(self.correct_label * tf.log(self.y), reduction_indices=[0]))
        return self.cross_entropy

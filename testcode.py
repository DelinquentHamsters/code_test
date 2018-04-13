# coding: UTF-8
import sys
import numpy
import sklearn
import math
import matplotlib.pyplot as plt

# シグモイド関数
def sigmoid(a):
    return 1.0 / (1.0 + math.exp(-a))

# ニューロンクラス
class Neuron:
    input_sum =0.0
    output = 0.0

    def setInput(self,imp):
        self.input_sum +=imp

    def getOutpu(self):
        self.output = sigmoid(self.input_sum)
        return self.output

# ニューラルネットワーククラス
class NeuralNetwork:
    # 入力の重み
    w = [0.5,0.5,0.5]

    #ニューロンのインスタンス
    neuron = Neuron()
    #実行
    def commit(self,input_data):
        for data in input_data:
            self.neuron.setInput(data)
        return self.neuron.getOutpu()
            
# 基準点（データの範囲を0.0-1.0に)
refer_point_0 = 34.5
refer_point_1 = 137.5

# ファイル読み込み
trial_data = []
trial_data_file = open("C:/Users/2120191/Documents/GitHub/code_test/trial_data.txt","r")
for line in trial_data_file:
    line = line.rstrip().split(",")
    #データ加工
    trial_data.append([float(line[0]) - refer_point_0, float(line[1])- refer_point_1])
trial_data_file.close()

# ニューラルネットワークのインスタンス
neural_network = NeuralNetwork()

# 実行
position = [[],[]]
for data in trial_data:
    position[0].append(data[1] + refer_point_1)
    position[1].append(data[0] + refer_point_0)

# plot
plt.scatter(position[0],position[1], c="red",label="position",marker="+")
plt.legend()
plt.show()
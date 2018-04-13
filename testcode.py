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
    def reset(self):
        self.input_sum = 0
        self.output = 0

# ニューラルネットワーククラス
class NeuralNetwork:
    # 入力の重み
    w = [-0.5,0.5]

    #ニューロンのインスタンス
    neuron = Neuron()
    #実行
    def commit(self,input_data):
        self.neuron.reset()
        self.neuron.setInput(input_data[0]*self.w[0])
        self.neuron.setInput(input_data[1]*self.w[1])

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
position_tokyo = [[],[]]
position_kanagawa = [[],[]]
for data in trial_data:
    if neural_network.commit(data)<0.5:
        position_tokyo[0].append(data[1] + refer_point_1)
        position_tokyo[1].append(data[0] + refer_point_0)
    else:
        position_kanagawa[0].append(data[1] + refer_point_1)
        position_kanagawa[1].append(data[0] + refer_point_0)

# 散布図plot
plt.scatter(position_tokyo[0],position_tokyo[1], c="red",label="tokyo",marker="+")
plt.scatter(position_kanagawa[0],position_kanagawa[1], c="blue",label="kanagawa",marker="+")
plt.legend()
plt.show()
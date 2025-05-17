import torch
import torch.nn as nn
from mamba_ssm import Mamba
import numpy as np
import torch.optim as optim
import torch.nn.init as init
import math


max_seq_length = 200
batch_size=1
model_dim=768
learning_rate = 0.001
Crossentropy = nn.CrossEntropyLoss()
vocab_size=80000

class CustomLinear(nn.Linear):
    def __init__(self, in_features, out_features, bias=True):
        super(CustomLinear, self).__init__(in_features, out_features, bias)
        # 使用自定义的权重初始化方法
        init.kaiming_uniform_(self.weight, a=math.sqrt(5))
        if self.bias is not None:
            fan_in, _ = init._calculate_fan_in_and_fan_out(self.weight)
            bound = 1 / math.sqrt(fan_in)
            init.uniform_(self.bias, -bound, bound)
        self.bias.requires_grad = False
        for i in range(len(self.bias)):
            self.bias[i] = torch.tensor(0)
        # print(self.bias)
        self.bias.requires_grad = True
        
        self.weight.requires_grad=False
        for i in range(len(self.weight)):
            self.weight[i] = torch.tensor(0)
        self.weight.requires_grad=True
        # print(self.weight)
        # print(type(self.weight))

class Domain_pretraining(nn.Module):
    def __init__(self):
        super(Domain_pretraining, self).__init__()
        self.embed = nn.Embedding(vocab_size, 768).to("cuda:0")
        self.mamba_process = Mamba(d_model=768,d_state=128,d_conv=4,expand=2,).to("cuda:0")
        self.lstm = nn.LSTM(768,1,bidirectional=False).to("cuda:0")
        self.sigmoid = nn.Sigmoid().to("cuda:0")
        
    def forward(self,x):
        x_length = x.shape[1]
        embedding_out = self.embed(x)
        mamba_output = self.mamba_process(embedding_out)
        hidden_state = torch.zeros(1,x_length,1).to("cuda:0")
        cell_state = torch.zeros(1,x_length,1).to("cuda:0")
        label_output,(final_hidden_state,final_cell_state) = self.lstm(mamba_output,(hidden_state,cell_state))
        label_output = torch.squeeze(label_output)
        label_output = self.sigmoid(label_output)
        return mamba_output,label_output
        




if __name__=='__main__':
    train_batch=torch.randint(0,vocab_size,(batch_size,max_seq_length)).to("cuda:0")
    print(train_batch.shape)
    model = Domain_pretraining()
    mamba_output,label_output = model(train_batch)
    print("label output:",label_output.shape)
    print("mamba_output:",mamba_output.shape)

        
    
    
    

    

import torch

x = torch.empty(3)
#nums approaching zero
x = torch.rand(3)
#sheesh i think it might be random
x = torch.zeros(2,2)
#2*2 square filled with all zero
#also in torch.ones()
#(x)in 1d, (x,x)in 2d, (x,x,x)in 3d, and more plus
x = torch.add(a,b)
#make sure that a & b are in the same flame and then add them together one by one

print(x)


##

import torch
from torch import nn

class MLP(nn.Module):
	def __init__(self, **kwargs):
		#初始化模型的参数
		super(MLP, self).__init__(**kwargs)
		#父类构造函数正确初始化
		self.hidden = nn.Linear(14,64)#hidden隐藏层
		self.output = nn.Linear(64,3)#output输出层
		self.act = nn.ReLU()#ReLU激活函数
	
	def forward(self, x):
		x = self.hidden(x)
		x = self.act(x)
		x = self.output(x)
		return x
		#执行步骤
		
X = torch.rand(100,14)
model = MLP()
print(model)
print(model(X))


##

from torch import optim

criterion = nn.CrossEntropyLoss()
#损失函数min差距，计算损失更新权重
optimizer = optim.Adam(model.parameters(),lr=0.01)
#Adam优化算法，0.01学习率

##

for epoch in range(10):#进行10个周期
	for inputs,labels in train_loader:
		optimizer.zero_grad()
		#优化器清零（默认相加，故在循环中每个周期开始时需要return0）
		outputs = model(inputs)
		loss = criterion(outputs,labels)
		loss.backward()
		#回传数据，更新参数
		optimizer.step()
		#依据以上更新参数，每次循环进行迭代
		
with torch.no_grad():#喜报，把backward禁了
	for inputs,labels in test_loader:
		outputs = model(inputs)
		print(inputs)
		print(outputs)

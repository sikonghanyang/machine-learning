#1、用于训练模型的数据集称为训练集  用x表示输入变量，也称为特征或输入特征
#x="input" Variable also named feature
#y="output" variable      "target" variable
# (x,y) = single training example
#(x^(i),y^(i)) = i^th training example
# x --> f  --> y-hat:prediction
#f_w,b(x) = w x + b  w：权重 b：偏移量
#(y_hat - y )^2
#构建成本函数cost function J(w,b)=1/2m Σ(y_hat^(i)-y^(i))^2 ;此处的1/2是为了方便微分
#goal min（cost function) 
#
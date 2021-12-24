                                             《The case for learned index structures》论文的实现及其他机器学习索引模型的实现，如：B-Tree，Linear Regression，K-Nearest Neighbor，Naïve Bayes，Neural  Networks


这是我的大实验项目的第一部分
1.此部分工作介绍：
（1）实现了Kraska 等人在论文《The case for learned index structures》中提到的多层神经网学习索引模型。
（2）设计了其他学习索引模型如Linear Regression，K-Nearest Neighbor，Naïve Bayes，Neural  Networks，并将这些模型和传统的索引方法如B树做对比；
（3）在多种类型的数据集（一维数字、二维数字、字符串）中进行了实验测试，并且可以调整模型中的超参数。


2.环境：
-Python 3.7+
-Scikit-learn
-Tensorflow 2.0+
-Numpy
-Spacy
-chars2vec
确保您已在设备中安装这些环境，如果尚未安装这些软件包，可在命令行cmd中运行pip3 install [package name]指令来安装运行环境与包；同时如果你也需要在字符串数据集上运行各种学习索引结构，还应该执行以下命令：
                  python3 -m spacy download en_core_web_md
                  pip3 install keras-word-char-embd
                  pip3 install chars2vec


3.数据集介绍：
本实验项目中的数据集来源有两个：随机生成，来自 UCI 存储库
详细的数据集信息可以在dataset文件夹中看到（每个数据集包含一个训练集data.csv和一个测试集data_test.csv）


4.怎样运行代码
如果您想在 GPU/TPU 上运行实验，请确保您安装了正确版本的 Tensorflow。
如果你在正常的Windows主机上运行，可以直接点开code文件夹，然后单击鼠标右键选择将code文件在Windows终端中打开进入命令行模式。
（1）如果要对一维数字的数据集建立索引，请运行以下命令：
python3（或python） learned_index_1d_number.py -d [dataset path] -c [counting number] -p [hyper-parameter] -m [model name]
（2）如果要对多维数字的数据集建立索引，请运行以下命令：
python3（或python）learned_index_nd_number.py -d [dataset path] -c [counting number] -p [hyper-parameter] -m [model name]
（3）如果要对字符串的数据集建立索引，请运行以下命令：
python3（或python）learned_index_string.py -d [dataset path] -c [counting number] -p [hyper-parameter] -m [model name] -e [type]

参数说明：
-d:data.csv和data_test.csv存储的相对目录
-c: 代码执行多少次（必须是正整数）
-p：模型的超参数（不同模型有不同的超参数，有些可能没有）
-m: 选择的模型名称
-e:  字符串数据集的类型
参数要求：
模型                              -m的值           -p（超参）的要求
B-Tree                            BT                 integer, >=2（B树的度数）
Linear Regression           LR                省略（没有超参）
K-Nearest Neighbor      KNN              integer, >=1（K的取值）
Naïve Bayes                   NB                省略（没有超参）
Neural Networks           NN                 省略（没有超参）
另：-e参数只有在对字符串的数据集建立索引时才取值，否则省略
-e: 1 用于文本字符串；2 用于非文本字符串

5. 运行输入的命令举例
将code文件在Windows终端中打开进入命令行模式
（1）python3 （或python）learned_index_1d_number.py -d "..\dataset\single column number\random data\data_10k" -c 5 -p 5 -m BT
  (2)  python3 （或python）learned_index_nd_number.py -d "..\dataset\multiple column number\bike sharing data" -c 5 -p 5 -m KNN
  (3)  python3 （或python）learned_index_string.py -d "..\dataset\single column text\health news" -c 3 -m NN -e 1

6.文件功能说明
 (1)  code文件夹：存储本研究项目中的所有代码文件
random_generation.py : 用于生成随机数据集（我已生成一份）
test_generation.py : 一个测试代码文件，以确保每次生成不同的数据集
learn_index_1d_number.py：用于对一维数字进行索引实验
learn_index_nd_number.py : 用于多维数字进行索引实验
learn_index_string.py : 用于对一维字符串进行索引实验
learn_index_figures.py : 用于生成本项目的一些结果图表（可直接运行）
（2）dataset文件夹：存储本研究项目中使用的所有数据集
single column number: 一维数字的数据集
multiple column number: 多维数字的数据集
text string: 文本字符串数据集
non-text string: 非文本字符串的数据集
（3）image文件夹：
存储我的实验结果的一些图片（因为需要多次测试以及不同数据集及超参的结果）







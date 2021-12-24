                                             《XIndex: A Scalable Learned Index for Multicore Data Storage》论文的并发部分实现及对数据增删等更新操作的支持验证


这是我的大实验项目的第二部分
1.此部分工作介绍：
（1）实现了Tang 等人在论文《XIndex: A Scalable Learned Index for Multicore Data Storage》中提到的并发的学习索引XIndex
（2）设计并发的学习索引XIndex对数据更新的支持
（3）实现了XIndex的两种数据集查询方式（分别实现点查询XIndex-H和范围查询XIndex-R），并且在不同的数据集及不同的增删查操作比例下进行验证。


2.环境：
首先需要创建一个Linux虚拟机，将此文件夹共享到Linux虚拟机上。
在Linux虚拟机上该项目使用CMake (3.5+) 进行构建和测试，它还需要Intel MKL和jemalloc 的依赖项。
以下都是在Linux虚拟机命令行下运行：
（1）安装Intel MKL
$ cd /tmp
$ wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
$ apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
$ rm GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
$ sh -c 'echo deb https://apt.repos.intel.com/mkl all main > /etc/apt/sources.list.d/intel-mkl.list'
$ apt-get update
$ apt-get install -y intel-mkl-2019.0-045
安装完成后，请相应修改CMakeLists.txt（若已是这样则不用修改）：
set(MKL_LINK_DIRECTORY "/opt/intel/mkl/lib/intel64")
set(MKL_INCLUDE_DIRECTORY "/opt/intel/mkl/include")
（2）安装jemalloc
$ apt-get -y install libjemalloc1
$ cd /usr/lib/x86_64-linux-gnu/
$ ln -s libjemalloc.so.1 libjemalloc.so
安装后，请相应地修改以下行CMakeLists.txt（若已是这样则不用修改）：
set(JEMALLOC_DIR "/usr/lib/x86_64-linux-gnu")

3.构建和运行
（1）执行 XIndex-H
首先点开 XIndex-H文件夹，在我们XIndex-H文件夹内打开Linux终端，接下来使用 CMake 来构建 XIndex-H：
$ cmake . -DCMAKE_BUILD_TYPE=Release  # or -DCMAKE_BUILD_TYPE=Debug for more debug information
$ make microbench
运行微基准测试：
$ ./microbench
该microbench有几个参数可以传递，如read/write ratio，table size和XIndex-H的配置
所以运行指令也可以为：$ ./microbench --read 0.9 --insert 0.05 --remove 0.05 --table-size 100000等等
（2）执行 XIndex-R
首先点开 XIndex-R文件夹，在我们XIndex-R文件夹内打开Linux终端，接下来使用 CMake 来构建 XIndex-R：
$ cmake . -DCMAKE_BUILD_TYPE=Release  # or -DCMAKE_BUILD_TYPE=Debug for more debug information
$ make microbench
运行微基准测试：
$ ./microbench
该microbench有几个参数可以传递，如read/write ratio，table size和XIndex-H的配置
所以运行指令也可以为：$ ./microbench --read 0.9 --insert 0.05 --remove 0.05 --table-size 100000等等

4.文件夹说明
XIndex-H文件夹：实现了XIndex的数据集点查询方式
XIndex-R文件夹：实现了XIndex的数据集点范围查询方式



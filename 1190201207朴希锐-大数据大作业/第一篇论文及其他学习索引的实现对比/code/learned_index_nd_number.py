# -*- coding: utf-8 -*-

# Instructions

print("Learned Index Models, by piaoxirui")
print("This program comes with ABSOLUTELY NO WARRANTY;")
print("This is comparison of different learning indexes")
print("======================================================================================")

import sys, getopt

path = ''
count = 0
h_param = 0.0
model_str = ''
X_train=None
Y_train=None
Z_train=None
X_test=None
Y_test=None
Z_test=None
trainkeys = None
trainpages = None
trainres = None
testkeys = None
testpages = None
testres = None

def main(argv):
  global path
  global count
  global h_param
  global model_str
  try:
    opts, args = getopt.getopt(argv,"hd:c:p:m:",["directory=","count=","parameter=","model="])
  except getopt.GetoptError:
    print("Usage: [filename].py -d [dataset path] -c [counting number] -p [hyper-parameter] -m [model name]")
    exit(1)
  if len(opts) == 0:
    print("Usage: [filename].py -d [dataset path] -c [counting number] -p [hyper-parameter] -m [model name]")
    exit(1)
  for opt, arg in opts:
    if opt == '-h':
      print("Usage: [filename].py -d [dataset path] -c [counting number] -p [hyper-parameter] -m [model name]")
      exit()
    elif opt in ("-d", "--directory"):
      path = arg
    elif opt in ("-c", "--count"):
      count = int(arg)
    elif opt in ("-p", "--parameter"):
      h_param = float(arg)
    elif opt in ("-m", "--model"):
      model_str = arg
    else:
      print("Usage: [filename].py -d [dataset path] -c [counting number] -p [hyper-parameter] -m [model name]")
      exit(1)
if __name__ == "__main__":
   main(sys.argv[1:])




# Read Dataset

### read data

def process():
  import codecs
  import os
  global X_train
  global Y_train
  global Z_train
  global X_test
  global Y_test
  global Z_test
  global trainkeys 
  global trainpages 
  global trainres 
  global testkeys 
  global testpages 
  global testres 
  # minkey=1000
  # maxkey=9999
  # keynum=3000
  # current_path=os.path.abspath(os.curdir)
  f=codecs.open(os.path.join(path,"data.csv"), "r", "utf-8")
  strlist=f.read().split("\n")
  f.close()
  trainkeys=[]
  trainres=[]
  for ele in strlist:
      temp=ele.split(",")
      if len(temp)<2:
          continue
      trainkeys.append([float(temp[i]) for i in range(0,len(temp)-1)])
      trainres.append(int(temp[len(temp)-1]))

  f=codecs.open(os.path.join(path,"data_test.csv"), "r", "utf-8")
  strlist=f.read().split("\n")
  f.close()
  testkeys=[]
  testres=[]
  for ele in strlist:
      temp=ele.split(",")
      if len(temp)<2:
          continue
      testkeys.append([float(temp[i]) for i in range(0,len(temp)-1)])
      testres.append(int(temp[len(temp)-1]))



  print("training data size:",len(trainkeys))

  print("testing data size:",len(testkeys))

  """### data preprocessing"""

  trainpages=[]
  for ele in trainres:
    trainpages.append(int(ele)//100)
  testpages=[]
  for ele in testres:
    testpages.append(int(ele)//100)

  import numpy as np
  X_train=np.array(trainkeys)
  Y_train=np.array(trainres).reshape(-1,1)
  Z_train=np.array(trainpages).reshape(-1,1)
  X_test=np.array(testkeys)
  Y_test=np.array(testres).reshape(-1,1)
  Z_test=np.array(testpages).reshape(-1,1)

  import warnings
  from sklearn.exceptions import DataConversionWarning
  warnings.filterwarnings(action='ignore', category=DataConversionWarning)


"""## B-Tree"""



import time
class BTreeNode:
    '''
    B?????????
    '''
    def __init__(self, n = 0, isleaf = True):
        '''
        B?????????

        Args
        ===
        `n` : ??????????????????????????????

        `isleaf` : ?????????????????????

        '''
        # ??????????????????????????????
        self.n = n
        # ?????????????????????
        self.keys = []
        # ???????????????
        self.children = []
        # ?????????????????????
        self.isleaf = isleaf

    def __str__(self):

        returnStr = 'keys:['
        for i in range(self.n):
            returnStr += str(self.keys[i]) + ' '
        returnStr += '];childrens:['
        for child in self.children:
            returnStr += str(child) + ';'
        returnStr += ']\r\n'
        return returnStr

    def diskread(self):
        '''
        ?????????
        '''
        pass

    def diskwrite(self):
        '''
        ?????????
        '''
        pass

    @classmethod
    def allocate_node(self, key_max):
        '''
        ???O(1)????????????????????????????????????????????????

        ?????????ALLOCATE-NODE???????????????????????????DISK-READ?????????????????????????????????????????????????????????

        Return
        ===
        `btreenode` : ?????????B?????????

        Example
        ===
        ```python
        btreenode = BTreeNode.allocate_node()
        ```
        '''
        node = BTreeNode()
        child_max = key_max + 1
        for i in range(key_max):
            node.keys.append(None)
        for i in range(child_max):
            node.children.append(None)
        return node

class BTree:
    '''
    B???
    '''
    def __init__(self, m = 3):
        '''
        B????????????
        '''
        # B??????????????????
        self.M = m
        # ????????????????????????????????????
        self.KEY_MAX = 2 * self.M - 1
        # ??????????????????????????????????????????
        self.KEY_MIN = self.M - 1
        # ????????????????????????
        self.CHILD_MAX = self.KEY_MAX + 1
        # ????????????????????????
        self.CHILD_MIN = self.KEY_MIN + 1
        # ?????????
        self.root: BTreeNode = None

    def __new_node(self):
        '''
        ????????????B?????????
        '''
        return BTreeNode.allocate_node(self.KEY_MAX)

    def insert(self, key):
        '''
        ???B?????????????????????`key`  
        '''
        # ???????????????????????????
        if self.contain(key) == True:
            return False
        else:
            # ?????????????????????
            if self.root is None:
                node = self.__new_node()
                node.diskwrite()
                self.root = node    
            # ???????????????????????????      
            if self.root.n == self.KEY_MAX:
                # ?????????????????????
                pNode = self.__new_node()
                pNode.isleaf = False
                pNode.children[0] = self.root
                self.__split_child(pNode, 0, self.root)
                # ??????????????????
                self.root = pNode
            self.__insert_non_full(self.root, key)
            return True

    def remove(self, key): 
        '''
        ???B???????????????`key`
        '''      
        # ????????????????????????
        if not self.search(self.root, key):
            return False
        # ??????????????????
        if self.root.n == 1:
            if self.root.isleaf == True:
                self.clear()
            else:
                pChild1 = self.root.children[0]
                pChild2 = self.root.children[1]
                if pChild1.n == self.KEY_MIN and pChild2.n == self.KEY_MIN:
                    self.__merge_child(self.root, 0)
                    self.__delete_node(self.root)
                    self.root = pChild1
        self.__recursive_remove(self.root, key)
        return True
    
    def display(self):
        '''
        ?????????????????????  
        '''
        self.__display_in_concavo(self.root, self.KEY_MAX * 10)

    def contain(self, key):
        '''
        ?????????`key`???????????????B??????  
        '''
        self.__search(self.root, key)

    def clear(self):
        '''
        ??????B???  
        '''
        self.__recursive_clear(self.root)
        self.root = None

    def __recursive_clear(self, pNode : BTreeNode):
        '''
        ?????????  
        '''
        if pNode is not None:
            if not pNode.isleaf:
                for i in range(pNode.n):
                    self.__recursive_clear(pNode.children[i])
            self.__delete_node(pNode)

    def __delete_node(self, pNode : BTreeNode):
        '''
        ???????????? 
        '''
        if pNode is not None:
            pNode = None
    
    def __search(self, pNode : BTreeNode, key):
        '''
        ???????????????  
        '''
        # ???????????????????????????????????????????????????????????????
        if pNode is None:
            return False
        else:
            i = 0
            # ?????????key < pNode.keys[i]?????????????????????
            while i < pNode.n and key > pNode.keys[i]:
                i += 1
            if i < pNode.n and key == pNode.keys[i]:
                return True
            else:
                # ????????????????????????????????????
                if pNode.isleaf == True:
                    return False
                else:
                    return self.__search(pNode.children[i], key)

    def __split_child(self, pParent : BTreeNode, nChildIndex, pChild : BTreeNode):
        '''
        ???????????????
        '''
        # ???pChild?????????pLeftChild???pChild????????????
        pRightNode = self.__new_node()  # ?????????????????????
        pRightNode.isleaf = pChild.isleaf
        pRightNode.n = self.KEY_MIN
        # ?????????????????????
        for i in range(self.KEY_MIN):
            pRightNode.keys[i] = pChild.keys[i + self.CHILD_MIN]
        # ??????????????????????????????????????????????????????
        if not pChild.isleaf:
            for i in range(self.CHILD_MIN):
                pRightNode.children[i] = pChild.children[i + self.CHILD_MIN]
        # ?????????????????????????????????
        pChild.n = self.KEY_MIN
        # ??????????????????pChildIndex????????????????????????????????????????????????????????????
        for i in range(nChildIndex, pParent.n):
            j = pParent.n + nChildIndex - i
            pParent.children[j + 1] = pParent.children[j]
            pParent.keys[j] = pParent.keys[j - 1]
        # ?????????????????????????????????
        pParent.n += 1
        # ?????????????????????
        pParent.children[nChildIndex + 1] = pRightNode
        # ????????????????????????????????????
        pParent.keys[nChildIndex] = pChild.keys[self.KEY_MIN]
        pChild.diskwrite()
        pRightNode.diskwrite()
        pParent.diskwrite()
    
    def __insert_non_full(self, pNode: BTreeNode, key):
        '''
        ?????????????????????????????????
        '''
        # ??????????????????????????????
        i = pNode.n
        # ??????pNode???????????????
        if pNode.isleaf == True:
            # ???????????? ??????????????????????????????
            while i > 0 and key < pNode.keys[i - 1]:
                # ????????????
                pNode.keys[i] = pNode.keys[i - 1]
                i -= 1
            # ?????????????????????
            pNode.keys[i] = key
            # ??????????????????????????????
            pNode.n += 1
            pNode.diskwrite()
        # pnode????????????
        else:
            # ???????????? ?????????????????????????????????
            while i > 0 and key < pNode.keys[i - 1]:
                i -= 1
            # ????????????????????????
            pChild = pNode.children[i]
            pNode.children[i].diskread()
            # ????????????????????????
            if pChild.n == self.KEY_MAX:
                # ??????????????????
                self.__split_child(pNode, i, pChild)
                # ??????????????????
                if key > pNode.keys[i]:
                    pChild = pNode.children[i + 1]
            # ????????????????????????????????????
            self.__insert_non_full(pChild, key)

    def __display_in_concavo(self, pNode: BTreeNode, count):
        '''
        ?????????????????? 
        '''
        if pNode is not None:
            i = 0
            j = 0
            for i in range(pNode.n):
                if not pNode.isleaf:
                    self.__display_in_concavo(pNode.children[i], count - 2)
                for j in range(-1, count):
                    k = count - j - 1
                    print('-', end='')
                print(pNode.keys[i])
            if not pNode.isleaf:
                self.__display_in_concavo(pNode.children[i], count - 2)

    def __merge_child(self, pParent: BTreeNode, index):
        '''
        ?????????????????????
        '''
        pChild1 = pParent.children[index]
        pChild2 = pParent.children[index + 1]
        # ???pChild2???????????????pChild1
        pChild1.n = self.KEY_MAX
        # ????????????index????????????
        pChild1.keys[self.KEY_MIN] = pParent.keys[index]
        for i in range(self.KEY_MIN):
            pChild1.keys[i + self.KEY_MIN + 1] = pChild2.keys[i]
        if not pChild1.isleaf:
            for i in range(self.CHILD_MIN):
                pChild1.children[i + self.CHILD_MIN] = pChild2.children[i]
        # ???????????????index???key???index?????????????????????
        pParent.n -= 1
        for i in range(index, pParent.n):
            pParent.keys[i] = pParent.keys[i + 1]
            pParent.children[i + 1] = pParent.children[i + 2]
        # ??????pChild2
        self.__delete_node(pChild2)

    def __recursive_remove(self, pNode: BTreeNode, key):
        '''
        ????????????????????????`key`  
        '''
        i = 0
        while i < pNode.n and key > pNode.keys[i]:
            i += 1
        # ?????????key?????????pNode
        if i < pNode.n and key == pNode.keys[i]:
            # pNode???????????????
            if pNode.isleaf == True:
                # ???pNode?????????k
                for j in range(i, pNode.n):
                    pNode.keys[j] = pNode.keys[j + 1]
                return
            # pNode???????????????
            else:
                # ??????pNode?????????key????????????
                pChildPrev = pNode.children[i]
                # ??????pNode?????????key????????????
                pChildNext = pNode.children[i + 1]
                if pChildPrev.n >= self.CHILD_MIN:
                    # ??????key??????????????????
                    prevKey = self.predecessor(pChildPrev)
                    self.__recursive_remove(pChildPrev, prevKey)
                    # ?????????key??????????????????
                    pNode.keys[i] = prevKey
                    return
                # ??????pChildNext???????????????CHILD_MIN????????????
                elif pChildNext.n >= self.CHILD_MIN:
                    # ??????key??????????????????
                    nextKey = self.successor(pChildNext)
                    self.__recursive_remove(pChildNext, nextKey)
                    # ?????????key??????????????????
                    pNode.keys[i] = nextKey
                    return
                # ??????pChildPrev???pChildNext???????????????CHILD_MIN-1????????????
                else:
                    self.__merge_child(pNode, i)
                    self.__recursive_remove(pChildPrev, key)
        # ?????????key????????????pNode???
        else:
            # ??????key??????????????????
            pChildNode = pNode.children[i]
            # ??????t-1????????????
            if pChildNode.n == self.KEY_MAX:
                # ???????????????
                pLeft = None
                # ???????????????
                pRight = None
                # ???????????????
                if i > 0:
                    pLeft = pNode.children[i - 1]
                # ???????????????
                if i < pNode.n:
                    pRight = pNode.children[i + 1]
                j = 0
                if pLeft is not None and pLeft.n >= self.CHILD_MIN:
                    # ????????????i-1?????????????????????pChildNode???
                    for j in range(pChildNode.n):
                        k = pChildNode.n - j
                        pChildNode.keys[k] = pChildNode.keys[k - 1]
                    pChildNode.keys[0] = pNode.keys[i - 1]
                    if not pLeft.isleaf:
                        # pLeft????????????????????????????????????pChildNode???
                        for j in range(pChildNode.n + 1):
                            k = pChildNode.n + 1 - j
                            pChildNode.children[k] = pChildNode.children[k - 1]
                        pChildNode.children[0] = pLeft.children[pLeft.n]
                    pChildNode.n += 1
                    pNode.keys[i] = pLeft.keys[pLeft.n - 1]
                    pLeft.n -= 1
                # ????????????????????????CHILD_MIN????????????
                elif pRight is not None and pRight.n >= self.CHILD_MIN:
                    # ????????????i?????????????????????pChildNode???
                    pChildNode.keys[pChildNode.n] = pNode.keys[i]
                    pChildNode.n += 1
                    # pRight????????????????????????????????????pNode???
                    pNode.keys[i] = pRight.keys[0]
                    pRight.n -= 1
                    for j in range(pRight.n):
                        pRight.keys[j] = pRight.keys[j + 1]
                    if not pRight.isleaf:
                        # pRight???????????????????????????????????????pChildNode???
                        pChildNode.children[pChildNode.n] = pRight.children[0]
                        for j in range(pRight.n):
                            pRight.children[j] = pRight.children[j + 1]
                # ??????????????????????????????CHILD_MIN-1?????????
                elif pLeft is not None:
                    self.__merge_child(pNode, i - 1)
                    pChildNode = pLeft
                # ??????????????????
                elif pRight is not None:
                    self.__merge_child(pNode, i)
            self.__recursive_remove(pChildNode, key)

    def predecessor(self, pNode: BTreeNode):
        '''
        ???????????????
        '''
        while not pNode.isleaf:
            pNode = pNode.children[pNode.n]
        return pNode.keys[pNode.n - 1]

    def successor(self, pNode: BTreeNode):
        '''
        ???????????????
        '''
        while not pNode.isleaf:
            pNode = pNode.children[0]
        return pNode.keys[0]

def test_BTree(hp:int):
    '''
    test class `BTree` and class `BTreeNode`
    '''
    tree = BTree(hp)
    
    t1=time.time()
    for i in range(0,len(trainkeys)):
        tree.insert(trainkeys[i])
    t2=time.time()
    time_interval=t2-t1
    print("time interval for building model:"+str(time_interval*1000)+" ms")
    ret1=time_interval*1000
    t1=time.time()
    
    for i in range(0,len(testkeys)):
        tree.contain(testkeys[i])
    t2=time.time()
    time_interval=t2-t1
    print("time interval for indexing data :"+str(time_interval*1000)+" ms")
    print("average time interval for indexing data :"+str(time_interval/len(testkeys)*1000)+" ms")
    ret2=time_interval*1000
    ret3=time_interval/len(testkeys)*1000
    return (ret1,ret2,ret3)

def model_BT(counting:int,hp:int):
    avg_a=0.0
    avg_b=0.0
    avg_c=0.0
    # counting=20
    for i in range(0,counting):
        (a,b,c)=test_BTree(hp)
        avg_a+=a
        avg_b+=b
        avg_c+=c
    avg_a=avg_a/counting
    avg_b=avg_b/counting
    avg_c=avg_c/counting
    print("average times (ms):",avg_a,avg_b,avg_c)
    return


"""## Linear Regression"""


# print("Linear Regression Model")
def test_LR():
  from sklearn.linear_model import LinearRegression
  import numpy as np
  from sklearn.metrics import mean_squared_error 
  import math
  import time
  t1=time.time()
  reg = LinearRegression()
  reg.fit(X_train,Y_train)
  t2=time.time()
  time_interval=t2-t1
  print("time interval for building model:"+str(time_interval*1000)+" ms")
  ret1=time_interval*1000
  
  t1=time.time()
  testpre=reg.predict(X_test).reshape(1,-1).tolist()[0]
  for i in range(0,len(testpre)):
    testpre[i]=abs(int(testpre[i]))
  t2=time.time()
  time_interval=t2-t1
  print("time interval for indexing data :"+str(time_interval*1000)+" ms")
  print("average time interval for indexing data :"+str(time_interval/len(testkeys)*1000)+" ms")
  ret2=time_interval*1000
  ret3=time_interval/len(testkeys)*1000
  
  t1=time.time()
  count_error=0
  for i in range(0,len(testpre)):
    estimated_loc=testpre[i]
    correct_res=testres[i]
    if estimated_loc>=0 and estimated_loc<len(trainkeys):
      finding_res=trainres[estimated_loc]
    elif estimated_loc<0:
      finding_res=trainres[0]
    else:
      finding_res=trainres[len(trainkeys)-1]
    if finding_res!=correct_res:
      count_error+=1
    begin=0
    end=len(trainkeys)-1
    while finding_res!=correct_res and abs(finding_res-correct_res)>1:
      
      
      if finding_res<correct_res:
        begin=estimated_loc
        
        estimated_loc=(begin+end)//2
        if estimated_loc>=0 and estimated_loc<len(trainkeys):
          finding_res=trainres[estimated_loc]
        elif estimated_loc<0:
          finding_res=trainres[0]
        else:
          finding_res=trainres[len(trainkeys)-1]
      else:
        
        end=estimated_loc
        estimated_loc=(begin+end)//2
        if estimated_loc>=0 and estimated_loc<len(trainkeys):
          finding_res=trainres[estimated_loc]
        elif estimated_loc<0:
          finding_res=trainres[0]
        else:
          finding_res=trainres[len(trainkeys)-1]
    
  t2=time.time()
  time_interval=t2-t1
  print("time interval for error correction :"+str(time_interval*1000)+" ms")
  print("average time interval for error correction :"+str(time_interval/count_error*1000)+" ms")
  ret4=time_interval*1000
  ret5=time_interval/len(testkeys)*1000
  return (ret1,ret2,ret3,ret4,ret5)

def model_LR(counting:int):
  avg_a=0.0
  avg_b=0.0
  avg_c=0.0
  avg_d=0.0
  avg_e=0.0
  # counting=20
  for i in range(0,counting):
    (a,b,c,d,e)=test_LR()
    avg_a+=a
    avg_b+=b
    avg_c+=c
    avg_d+=d
    avg_e+=e
  avg_a=avg_a/counting
  avg_b=avg_b/counting
  avg_c=avg_c/counting
  avg_d=avg_d/counting
  avg_e=avg_e/counting
  print("average times (ms):",avg_a,avg_b,avg_c,avg_d,avg_e)
  return

"""## Ridge Regression"""


def test_RR(hp:float):
  from sklearn.linear_model import Ridge
  import numpy as np
  from sklearn.metrics import mean_squared_error 
  import math
  import time
  t1=time.time()
  reg = Ridge(alpha=hp)
  reg.fit(X_train,Y_train)
  t2=time.time()
  time_interval=t2-t1
  print("time interval for building model:"+str(time_interval*1000)+" ms")
  ret1=time_interval*1000
  
  t1=time.time()
  testpre=reg.predict(X_test).reshape(1,-1).tolist()[0]
  for i in range(0,len(testpre)):
    testpre[i]=abs(int(testpre[i]))
  t2=time.time()
  time_interval=t2-t1
  print("time interval for indexing data :"+str(time_interval*1000)+" ms")
  print("average time interval for indexing data :"+str(time_interval/len(testkeys)*1000)+" ms")
  ret2=time_interval*1000
  ret3=time_interval/len(testkeys)*1000
  
  t1=time.time()
  count_error=0
  for i in range(0,len(testpre)):
    estimated_loc=testpre[i]
    correct_res=testres[i]
    if estimated_loc>=0 and estimated_loc<len(trainkeys):
      finding_res=trainres[estimated_loc]
    elif estimated_loc<0:
      finding_res=trainres[0]
    else:
      finding_res=trainres[len(trainkeys)-1]
    if finding_res!=correct_res:
      count_error+=1
    begin=0
    end=len(trainkeys)-1
    while finding_res!=correct_res and abs(finding_res-correct_res)>1:
      
      
      if finding_res<correct_res:
        begin=estimated_loc
        
        estimated_loc=(begin+end)//2
        if estimated_loc>=0 and estimated_loc<len(trainkeys):
          finding_res=trainres[estimated_loc]
        elif estimated_loc<0:
          finding_res=trainres[0]
        else:
          finding_res=trainres[len(trainkeys)-1]
      else:
        
        end=estimated_loc
        estimated_loc=(begin+end)//2
        if estimated_loc>=0 and estimated_loc<len(trainkeys):
          finding_res=trainres[estimated_loc]
        elif estimated_loc<0:
          finding_res=trainres[0]
        else:
          finding_res=trainres[len(trainkeys)-1]
    
  t2=time.time()
  time_interval=t2-t1
  print("time interval for error correction :"+str(time_interval*1000)+" ms")
  print("average time interval for error correction :"+str(time_interval/count_error*1000)+" ms")
  ret4=time_interval*1000
  ret5=time_interval/count_error*1000
  return (ret1,ret2,ret3,ret4,ret5)

def model_RR(counting:int,hp:float):
  avg_a=0.0
  avg_b=0.0
  avg_c=0.0
  avg_d=0.0
  avg_e=0.0
  # counting=20
  for i in range(0,counting):
    (a,b,c,d,e)=test_RR(hp)
    avg_a+=a
    avg_b+=b
    avg_c+=c
    avg_d+=d
    avg_e+=e
  avg_a=avg_a/counting
  avg_b=avg_b/counting
  avg_c=avg_c/counting
  avg_d=avg_d/counting
  avg_e=avg_e/counting
  print("average times (ms):",avg_a,avg_b,avg_c,avg_d,avg_e)
  return

"""## KNN"""


def test_KNN(hp:int):
  from sklearn.neighbors import KNeighborsClassifier
  import time
  import numpy as np
  from sklearn.metrics import classification_report
  t1=time.time()
  neigh = KNeighborsClassifier(n_neighbors=hp)
  neigh.fit(X_train,Z_train)
  t2=time.time()
  time_interval=t2-t1
  
  ret1=time_interval*1000
  t1=time.time()
  testpre=neigh.predict(X_test).reshape(1,-1).tolist()[0]
  
  t2=time.time()
  time_interval=t2-t1
  print("time interval for indexing data :"+str(time_interval*1000)+" ms")
  print("average time interval for indexing data :"+str(time_interval/len(testkeys)*1000)+" ms")
  ret2=time_interval*1000
  ret3=time_interval/len(testkeys)*1000
  t1=time.time()
  count_error=0
  for i in range(0,len(testpre)):
    estimated_page=testpre[i]
    estimated_loc = estimated_page*100+50
    correct_res=testres[i]
    if estimated_loc>=0 and estimated_loc<len(trainkeys):
        finding_res=trainres[estimated_loc]
    elif estimated_loc<0:
        finding_res=trainres[0]
    else:
        finding_res=trainres[len(trainkeys)-1]
    if finding_res!=correct_res:
      count_error+=1
    begin=0
    end=len(trainkeys)-1
    while finding_res!=correct_res and abs(finding_res-correct_res)>1:
      
      
      if finding_res<correct_res:
        begin=estimated_loc
        
        estimated_loc=(begin+end)//2
        if estimated_loc>=0 and estimated_loc<len(trainkeys):
          finding_res=trainres[estimated_loc]
        elif estimated_loc<0:
          finding_res=trainres[0]
        else:
          finding_res=trainres[len(trainkeys)-1]
      else:
        
        end=estimated_loc
        estimated_loc=(begin+end)//2
        if estimated_loc>=0 and estimated_loc<len(trainkeys):
          finding_res=trainres[estimated_loc]
        elif estimated_loc<0:
          finding_res=trainres[0]
        else:
          finding_res=trainres[len(trainkeys)-1]
  t2=time.time()
  time_interval=t2-t1
  print("time interval for error correction :"+str(time_interval*1000)+" ms")
  print("average time interval for error correction :"+str(time_interval/count_error*1000)+" ms")
  ret4=time_interval*1000
  ret5=time_interval/len(testkeys)*1000
  return (ret1,ret2,ret3,ret4,ret5)

def model_KNN(counting:int,hp:int):
  avg_a=0.0
  avg_b=0.0
  avg_c=0.0
  avg_d=0.0
  avg_e=0.0
  # counting=20
  for i in range(0,counting):
    (a,b,c,d,e)=test_KNN(hp)
    avg_a+=a
    avg_b+=b
    avg_c+=c
    avg_d+=d
    avg_e+=e
  avg_a=avg_a/counting
  avg_b=avg_b/counting
  avg_c=avg_c/counting
  avg_d=avg_d/counting
  avg_e=avg_e/counting
  print("average times (ms):",avg_a,avg_b,avg_c,avg_d,avg_e)
  return

"""## Naive Bayes"""


def test_NB():
  from sklearn.naive_bayes import GaussianNB
  import time
  import numpy as np
  from sklearn.metrics import classification_report
  t1=time.time()
  NB = GaussianNB()
  NB.fit(X_train,Z_train)
  t2=time.time()
  time_interval=t2-t1
  
  print("time interval for building model:"+str(time_interval*1000)+" ms")
  ret1=time_interval*1000
  t1=time.time()
  testpre=NB.predict(X_test).reshape(1,-1).tolist()[0]
  t2=time.time()
  time_interval=t2-t1
  print("time interval for indexing data :"+str(time_interval*1000)+" ms")
  print("average time interval for indexing data :"+str(time_interval/len(testkeys)*1000)+" ms")
  ret2=time_interval*1000
  ret3=time_interval/len(testkeys)*1000
  t1=time.time()
  count_error=0
  for i in range(0,len(testpre)):
    estimated_page=testpre[i]
    estimated_loc = estimated_page*100+50
    correct_res=testres[i]
    if estimated_loc>=0 and estimated_loc<len(trainkeys):
        finding_res=trainres[estimated_loc]
    elif estimated_loc<0:
        finding_res=trainres[0]
    else:
        finding_res=trainres[len(trainkeys)-1]
    if finding_res!=correct_res:
      count_error+=1
    begin=0
    end=len(trainkeys)-1
    while finding_res!=correct_res and abs(finding_res-correct_res)>1:
      
      
      if finding_res<correct_res:
        begin=estimated_loc
        
        estimated_loc=(begin+end)//2
        if estimated_loc>=0 and estimated_loc<len(trainkeys):
          finding_res=trainres[estimated_loc]
        elif estimated_loc<0:
          finding_res=trainres[0]
        else:
          finding_res=trainres[len(trainkeys)-1]
      else:
        
        end=estimated_loc
        estimated_loc=(begin+end)//2
        if estimated_loc>=0 and estimated_loc<len(trainkeys):
          finding_res=trainres[estimated_loc]
        elif estimated_loc<0:
          finding_res=trainres[0]
        else:
          finding_res=trainres[len(trainkeys)-1]
  t2=time.time()
  time_interval=t2-t1
  print("time interval for error correction :"+str(time_interval*1000)+" ms")
  print("average time interval for error correction :"+str(time_interval/count_error*1000)+" ms")
  ret4=time_interval*1000
  ret5=time_interval/len(testkeys)*1000
  return (ret1,ret2,ret3,ret4,ret5)

def model_NB(counting:int):
  avg_a=0.0
  avg_b=0.0
  avg_c=0.0
  avg_d=0.0
  avg_e=0.0
  # counting=20
  for i in range(0,counting):
    (a,b,c,d,e)=test_NB()
    avg_a+=a
    avg_b+=b
    avg_c+=c
    avg_d+=d
    avg_e+=e
  avg_a=avg_a/counting
  avg_b=avg_b/counting
  avg_c=avg_c/counting
  avg_d=avg_d/counting
  avg_e=avg_e/counting
  print("average times (ms):",avg_a,avg_b,avg_c,avg_d,avg_e)

"""## Decision Tree"""


def test_DT(hp:int):
  from sklearn import tree
  import time
  import numpy as np
  from sklearn.metrics import classification_report
  t1=time.time()
  dtree = tree.DecisionTreeClassifier(max_depth=hp)
  dtree.fit(X_train,Z_train)
  t2=time.time()
  time_interval=t2-t1
  
  print("time interval for building model:"+str(time_interval*1000)+" ms")
  ret1=time_interval*1000
  t1=time.time()
  testpre=dtree.predict(X_test).reshape(1,-1).tolist()[0]
  t2=time.time()
  time_interval=t2-t1
  print("time interval for indexing data :"+str(time_interval*1000)+" ms")
  print("average time interval for indexing data :"+str(time_interval/len(testkeys)*1000)+" ms")
  ret2=time_interval*1000
  ret3=time_interval/len(testkeys)*1000
  t1=time.time()
  count_error=0
  for i in range(0,len(testpre)):
    estimated_page=testpre[i]
    estimated_loc = estimated_page*100+50
    correct_res=testres[i]
    if estimated_loc>=0 and estimated_loc<len(trainkeys):
        finding_res=trainres[estimated_loc]
    elif estimated_loc<0:
        finding_res=trainres[0]
    else:
        finding_res=trainres[len(trainkeys)-1]
    if finding_res!=correct_res:
      count_error+=1
    begin=0
    end=len(trainkeys)-1
    while finding_res!=correct_res and abs(finding_res-correct_res)>1:
      
      
      if finding_res<correct_res:
        begin=estimated_loc
        
        estimated_loc=(begin+end)//2
        if estimated_loc>=0 and estimated_loc<len(trainkeys):
          finding_res=trainres[estimated_loc]
        elif estimated_loc<0:
          finding_res=trainres[0]
        else:
          finding_res=trainres[len(trainkeys)-1]
      else:
        
        end=estimated_loc
        estimated_loc=(begin+end)//2
        if estimated_loc>=0 and estimated_loc<len(trainkeys):
          finding_res=trainres[estimated_loc]
        elif estimated_loc<0:
          finding_res=trainres[0]
        else:
          finding_res=trainres[len(trainkeys)-1]
  t2=time.time()
  time_interval=t2-t1
  print("time interval for error correction :"+str(time_interval*1000)+" ms")
  print("average time interval for error correction :"+str(time_interval/count_error*1000)+" ms")
  ret4=time_interval*1000
  ret5=time_interval/len(testkeys)*1000
  return (ret1,ret2,ret3,ret4,ret5)

def model_DT(counting:int,hp:int):
  avg_a=0.0
  avg_b=0.0
  avg_c=0.0
  avg_d=0.0
  avg_e=0.0
  # counting=20
  for i in range(0,counting):
    (a,b,c,d,e)=test_DT(hp)
    avg_a+=a
    avg_b+=b
    avg_c+=c
    avg_d+=d
    avg_e+=e
  avg_a=avg_a/counting
  avg_b=avg_b/counting
  avg_c=avg_c/counting
  avg_d=avg_d/counting
  avg_e=avg_e/counting
  print("average times (ms):",avg_a,avg_b,avg_c,avg_d,avg_e)
  return

"""## Neural Networks"""





def test_NN():
  import tensorflow as tf
  from tensorboard.plugins.hparams import api
  from keras import models as md
  from keras import layers as lr
  import time
  import numpy as np
  from sklearn.metrics import classification_report
  temp=Z_train.reshape(1,-1)
  T_train=np.zeros((temp.size, temp.max()+1))
  T_train[np.arange(temp.size),temp] = 1
  # print(T_train)
  # print(X_train.shape)
  t1=time.time()
  model = md.Sequential()
  model.add(lr.Dense(1,activation="relu"))
  # model.add(lr.Dense(4,activation="relu"))
  model.add(lr.Dense(128,activation="relu"))
  # model.add(lr.Dropout(0.2))
  model.add(lr.Dense(temp.max()+1,activation="softmax"))
  model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])#compile the model
  model.fit(X_train, T_train, epochs=16, batch_size=32)#fit the model
  t2=time.time()
  time_interval=t2-t1
  
  print("time interval for building model:"+str(time_interval*1000)+" ms")
  ret1=time_interval*1000
  t1=time.time()
  testpre=model.predict(X_test)#.reshape(1,-1).tolist()[0]
  testpre=np.argmax(testpre,axis=1)
  
  t2=time.time()
  time_interval=t2-t1
  print("time interval for indexing data :"+str(time_interval*1000)+" ms")
  print("average time interval for indexing data :"+str(time_interval/len(testkeys)*1000)+" ms")
  
  ret2=time_interval*1000
  ret3=time_interval/len(testkeys)*1000
  t1=time.time()
  count_error=0
  for i in range(0,len(testpre)):
    estimated_page=testpre[i]
    estimated_loc = estimated_page*100+50
    correct_res=testres[i]
    if estimated_loc>=0 and estimated_loc<len(trainkeys):
        finding_res=trainres[estimated_loc]
    elif estimated_loc<0:
        finding_res=trainres[0]
    else:
        finding_res=trainres[len(trainkeys)-1]
    if finding_res!=correct_res:
      count_error+=1
    begin=0
    end=len(trainkeys)-1
    while finding_res!=correct_res and abs(finding_res-correct_res)>1:
      
      
      if finding_res<correct_res:
        begin=estimated_loc
        
        estimated_loc=(begin+end)//2
        if estimated_loc>=0 and estimated_loc<len(trainkeys):
          finding_res=trainres[estimated_loc]
        elif estimated_loc<0:
          finding_res=trainres[0]
        else:
          finding_res=trainres[len(trainkeys)-1]
      else:
        
        end=estimated_loc
        estimated_loc=(begin+end)//2
        if estimated_loc>=0 and estimated_loc<len(trainkeys):
          finding_res=trainres[estimated_loc]
        elif estimated_loc<0:
          finding_res=trainres[0]
        else:
          finding_res=trainres[len(trainkeys)-1]
  t2=time.time()
  time_interval=t2-t1
  print("time interval for error correction :"+str(time_interval*1000)+" ms")
  print("average time interval for error correction :"+str(time_interval/count_error*1000)+" ms")
  ret4=time_interval*1000
  ret5=time_interval/len(testkeys)*1000
  return (ret1,ret2,ret3,ret4,ret5)

def model_NN(counting:int):
  avg_a=0.0
  avg_b=0.0
  avg_c=0.0
  avg_d=0.0
  avg_e=0.0
  # counting=20
  for i in range(0,counting):
    (a,b,c,d,e)=test_NN()
    avg_a+=a
    avg_b+=b
    avg_c+=c
    avg_d+=d
    avg_e+=e
  avg_a=avg_a/counting
  avg_b=avg_b/counting
  avg_c=avg_c/counting
  avg_d=avg_d/counting
  avg_e=avg_e/counting
  print("average times (ms):",avg_a,avg_b,avg_c,avg_d,avg_e)
  return


process()

print("==============Preperocess Completed============")

if model_str == 'BT':
  model_BT(count,int(h_param))
elif model_str == 'LR':
  model_LR(count)
elif model_str == 'RR':
  model_RR(count,h_param)
elif model_str == 'KNN':
  model_KNN(count,int(h_param))
elif model_str == 'NB':
  model_NB(count)
elif model_str == 'DT':
  model_DT(count,int(h_param))
elif model_str == 'NN':
  model_NN(count)
else:
  print("Error: Invalid Model")
  sys.exit(1)
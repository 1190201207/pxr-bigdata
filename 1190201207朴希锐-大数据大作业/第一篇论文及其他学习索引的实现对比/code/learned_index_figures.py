# -*- coding: utf-8 -*-
"""learned_index_figures.ipynb


This notebook is used for generating figures in project learned index structures.

## Import packages
"""
print("Learned Index Models, by piaoxirui")
print("This program comes with ABSOLUTELY NO WARRANTY;")
print("This is comparison of different learning indexes")
print("======================================================================================")
import matplotlib.pyplot as plt
import numpy as np

"""## Start Generating Figures

### Single Column Numbers Indexing

#### B-Tree
"""

bottom_list = ['3','4','5','6','7','8','9','10']
res_list1 = [139.5875931,129.8464537,115.6086683,109.2769265,105.2844644,98.39254618,105.1092267,103.8674712]
res_list2 = [20.84536552,18.76618862,18.15875769,17.7090168,17.00015068,16.85439348,16.78961515,17.62440205]
x =list(range(len(res_list1)))
total_width, n = 0.6, 2
width = total_width / n
 
plt.bar(x, res_list1, width=width, label='creation time',fc = 'y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list2, width=width, label='look-up time',tick_label = bottom_list,fc = 'r')

plt.title('B-Tree Performance Chart (Random Data, size:10k)')
plt.xlabel('degree of B-Tree')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

bottom_list = ['3','4','5','6','7','8','9','10']
res_list1 = [464.3626809,370.4710364,347.3912358,345.6935883,334.0625405,350.1921058,342.0792341,350.9931922]
res_list2 = [73.40781689,57.78639317,57.30978251,57.50311613,54.34116125,56.26904964,53.32070589,58.18823576]
x =list(range(len(res_list1)))
total_width, n = 0.6, 2
width = total_width / n
 
plt.bar(x, res_list1, width=width, label='creation time',fc = 'y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list2, width=width, label='look-up time',tick_label = bottom_list,fc = 'r')

plt.title('B-Tree Performance Chart (Random Data, size:30k)')
plt.xlabel('degree of B-Tree')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

bottom_list = ['3','4','5','6','7','8','9','10']
res_list1 = [793.9297438,655.0346136,614.3287778,595.3386188,593.7197089,582.7657342,597.2927094,608.2878709]
res_list2 = [135.9722376,110.5522871,108.7019205,107.6374292,107.9795241,102.4820328,102.8325796,106.6941261]
x =list(range(len(res_list1)))
total_width, n = 0.6, 2
width = total_width / n
 
plt.bar(x, res_list1, width=width, label='creation time',fc = 'y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list2, width=width, label='look-up time',tick_label = bottom_list,fc = 'r')

plt.title('B-Tree Performance Chart (Random Data, size:50k)')
plt.xlabel('degree of B-Tree')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

bottom_list = ['3','4','5','6','7','8','9','10']
res_list1 = [1548.034191,1121.301508,1044.108081,1020.44729,1007.341957,1000.681329,1004.441452,1025.207722]
res_list2 = [260.084331,193.149519,188.9408231,188.6917472,183.3536744,183.4278822,182.1617603,180.8934212]
x =list(range(len(res_list1)))
total_width, n = 0.6, 2
width = total_width / n
 
plt.bar(x, res_list1, width=width, label='creation time',fc = 'y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list2, width=width, label='look-up time',tick_label = bottom_list,fc = 'r')

plt.title('B-Tree Performance Chart (Random Data, size:80k)')
plt.xlabel('degree of B-Tree')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

bottom_list = ['3','4','5','6','7','8','9','10']
res_list1 = [1693.082881,1375.005567,1287.181401,1258.440018,1254.439914,1254.503226,1254.530728,1280.195928]
res_list2 = [296.0122824,242.5850153,241.7551279,241.9775009,232.2111964,229.5351624,235.808146,232.2704077]
x =list(range(len(res_list1)))
total_width, n = 0.6, 2
width = total_width / n
 
plt.bar(x, res_list1, width=width, label='creation time',fc = 'y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list2, width=width, label='look-up time',tick_label = bottom_list,fc = 'r')

plt.title('B-Tree Performance Chart (Random Data, size:100k)')
plt.xlabel('degree of B-Tree')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

bottom_list = ['3','4','5','6','7','8','9','10']
res_list1 = [5570.952415,4681.018543,4360.188735,4396.883643,4195.305312,4115.707123,4199.004185,4285.306466]
res_list2 = [1108.959973,926.1843204,928.8270473,929.1199803,929.7836423,865.9741044,855.3031683,901.6337514]
x =list(range(len(res_list1)))
total_width, n = 0.6, 2
width = total_width / n
 
plt.bar(x, res_list1, width=width, label='creation time',fc = 'y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list2, width=width, label='look-up time',tick_label = bottom_list,fc = 'r')

plt.title('B-Tree Performance Chart (Random Data, size:300k)')
plt.xlabel('degree of B-Tree')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

"""#### Ridge Regression"""

x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
y1=[1.955509186,1.793408394,1.83955431,1.714193821,1.9089818,1.827251911,1.965045929,1.704871655,1.665067673,1.732432842]
y2=[1.478338242,1.364910603,1.410198212,1.416623592,1.414191723,1.35024786,1.458859444,1.385569572,1.382315159,1.50179863]
y3=[13.96714449,13.59815598,13.32600117,14.2749548,13.4510994,13.64617348,13.60645294,13.49704266,13.29748631,15.45089483]

l1=plt.plot(x,y1,'r--',label='creation time')
l2=plt.plot(x,y2,'g--',label='look-up time')
l3=plt.plot(x,y3,'b--',label='error-correction time')
plt.plot(x,y1,'ro-',x,y2,'go-',x,y3,'bo-')

plt.title('Ridge Regression Performance Chart (Random Data, size:10k)')
plt.xlabel(r'$\lambda$')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
y1=[1.796734333,2.080786228,1.977622509,1.903808117,1.978754997,1.61036253,1.906049252,2.395677567,3.125989437,4.656469822]
y2=[5.54612875,5.694723129,5.590355396,5.722641945,5.884301662,5.551683903,5.519628525,5.420136452,5.346846581,8.088767529]
y3=[89.54124451,89.15843964,87.9699111,86.624825,89.61678743,88.31157684,88.08146715,86.67855263,87.50708103,94.96427774]

l1=plt.plot(x,y1,'r--',label='creation time')
l2=plt.plot(x,y2,'g--',label='look-up time')
l3=plt.plot(x,y3,'b--',label='error-correction time')
plt.plot(x,y1,'ro-',x,y2,'go-',x,y3,'bo-')

plt.title('Ridge Regression Performance Chart (Random Data, size:30k)')
plt.xlabel(r'$\lambda$')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
y1=[2.464675903,2.184522152,2.207350731,2.113473415,2.331650257,2.256214619,2.419281006,2.690434456,4.981136322,2.520728111]
y2=[8.830559254,8.720934391,8.728373051,8.742010593,8.754789829,9.003806114,8.775281906,8.777546883,9.828364849,9.138596058]
y3=[150.154984,147.4597573,147.8938818,148.0935335,146.6283917,147.7205873,147.2584844,147.5887895,165.578258,147.8530288]

l1=plt.plot(x,y1,'r--',label='creation time')
l2=plt.plot(x,y2,'g--',label='look-up time')
l3=plt.plot(x,y3,'b--',label='error-correction time')
plt.plot(x,y1,'ro-',x,y2,'go-',x,y3,'bo-')

plt.title('Ridge Regression Performance Chart (Random Data, size:50k)')
plt.xlabel(r'$\lambda$')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
y1=[8.535134792,5.391633511,3.422892094,4.35167551,5.952465534,4.169332981,4.92361784,4.386925697,5.924141407,2.849245071]
y2=[14.06077147,14.10657167,14.4898057,14.17105198,14.24816847,14.69753981,14.05142546,14.67235088,14.92558718,15.12761116]
y3=[216.0603285,222.7684021,232.8243971,231.7257762,221.3906288,231.7206383,220.6510186,230.0902843,221.5123296,220.4671621]

l1=plt.plot(x,y1,'r--',label='creation time')
l2=plt.plot(x,y2,'g--',label='look-up time')
l3=plt.plot(x,y3,'b--',label='error-correction time')
plt.plot(x,y1,'ro-',x,y2,'go-',x,y3,'bo-')

plt.title('Ridge Regression Performance Chart (Random Data, size:80k)')
plt.xlabel(r'$\lambda$')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
y1=[2.869606018,2.970016003,2.777540684,2.733528614,2.619051933,3.323566914,3.04735899,2.807283401,4.874706268,3.063464165]
y2=[16.79506302,16.99078083,17.45476723,17.07185507,16.88507795,16.93854332,17.06287861,16.83707237,17.01340675,19.03709173]
y3=[259.7948909,260.1578116,257.1197152,257.1013093,254.4224977,256.7204714,260.0495219,253.0585647,254.1716933,269.0927982]

l1=plt.plot(x,y1,'r--',label='creation time')
l2=plt.plot(x,y2,'g--',label='look-up time')
l3=plt.plot(x,y3,'b--',label='error-correction time')
plt.plot(x,y1,'ro-',x,y2,'go-',x,y3,'bo-')

plt.title('Ridge Regression Performance Chart (Random Data, size:100k)')
plt.xlabel(r'$\lambda$')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
y1=[5.658769608,5.804991722,5.745661259,5.697286129,5.747759342,5.50249815,5.77378273,6.042933464,7.640779018,6.641316414]
y2=[51.93390846,51.16797686,51.39805079,51.53459311,51.19073391,51.43014193,51.31684542,51.50392056,51.96726322,55.12075424]
y3=[822.4347472,822.821331,817.1081901,814.3633485,811.3559842,816.0421014,821.490705,817.4332738,816.5633559,902.3567796]

l1=plt.plot(x,y1,'r--',label='creation time')
l2=plt.plot(x,y2,'g--',label='look-up time')
l3=plt.plot(x,y3,'b--',label='error-correction time')
plt.plot(x,y1,'ro-',x,y2,'go-',x,y3,'bo-')

plt.title('Ridge Regression Performance Chart (Random Data, size:300k)')
plt.xlabel(r'$\lambda$')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

"""#### KNN"""

bottom_list = ['2','3','4','5','6','7','8','9']
res_list1 = [140.9111381,142.2144055,142.3327327,141.8791175,142.0024753,141.6543126,143.2541966,144.0311074]
res_list2 = [88.41532469,92.53172874,88.55998516,89.45242167,90.53180218,90.31472206,92.33349562,94.41478252]
res_list3 = [5.661082268,5.797028542,5.713808537,5.647468567,6.077623367,5.41331768,5.698204041,5.773818493]
x =list(range(len(res_list1)))
total_width, n = 0.6, 3
width = total_width / n
 
plt.bar(x, res_list1, width=width, label='creation time',fc = 'y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list2, width=width, label='look-up time',tick_label = bottom_list,fc = 'r')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list3, width=width, label='error-correction time',tick_label = bottom_list,fc = 'g')

plt.title('KNN Performance Chart (Random Data, size:10k)')
plt.xlabel('k')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

bottom_list = ['2','3','4','5','6','7','8','9']
res_list1 = [1254.00579,1251.032841,1245.021725,1247.607195,1245.176423,1242.736542,1246.601081,1277.796602]
res_list2 = [255.4584384,257.7407241,260.3504419,260.7653022,259.773767,265.558672,259.5686555,290.0779843]
res_list3 = [16.4003253,15.76877832,16.15029573,16.2925005,16.63279533,16.31966829,16.02983475,17.90752411]
x =list(range(len(res_list1)))
total_width, n = 0.6, 3
width = total_width / n
 
plt.bar(x, res_list1, width=width, label='creation time',fc = 'y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list2, width=width, label='look-up time',tick_label = bottom_list,fc = 'r')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list3, width=width, label='error-correction time',tick_label = bottom_list,fc = 'g')

plt.title('KNN Performance Chart (Random Data, size:30k)')
plt.xlabel('k')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

bottom_list = ['2','3','4','5','6','7','8','9']
res_list1 = [3464.390373,3452.37416,3456.116974,3451.282275,3464.449716,3463.014555,3485.318196,3524.862123]
res_list2 = [427.6049495,425.7497787,431.0659409,427.768445,433.9232206,436.9111776,438.4119272,469.8619008]
res_list3 = [29.12983894,29.50768471,29.8666358,28.91653776,29.083848,29.34070826,28.78162861,29.01159525]
x =list(range(len(res_list1)))
total_width, n = 0.6, 3
width = total_width / n
 
plt.bar(x, res_list1, width=width, label='creation time',fc = 'y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list2, width=width, label='look-up time',tick_label = bottom_list,fc = 'r')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list3, width=width, label='error-correction time',tick_label = bottom_list,fc = 'g')

plt.title('KNN Performance Chart (Random Data, size:50k)')
plt.xlabel('k')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

bottom_list = ['2','3','4','5','6','7','8','9']
res_list1 = [9068.733692,9051.073074,9107.954741,9123.385429,9095.725298,9116.693974,9040.564299,9140.614986]
res_list2 = [831.0105801,854.6931744,888.6079788,883.9108944,857.663393,869.5421219,864.1581535,746.179986]
res_list3 = [46.23842239,46.77462578,50.61912537,48.60305786,47.23930359,46.45347595,48.37369919,47.64245749]
x =list(range(len(res_list1)))
total_width, n = 0.6, 3
width = total_width / n
 
plt.bar(x, res_list1, width=width, label='creation time',fc = 'y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list2, width=width, label='look-up time',tick_label = bottom_list,fc = 'r')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list3, width=width, label='error-correction time',tick_label = bottom_list,fc = 'g')

plt.title('KNN Performance Chart (Random Data, size:80k)')
plt.xlabel('k')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

bottom_list = ['2','3','4','5','6','7','8','9']
res_list1 = [13862.53834,13831.82526,13820.58239,13844.05208,13829.32448,13851.41778,13838.29451,14399.6538]
res_list2 = [843.2831764,852.7805805,859.8001003,863.961935,910.6228352,872.1628189,900.7015228,942.2077298]
res_list3 = [55.46498299,55.89199066,57.92784691,56.19549751,58.03275108,56.13994598,57.0037365,58.41122866]
x =list(range(len(res_list1)))
total_width, n = 0.6, 3
width = total_width / n
 
plt.bar(x, res_list1, width=width, label='creation time',fc = 'y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list2, width=width, label='look-up time',tick_label = bottom_list,fc = 'r')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list3, width=width, label='error-correction time',tick_label = bottom_list,fc = 'g')

plt.title('KNN Performance Chart (Random Data, size:100k)')
plt.xlabel('k')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

bottom_list = ['2','3','4','5','6','7','8','9']
res_list1 = [128127.4266,126162.4694,126076.5252,126336.7033,126117.6093,125410.4331,126526.8607,129092.1208]
res_list2 = [2662.190676,2695.25075,2590.280294,2670.11857,2617.266417,2687.391996,2585.324526,2812.780309]
res_list3 = [181.8425655,170.4719067,167.8996086,169.1451073,169.7444916,184.6683025,166.1677361,172.8920341]
x =list(range(len(res_list1)))
total_width, n = 0.6, 3
width = total_width / n
 
plt.bar(x, res_list1, width=width, label='creation time',fc = 'y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list2, width=width, label='look-up time',tick_label = bottom_list,fc = 'r')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, res_list3, width=width, label='error-correction time',tick_label = bottom_list,fc = 'g')

plt.title('KNN Performance Chart (Random Data, size:300k)')
plt.xlabel('k')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

"""#### Decision Tree"""

x=[3,6,9,12]
y1=[14.10480738,25.65586567,36.60339117,47.22682238]
y2=[1.874744892,1.796710491,1.83891058,1.794719696]
y3=[6.54528141,6.480407715,6.438243389,6.933522224]

l1=plt.plot(x,y1,'r--',label='creation time')
l2=plt.plot(x,y2,'y--',label='look-up time')
l3=plt.plot(x,y3,'b--',label='error-correction time')
plt.plot(x,y1,'ro-',x,y2,'yo-',x,y3,'bo-')

plt.title('Decision Tree Performance Chart (Random Data, size:10k)')
plt.xlabel('max depth of tree')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

x=[3,6,9,12]
y1=[79.4549346,155.5278897,229.7729611,304.7050476]
y2=[7.69238472,7.699680328,7.943296432,7.90951252]
y3=[18.66588593,19.23947334,18.64836216,18.78824234]

l1=plt.plot(x,y1,'r--',label='creation time')
l2=plt.plot(x,y2,'y--',label='look-up time')
l3=plt.plot(x,y3,'b--',label='error-correction time')
plt.plot(x,y1,'ro-',x,y2,'yo-',x,y3,'bo-')

plt.title('Decision Tree Performance Chart (Random Data, size:30k)')
plt.xlabel('max depth of tree')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

x=[3,6,9,12]
y1=[201.603961,393.5953736,583.3191514,771.2876678]
y2=[21.93481922,19.10841465,19.14710999,19.12784576]
y3=[29.92823124,30.90641499,29.71013784,29.97298241]

l1=plt.plot(x,y1,'r--',label='creation time')
l2=plt.plot(x,y2,'g--',label='look-up time')
l3=plt.plot(x,y3,'b--',label='error-correction time')
plt.plot(x,y1,'ro-',x,y2,'yo-',x,y3,'bo-')

plt.title('Decision Tree Performance Chart (Random Data, size:50k)')
plt.xlabel('max depth of tree')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

x=[3,6,9,12]
y1=[475.9470463,935.326457,1395.614469,1843.26998]
y2=[53.17834616,46.90583944,47.84359932,47.43001461]
y3=[45.43440342,45.1115489,46.15888596,45.95572948]

l1=plt.plot(x,y1,'r--',label='creation time')
l2=plt.plot(x,y2,'y--',label='look-up time')
l3=plt.plot(x,y3,'b--',label='error-correction time')
plt.plot(x,y1,'ro-',x,y2,'yo-',x,y3,'bo-')

plt.title('Decision Tree Performance Chart (Random Data, size:80k)')
plt.xlabel('max depth of tree')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

x=[3,6,9,12]
y1=[709.3069077,1405.193007,2102.088344,2797.462177]
y2=[75.28427839,70.1307416,71.78395987,72.83446789]
y3=[57.50689507,58.65219831,58.1957221,58.38272572]

l1=plt.plot(x,y1,'r--',label='creation time')
l2=plt.plot(x,y2,'y--',label='look-up time')
l3=plt.plot(x,y3,'b--',label='error-correction time')
plt.plot(x,y1,'ro-',x,y2,'yo-',x,y3,'bo-')

plt.title('Decision Tree Performance Chart (Random Data, size:100k)')
plt.xlabel('max depth of tree')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

x=[3,6,9,12]
y1=[6390.760684,12724.82492,19104.79895,25371.57011]
y2=[702.9869437,648.9350915,652.7395129,649.6348381]
y3=[172.0401168,171.6834307,181.5740347,178.0450344]

l1=plt.plot(x,y1,'r--',label='creation time')
l2=plt.plot(x,y2,'y--',label='look-up time')
l3=plt.plot(x,y3,'b--',label='error-correction time')
plt.plot(x,y1,'ro-',x,y2,'yo-',x,y3,'bo-')

plt.title('Decision Tree Performance Chart (Random Data, size:300k)')
plt.xlabel('max depth of tree')
plt.ylabel('timing (ms)')

plt.legend()
plt.show()

"""#### Summary"""

x=[10,30,50,80,100,300]
y1=[122.284615,388.4037018,701.6992331,1190.695632,1486.651111,5125.088954]
y2=[17.90105104,59.12134647,129.2155266,193.7104106,242.5570369,873.8640904]
y3=[16.77427292,97.47984409,157.7148318,241.5912628,273.9266276,868.2944775]
y4=[236.9790077,1524.664998,3907.967257,10055.89938,14764.20951,129175.967]
y5=[25.83992481,118.9437628,269.5587277,625.928843,1680.050766,47178.69135]
y6=[22.52483368,105.8132052,253.4670115,574.5597959,842.0980811,7265.787745]
y7=[10601.48501,33152.08387,56464.77151,73886.62052,95166.23354,483058.9347]

l1=plt.plot(x,y1,'r--',label='B-Tree')
l2=plt.plot(x,y2,'y--',label='Linear Regression')
l3=plt.plot(x,y3,'b--',label='Ridge Regression')
l6=plt.plot(x,y6,'m--',label='Decision Tree')
plt.plot(x,y1,'ro-',x,y2,'yo-',x,y3,'bo-',x,y6,'mo-')

plt.title('Performance Chart for Each Model (Random Data) [1]')
plt.xlabel('size of dataset (*1000)')
plt.ylabel('total timing (ms)')

plt.legend()
plt.show()

l4=plt.plot(x,y4,'g--',label='KNN')
l5=plt.plot(x,y5,'c--',label='Naive Bayes')
l7=plt.plot(x,y7,'k--',label='Deep Learning')

plt.plot(x,y4,'go-',x,y5,'co-',x,y7,'ko-')
plt.title('Performance Chart for Each Model (Random Data) [2]')
plt.xlabel('size of dataset (*1000)')
plt.ylabel('total timing (ms)')

plt.legend()
plt.show()
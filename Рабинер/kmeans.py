from sklearn.cluster import KMeans
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd
from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import LeaveOneOut
from sklearn import svm, datasets
from sklearn.model_selection import StratifiedKFold
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt


N=1000
def printer(list):
     for i in range(0,N,4):
          print(list[i*4:(i+1)*4])

     print("_______")

colnames=list(map(lambda x: 'a%i'%x , range(2,N+1)))

dataset = pd.read_csv('data (1).csv')
data = dataset[colnames].values.tolist()
target = [0,1,2,3]*(100*4) #dataset['matrix'].values.tolist()
#print(len(data), target)


model = SpectralClustering(n_clusters=4, affinity='nearest_neighbors',
                           assign_labels='kmeans')
labels = model.fit_predict(data,target)

cf_matrix = confusion_matrix(target, labels)
print(cf_matrix)
m = cf_matrix / cf_matrix.astype(np.float).sum(axis=1)
#printer(labels)ах
print(m)

df_cm = pd.DataFrame(m, index = ['tv', 'tn', 'bl', 'bp'],
                  columns = ['tv', 'tn', 'bl', 'bp'])
plt.figure(figsize = (10,7))
sn.heatmap(df_cm, annot=True)

plt.show()





#kmeans = KMeans(n_clusters=4)
#kmeans.fit(data)
#y_kmeans = kmeans.predict(data)
#centers = kmeans.cluster_centers_
##print(y_kmeans)
#printer(y_kmeans)

#cf_matrix = confusion_matrix(target, y_kmeans)
#print(cf_matrix)
#m = cf_matrix / cf_matrix.astype(np.float).sum(axis=1)
##printer(labels)ах
#print(m)
#
#df_cm = pd.DataFrame(m, index = ['tv', 'tn', 'bl', 'bp'],
#                  columns = ['tv', 'tn', 'bl', 'bp'])
#plt.figure(figsize = (10,7))
#sn.heatmap(df_cm, annot=True)
#
#plt.show()






#labels = KMeans(4, random_state=0).fit_predict(data)
#
#cf_matrix = confusion_matrix(target, labels)
#print(cf_matrix)
#m = cf_matrix / cf_matrix.astype(np.float).sum(axis=1)
##printer(labels)ах
#print(m)
#
#df_cm = pd.DataFrame(m, index = ['tv', 'tn', 'bl', 'bp'],
#                  columns = ['tv', 'tn', 'bl', 'bp'])
#plt.figure(figsize = (10,7))
#sn.heatmap(df_cm, annot=True)
#
#plt.show()

##print(labels)
#printer(labels)


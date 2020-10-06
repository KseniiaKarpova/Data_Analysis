from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn.cluster import SpectralClustering

N=1000
def printer(list):
     for i in range(0,N,4):
          print(list[i*4:(i+1)*4])

     print("_______")

colnames=list(map(lambda x: 'a%i'%x , range(2,N+1)))

dataset = pd.read_csv('data1000.csv')
data = dataset[colnames].values.tolist()


print(len(data))
model = SpectralClustering(n_clusters=4, affinity='nearest_neighbors',
                           assign_labels='kmeans')
labels = model.fit_predict(data)

#print(labels)
printer(labels)

kmeans = KMeans(n_clusters=4)
kmeans.fit(data)
y_kmeans = kmeans.predict(data)
centers = kmeans.cluster_centers_
#print(y_kmeans)
printer(y_kmeans)
labels = KMeans(4, random_state=0).fit_predict(data)
#print(labels)
printer(labels)
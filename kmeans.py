# kmeans.py
körpergrößen = [123, 107, 178, 100, 99,
                156, 178, 172, 112, 145, 133, 171, 118] #1
c1 = körpergrößen[0] #2
c2 = körpergrößen[1]
cluster1 = [] #3
fertig = False #4
while not fertig: #5
    altesCluster1 = cluster1 #6
    cluster1 = [] #7
    cluster2 = []
    for k in körpergrößen: #8
        if (k-c1)**2 < (k-c2)**2: #9
            cluster1 += [k]
        else:
            cluster2 += [k]
    c1 = sum(cluster1)/len(cluster1) #10
    c2 = sum(cluster2)/len(cluster2) #11
    print('Cluster 1:', cluster1) #12
    print('Cluster 2:', cluster2)
    fertig = cluster1 == altesCluster1 #13
print('Größe 1:', round(c1),'cm,',
'Größe 2:', round(c2),'cm') #14

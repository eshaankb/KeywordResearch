import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import spacy 

def cluster_data(data):
    nlp = spacy.load("en_core_web_lg")
    print(data.values)
    X = np.zeros((len(data), 300))
    #kmeans = KMeans(n_clusters=4, random_state=42)
    #kmeans.fit(X)
    for i, keyword in enumerate(data.values):
        X[i] = nlp(keyword).vector
    print(X)
    kmeans = KMeans(n_clusters=10, random_state=42)
    kmeans.fit(X)
    # Retrieve the cluster labels and centroids.
    labels = kmeans.labels_
    output = pd.DataFrame({
        'Keyword': data.values,
        'Cluster': labels
    })
    output.to_csv("output.csv")
from sklearn.metrics import silhouette_score

score = silhouette_score(X_pca, labels)
print(score)

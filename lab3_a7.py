from sklearn.neighbors import KNeighborsClassifier
def train_knn_classifier(X_train, y_train, k):
    # The function trains a kNN classifier using the training dataset forn a6
    knn_model = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(X_train, y_train)
    return knn_model
# main program

# training kNN classifier with k = 3
knn_model = train_knn_classifier(X_train, y_train, k=3)

print(" kNN classifier trained successfully with k = 3")

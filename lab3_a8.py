def calculate_knn_accuracy(knn_model, X_test, y_test):
    # the function calculates the accuracy of the  kNN classifier(trained)
    accuracy_value = knn_model.score(X_test, y_test)
    return accuracy_value
# mainprogram

# calculating the accuracy of the kNN classifier on test data
knn_accuracy = calculate_knn_accuracy(knn_model, X_test, y_test)

print("A8: Accuracy of kNN classifier (k = 3):", knn_accuracy)

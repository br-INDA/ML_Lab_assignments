def get_knn_predictions(knn_model, X_test):
    # The function predicts the class labels for the test feature vectors
    predicted_labels = knn_model.predict(X_test)
    return predicted_labels
#  main program

# Predicting the class labels for the test data
y_predicted_test = get_knn_predictions(knn_model, X_test)

print("A9: Predicted class labels for test dataset:")
print(y_predicted_test)

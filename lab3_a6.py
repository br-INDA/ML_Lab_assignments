def split_train_test(X_features, y_labels, test_size):
    # The function splits the dataset into training set and testing set
    X_train, X_test, y_train, y_test = train_test_split(
        X_features,
        y_labels,
        test_size=test_size,
        random_state=42
    )
    return X_train, X_test, y_train, y_test
#  main program

# Splitting the dataset into training set and testing set
X_train, X_test, y_train, y_test = split_train_test(
    X_features,
    y_labels,
    test_size=0.3
)

print(" Dataset split completed")
print(" Number of training samples:", len(X_train))
print(" Number of testing samples:", len(X_test))

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_model():
    # Load dataset
    data = pd.read_csv('spam_ham_dataset.csv')  # Replace with your dataset path

    # Split data
    X = data['text']
    y = data['label_num']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a pipeline
    model = make_pipeline(CountVectorizer(), MultinomialNB())

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model accuracy: {accuracy * 100:.2f}%')

    # Save the model
    with open('spam_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    print('Model training complete and model saved as spam_model.pkl')


if __name__ == "__main__":
    train_model()
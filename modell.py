import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load training data
data = pd.read_csv("training_data.csv")  # Placeholder for actual training data
X = data.drop("vulnerability", axis=1)
y = data["vulnerability"]

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "model.joblib")

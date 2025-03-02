import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Simulated Stock Data (Replace with real stock data if available)
data = pd.DataFrame({
    'Open': np.random.rand(100) * 100,
    'High': np.random.rand(100) * 100,
    'Low': np.random.rand(100) * 100,
    'Close': np.random.rand(100) * 100
})

# Features and Label
X = data[['Open', 'High', 'Low']]
y = data['Close']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the Model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved successfully!")

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pickle

data = pd.read_csv("agricultural_data.csv")
features = ["N (kg/ha)", "P (kg/ha)", "K (kg/ha)"]
target = "Crop Yield (tons/ha)"

X = data[features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = SVR(kernel='rbf', C=100, gamma=0.1)

model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)


from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse:.2f}")

with open('multitask_svr_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved")


plt.scatter(X_test["N (kg/ha)"], y_test, color='blue', label='Actual Yield')
plt.scatter(X_test["N (kg/ha)"], y_pred, color='red', label='Predicted Yield')
plt.xlabel('Nitrogen (kg/ha)')
plt.ylabel('Crop Yield (tons/ha)')
plt.title('Nitrogen vs. Crop Yield')
plt.legend()
plt.grid(True)
plt.show()



import numpy as np
from sklearn.ensemble import IsolationForest
import pickle, os

data = np.random.randint(10, 90, size=(600, 5))  # CPU, Mem, Disk, Temp, Net

model = IsolationForest(n_estimators=200, contamination=0.10)
model.fit(data)

os.makedirs("models", exist_ok=True)

with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")

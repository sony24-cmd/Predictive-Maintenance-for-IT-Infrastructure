import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle

# Step 1: Generate Synthetic Data
def generate_synthetic_data(num_samples=1000):
    np.random.seed(42)
    cpu_usage = np.random.uniform(20, 80, num_samples)
    memory_usage = np.random.uniform(30, 90, num_samples)
    disk_usage = np.random.uniform(10, 70, num_samples)
    network_usage = np.random.uniform(15, 85, num_samples)
    
    # Capacity requirement is a function of the above metrics
    capacity_requirement = 0.5 * cpu_usage + 0.3 * memory_usage + 0.1 * disk_usage + 0.1 * network_usage + np.random.normal(0, 5, num_samples)
    
    data = pd.DataFrame({
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'disk_usage': disk_usage,
        'network_usage': network_usage,
        'capacity_requirement': capacity_requirement
    })
    
    return data

# Step 2: Train the Model
data = generate_synthetic_data()
X = data[['cpu_usage', 'memory_usage', 'disk_usage', 'network_usage']]
y = data['capacity_requirement']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Step 3: Save the Model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as 'model.pkl'.")
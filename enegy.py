import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Generate a synthetic dataset (replace this with real-world data)
data = {
    'Appliance': ['Refrigerator', 'Air Conditioner', 'Television'],
    'PowerRating': [100, 1500, 50],  # Watts
    'EnergyConsumption': [300, 2000, 100],  # Daily energy consumption in Watt-hours
}
df = pd.DataFrame(data)

class EnergyEfficiencyAdvisor:
    def _init_(self):
        self.model = LinearRegression()
        self.appliances = []

    def add_appliance(self, appliance):
        self.appliances.append(appliance)

    def train_model(self):
        X = df['PowerRating'].values.reshape(-1, 1)
        y = df['EnergyConsumption'].values
        self.model.fit(X, y)

    def predict_energy_consumption(self, power_rating):
        return self.model.predict(np.array([[power_rating]]))[0]

if _name_ == "_main_":
    advisor = EnergyEfficiencyAdvisor()

    # Train the model with the synthetic dataset
    advisor.train_model()

    while True:
        appliance_name = input("Enter the name of the appliance (or 'exit' to quit): ")
        if appliance_name.lower() == 'exit':
            break

        while True:
            try:
                power_rating = float(input(f"Enter the power rating of {appliance_name} in Watts: "))
                if power_rating >= 0:
                    break
                else:
                    print("Power rating should be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        predicted_consumption = advisor.predict_energy_consumption(power_rating)
        print(f"Estimated daily energy consumption for {appliance_name}: {predicted_consumption:.2f} Watt-hours.")
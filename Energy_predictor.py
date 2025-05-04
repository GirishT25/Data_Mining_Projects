import pandas as pd
import mysql.connector
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Step 1: Load the dataset
df = pd.read_csv('Energy_consumption.csv')

# Step 2: Clean and format columns
df.columns = df.columns.str.strip()
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Step 3: Convert categorical columns to numerical
df['HVACUsage'] = df['HVACUsage'].map({'On': 1, 'Off': 0})
df['LightingUsage'] = df['LightingUsage'].map({'On': 1, 'Off': 0})
df['Holiday'] = df['Holiday'].map({'Yes': 1, 'No': 0})
df = pd.get_dummies(df, columns=['DayOfWeek'], drop_first=True)

# Step 4: Feature engineering - extract time components
df['hour'] = df['Timestamp'].dt.hour
df['day'] = df['Timestamp'].dt.day
df['month'] = df['Timestamp'].dt.month

# Step 5: Prepare features and labels
feature_cols = ['Temperature', 'Humidity', 'SquareFootage', 'Occupancy',
                'HVACUsage', 'LightingUsage', 'RenewableEnergy', 'Holiday',
                'hour', 'day', 'month'] + [col for col in df.columns if col.startswith('DayOfWeek_')]

X = df[feature_cols]
y = df['EnergyConsumption']

# Step 6: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Step 7: Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 8: Predict and evaluate
df['predicted_energy'] = model.predict(X)
mae = mean_absolute_error(y_test, model.predict(X_test))
print("Mean Absolute Error:", mae)

# Step 9: Store predictions in MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Girish@25',
    database='energy_db'
)
cursor = conn.cursor()
cursor.execute("DELETE FROM energy_predictions")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO energy_predictions (timestamp, zone, predicted_energy)
        VALUES (%s, %s, %s)
    """, (row['Timestamp'].to_pydatetime(), 'ZoneA', row['predicted_energy']))

conn.commit()
cursor.close()
conn.close()

print("Predictions inserted into MySQL database successfully.")

# =============================
# OLAP Operations (Simulation)
# =============================

print("\n--- OLAP Operations ---")

# Roll-up: Group by month and get average predicted energy
monthly_rollup = df.groupby('month')['predicted_energy'].mean()
print("\nRoll-up (Monthly average predicted energy):\n", monthly_rollup)

# Drill-down: Group by day within a specific month (e.g., month = 1)
drilldown = df[df['month'] == 1].groupby('day')['predicted_energy'].mean()
print("\nDrill-down (Daily average for January):\n", drilldown)

# Slice: Filter records for a specific hour (e.g., 9 AM)
slice_result = df[df['hour'] == 9]
print("\nSlice (Records for 9 AM):\n", slice_result[['Timestamp', 'predicted_energy']])

# Dice: Filter where month = 1 and hour between 8 and 10
dice_result = df[(df['month'] == 1) & (df['hour'].between(8, 10))]
print("\nDice (January records between 8-10 AM):\n", dice_result[['Timestamp', 'predicted_energy']])

# Pivot (cross-tab): Pivot table of average predicted energy by hour and day
pivot_table = pd.pivot_table(df, values='predicted_energy', index='hour', columns='day', aggfunc='mean')
print("\nPivot Table (Hour vs Day - avg predicted energy):\n", pivot_table)

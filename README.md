## Requirements

- Python 3.8 or higher
- MySQL database
- Required Python libraries (see below)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/energy-dashboard.git
   cd energy-dashboard
2 .pip install -r requirements.txt

3. Set up the MySQL database:

Create a database named energy_db.
Import the required schema for energy_predictions and predictions_results tables.
4. Update the database connection string in dashboard.py

Usage

Run the Streamlit app:
    streamlit run dashboard.py
Open the app in your browser at http://localhost:8501.

Use the dashboard to:

Select a zone and view historical energy consumption data.
Input parameters to predict energy consumption.
View and store predictions in the database.
File Descriptions
dashboard.py: Main application file for the Streamlit dashboard.
Energy_consumption.csv: Dataset containing historical energy consumption data.
Energy_predictor.py: (Optional) Script for additional prediction logic.
Example Input for Prediction
Temperature: 25°C
Humidity: 50%
Square Footage: 1000 sq. ft.
Occupancy: 10 people
HVAC Usage: On/Off
Lighting Usage: On/Off
Renewable Energy Generated: 5 kWh
Holiday: Yes/No
Hour of Day: 12
Day: 15
Month: 6
Day of Week: Monday
Technologies Used
Streamlit: For building the interactive dashboard.
Pandas: For data manipulation.
SQLAlchemy: For database integration.
Scikit-learn: For machine learning model training and prediction.
MySQL: For storing and retrieving data.
Dataset
The dataset Energy_consumption.csv contains the following columns:

Timestamp: Date and time of the record.
Temperature: Temperature in °C.
Humidity: Humidity percentage.
SquareFootage: Area in square feet.
Occupancy: Number of occupants.
HVACUsage: Whether HVAC is On/Off.
LightingUsage: Whether lighting is On/Off.
RenewableEnergy: Renewable energy generated in kWh.
DayOfWeek: Day of the week.
Holiday: Whether it is a holiday.
EnergyConsumption: Energy consumption in kWh.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or feedback, please contact [thoratgirish286@gmail.com].


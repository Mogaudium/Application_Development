This project is an Air Quality Index (AQI) visualization web application that allows users to select a location and a date range to display AQI data over time. The application fetches AQI data from an API, visualizes it using a line chart, and offers functionality to convert the AQI data into SQL insert statements.

Files in the Project
1. index.html
Description: This is the main HTML file that provides the user interface for the application.
Key Features:
Users can select a location and date range to filter AQI data.
Includes a form for input and a canvas element for chart visualization.
Linked to the external styles (styles.css) and script (app.js) for functionality.
Contains a reference to Chart.js for rendering the charts.
2. app.js
Description: The main JavaScript file responsible for handling user interactions, fetching data, and rendering charts.
Key Features:
Handles form submissions, sends requests to the API (api.php) based on user input, and updates the chart with AQI data.
Uses Chart.js to visualize AQI data in a line chart.
Implements logic to fetch locations from the server using the locations.php file and populate a dropdown for user selection.
Core Functions:
createChart(ctx, labels, aqiValues): Initializes the AQI line chart.
fetchLocations(): Fetches available locations from the server and populates the location select element.
3. ny.py
Description: A Python script that retrieves AQI data from the OpenAQ API, processes it, and saves it as a CSV file.
Key Features:
Fetches AQI data for a specified city and date range using the OpenAQ API.
Saves the retrieved AQI data into a CSV file (ny_aqi_data.csv).
Can be customized to retrieve data for different cities.
Core Functions:
get_aqi_data(city, start_date, end_date): Fetches AQI data from the OpenAQ API.
save_aqi_data_to_csv(aqi_data_list, output_file): Saves the fetched AQI data to a CSV file.
4. convert.py
Description: A Python script that reads AQI data from a CSV file and converts it into SQL INSERT statements.
Key Features:
Reads AQI data from the CSV file generated by ny.py.
Converts each row of AQI data into SQL INSERT statements for database insertion.
Saves the SQL statements to a file (aqi_data.sql).
Core Functions:
convert_to_sql_insert_statements(df, table_name): Converts the CSV data into SQL insert statements.
save_sql_statements_to_file(sql_statements, output_file): Saves the generated SQL statements into a file.
5. aqi_data.csv
Description: A CSV file generated by the ny.py script containing AQI data fetched from the API.
Contents:
Columns: date, location, aqi, parameter.
Contains AQI data for a specific city and date range.
6. aqi_data.sql
Description: SQL file generated by the convert.py script containing INSERT statements for AQI data.
Contents:
SQL insert statements for adding AQI data into a database.
7. config.php, Database.php, api.php, locations.php
Descriptions:
These PHP files handle server-side functionality for retrieving and serving AQI data, managing database interactions, and providing available locations for the application.
config.php: Contains database configuration.
Database.php: Manages database connections and queries.
api.php: Serves AQI data from the database in response to user input.
locations.php: Provides available locations for the user to select in the frontend.

How to Run the Application
Frontend:

Open the index.html file in a browser.
Select a location and date range using the form.
Click "Filter" to display AQI data on a line chart.
Backend:

Ensure the backend PHP files (api.php, locations.php, config.php, Database.php) are correctly configured with a database to fetch and serve data.
Use the ny.py script to fetch new AQI data from the OpenAQ API and save it into a CSV file.
Run the convert.py script to convert the CSV data into SQL insert statements for database storage.

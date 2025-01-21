# 24-Hour Restaurant Finder

An interactive web application that helps users locate 24-hour restaurants in their area, visualize their locations on an interactive map, and filter restaurants by name, cuisine, and rating. Built using **Django**, **PostGIS**, **Leaflet.js**, and **HTML/CSS**.

---

## Features

- **Interactive Map**: Displays restaurant locations with dynamic markers using Leaflet.js.
- **Search Functionality**: Filter restaurants by:
  - Name
  - Cuisine type
  - Minimum rating
- **Restaurant Details**: View details such as address, cuisine type, and rating in both a list and map popup.
- **Geospatial Queries**: Powered by PostGIS to handle proximity searches and geolocation filtering.

---

## Tech Stack

### Backend
- **Django**: Web framework for backend logic.
- **PostgreSQL + PostGIS**: Database with geospatial support for storing and querying location data.

### Frontend
- **Leaflet.js**: Interactive mapping library for rendering markers and popups.
- **HTML/CSS/JavaScript**: For search forms and UI elements.

### Deployment
- Hosted on **[deployment platform name]** (e.g., PythonAnywhere, Render, or Heroku).

---

## Installation and Setup

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/24-hour-restaurant-finder.git
cd 24-hour-restaurant-finder
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
- Ensure **PostgreSQL** is installed and running.
- Create a database for the project:
  ```sql
  CREATE DATABASE restaurant_finder;
  CREATE EXTENSION postgis;
  ```
- Update `DATABASES` in `settings.py` with your PostgreSQL credentials.

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Add Sample Data
Use the Django admin panel or run a custom script to populate the database with restaurant data.

### 7. Run the Development Server
```bash
python manage.py runserver
```
Access the application at `http://127.0.0.1:8000/`.

---

## How It Works

### Interactive Map
- All restaurants are displayed as markers on the map.
- Clicking a marker shows details about the restaurant.

### Search Functionality
- Enter a name, cuisine type, or rating to filter restaurants.
- The map updates dynamically to display matching results.

---

## Future Enhancements
- Implement user geolocation for proximity searches.
- Add restaurant opening hours and 24-hour filters.
- Enable user authentication for saving favorite restaurants.

---

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests for review.



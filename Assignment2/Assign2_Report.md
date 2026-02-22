# CE3420 - GIS Assignment 2 Report

**Name:** Kaushal Singh
**Roll Number:** CH22BTECH11018

---

## Overview

This assignment covers Python fundamentals for GIS applications, including distance calculations using various methods, working with web APIs, and data manipulation with CSV files and Pandas.

---

## Tasks Completed

### 1. The Python Standard Library

**Objective:** Calculate the distance between two cities using the Haversine formula.

- **Cities:** Hyderabad (17.4065, 78.4772) and Bengaluru (12.9629, 77.5775)
- **Method:** Implemented the Haversine formula using Python's `math` module
- **Result:** Distance = **503.44 km**

---

### 2. Third-party Modules

**Objective:** Repeat distance calculation using the `geopy` library.

- **Library Used:** `geopy`
- **Results:**
  | Method | Distance |
  |--------|----------|
  | Great Circle | 503.45 km |
  | Geodesic (WGS-84 ellipsoid) | 501.10 km |

---

### 3. Using Web APIs

**Objective:** Use OpenRouteService API to calculate driving distances.

#### Question 1: Hyderabad to Bengaluru
- **Driving Distance:** 569.05 km
- **Estimated Duration:** 27,527.6 seconds (~7.6 hours)

#### Question 2: San Francisco to Multiple Cities
| Destination | Driving Distance |
|-------------|------------------|
| Los Angeles | 615.56 km |
| Boston | 4,991.47 km |
| Atlanta | 3,976.33 km |

---

### 4. Reading Files

**Objective:** Count the number of lines in the `worldcities.csv` file.

- **File:** `python_foundation/data/worldcities.csv`
- **Result:** Total lines = **15,494**

---

### 5. Reading CSV Files

**Objective:** Calculate geodesic distances from home city to all cities in the same country and export to CSV.

- **Home City:** Hyderabad, India
- **Method:** Used `csv` module with `geopy.distance.geodesic()`
- **Output File:** `Assignment2/cities_distance.csv`

---

### 6. Working with Pandas

**Objective:** Use Pandas to filter and calculate distances, excluding the home city from results.

- **Home City:** Bengaluru, India
- **Method:** Used `pandas.DataFrame.apply()` with custom distance function
- **Result:** Calculated distances to **211 Indian cities**

Sample output:
| City | Distance (km) |
|------|---------------|
| Mumbai | 837.19 |
| Delhi | 1,738.64 |
| Kolkata | 1,552.64 |
| Chennai | 295.34 |
| Hyderabad | 500.05 |

---

## Libraries Used

- `math` - Standard library for mathematical operations
- `os` - File path operations
- `csv` - CSV file handling
- `geopy` - Geocoding and distance calculations
- `requests` - HTTP requests for API calls
- `pandas` - Data manipulation and analysis

---

## Key Learnings

1. **Haversine Formula** - Calculates great-circle distance assuming a spherical Earth
2. **Geodesic Distance** - More accurate calculation using Earth's ellipsoid shape (WGS-84)
3. **API Integration** - Using REST APIs to get real-world driving distances and durations
4. **Data Processing** - Efficient handling of large CSV datasets using both native Python and Pandas

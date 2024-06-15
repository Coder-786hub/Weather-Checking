# Weather App

A simple weather application built using Python's Tkinter, Geopy, TimezoneFinder, and OpenWeatherMap API.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Clone the Repository](#clone-the-repository)
    - [Setup Virtual Environment](#setup-virtual-environment)
    - [Install Dependencies](#install-dependencies)
    - [API Key Configuration](#api-key-configuration)
    - [Run the Application](#run-the-application)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [Dependencies](#dependencies)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

## Features

- Search weather information by city name
- Display current time of the searched city
- Show weather conditions including temperature, wind speed, humidity, description, and pressure

## Installation

### Prerequisites

- Python 3.x
- Virtual environment tool (optional but recommended)

### Clone the Repository

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
Setup Virtual Environment
It is recommended to use a virtual environment to manage dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies
Install the required dependencies using pip:

bash
Copy code
pip install -r requirements.txt
API Key Configuration
Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key in the script (main.py):

python
Copy code
API_KEY = 'YOUR_API_KEY'
Run the Application
Start the application:

bash
Copy code
python main.py
Usage
Enter the city name in the search box.
Click the search icon or press Enter.
The current weather information and local time of the city will be displayed.


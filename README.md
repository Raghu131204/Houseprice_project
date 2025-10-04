# Houseprice Project

A project for predicting house prices using machine learning, wrapped in a web app.

## Table of Contents
- [Overview](#overview)  
- [Features](#features)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Model Training & EDA](#model-training--eda)  
- [Web App](#web-app)  
- [Requirements](#requirements)  
- [Contributing](#contributing)  
- [License](#license)  

## Overview
This repository provides a pipeline for:
1. Exploratory Data Analysis (EDA)  
2. Model training  
3. A web interface to input house features and output predicted prices  

It is built using Python, scikit-learn, and Flask (or similar) for deployment.

## Features
- Interactive EDA via Jupyter notebook  
- Trained model saved as a serialized file (`model.joblib`)  
- Web application with forms to enter house attributes and get price predictions  
- Clean UI using templates and static assets  

## Project Structure
Houseprice_project/
│
├── Dataset/ # Data files (e.g. CSVs)
├── EDA.ipynb # Notebook for exploratory data analysis
├── Modeltraining.ipynb # Notebook for training and selecting model
├── app.py # Flask (or other) app entry point
├── forms.py # Form handling definitions
├── model.joblib # Trained model artifact
├── requirements.txt # Python dependencies
├── templates/ # HTML template files
└── static/ # CSS, JS, images, etc.


## Installation
1. Clone the repository  
   ```bash
   git clone https://github.com/Raghu131204/Houseprice_project.git
   cd Houseprice_project
2. Install dependencies
pip install -r requirements.txt

3. Prepare the dataset
--Place your CSV or dataset files inside the Dataset/ directory (or modify paths accordingly).
--Ensure the same preprocessing pipeline that your notebooks use.

4.Running the Web App
python app.py


# Crime Rate Prediction System

## Overview
This project is a Machine Learning–based Crime Rate Prediction System developed using Python, Linear Regression, and Streamlit. It predicts crime rates based on selected City, Month, and Year through an interactive web interface. The system ensures consistent feature engineering and preprocessing between training and inference to provide accurate predictions.

---

## Features

### Crime Rate Prediction :-
- Predict crime rate using a trained Linear Regression model
- Dropdown-based selection for City, Month, and Year
- Real-time prediction output

### Web Application (Streamlit) :-
- Clean and center-aligned user interface
- Single-row dropdown layout for better usability
- Instant predictions without page reload
- Consistent feature encoding during inference

### Machine Learning Pipeline :-
- Feature engineering to derive Month and Year
- One-hot encoding for categorical city data
- Alignment of prediction input with training feature schema
- Model evaluation using regression metrics

---

## Technology Stack
- Python  
- Scikit-learn  
- Pandas  
- NumPy  
- Streamlit  

---

## Dataset

The dataset used for this project contains historical crime records with city and date information.  
Month and Year features are derived from the date column during preprocessing.

🔗 Dataset Link: https://www.kaggle.com/datasets/sudhanvahg/indian-crimes-dataset

---

## Model Details
- Model: Linear Regression  
- Input Features: City (One-Hot Encoded), Month, Year  
- Output: Predicted Crime Rate  
- Evaluation Metrics:
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - R² Score

---

## Project Structure
Crime-Rate-Prediction/
│
├── app.py
├── model.pkl
├── crime_dataset_india.csv
├── requirements.txt
├── crime_rate_prediction.ipynb
├── README.md


---

## Requirements
- Python 3.10 or higher  
- pip  
- Streamlit  

---

## Installation

### Step 1: Clone the Repository
https://github.com/Kevangi/Crime-Rate-Prediction.git


### Step 2: Navigate to the Project Directory
cd Crime-Rate-Prediction


### Step 3: Install Dependencies
pip install -r requirements.txt


### Step 4: Run the Application
streamlit run app.py


---

## Usage
1. Open the application in your browser at http://localhost:8501  
2. Select City, Month, and Year  
3. Click Predict  
4. View the predicted crime rate  

---

## Future Enhancements
- Crime trend visualization
- Batch prediction using CSV upload
- Streamlit Cloud deployment
- Advanced regression models

---

## Author
Kevangi Patel  
M.E. Information Technology  

---

## License
This project is for academic and learning purposes.

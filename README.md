# Network Security - Phishing Data Analysis

## Overview
This project is a comprehensive Network Security system designed to detect phishing attempts using Machine Learning. It includes an end-to-end pipeline for data ingestion, validation, transformation, model training, and deployment. The system utilizes MongoDB for data storage, MLflow for experiment tracking, and FastAPI for serving predictions.

## Features
- **Data Ingestion**: Automated extraction of data from MongoDB.
- **Data Validation**: Rigorous schema and quality checks to ensure data integrity.
- **Data Transformation**: Preprocessing and feature engineering pipelines.
- **Model Training**: Training classification models (e.g., Random Forest, Logistic Regression) to identify phishing URLs.
- **Experiment Tracking**: Integration with MLflow and DagsHub to track model performance and parameters.
- **Prediction API**: FastAPI-based REST API for real-time predictions.
- **Web Interface**: Simple UI for batch prediction and results visualization.
- **Dockerized**: Ready for containerized deployment.

## Tech Stack
- **Language**: Python 3.x
- **Web Framework**: FastAPI, Uvicorn
- **Database**: MongoDB (Atlas)
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **MLOps**: MLflow, DagsHub
- **Containerization**: Docker
- **CI/CD**: GitHub Actions (configured in `.github/workflows`)

## Project Structure
```
Network-Security/
├── networksecurity/        # Main package source code
│   ├── components/         # Pipeline components (Ingestion, Validation, etc.)
│   ├── pipeline/           # Training and Prediction pipelines
│   ├── entity/             # Configuration and Artifact entities
│   ├── utils/              # Utility functions
│   └── ...
├── Network_Data/           # Data storage
├── final_model/            # Saved models and preprocessors
├── prediction_output/      # Output of batch predictions
├── templates/              # HTML templates for the web app
├── app.py                  # FastAPI application entry point
├── main.py                 # Script to run the training pipeline
├── push_data.py            # Script to seed MongoDB with initial data
├── requirements.txt        # Project dependencies
├── setup.py                # Package setup script
└── Dockerfile              # Docker configuration
```

## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Network-Security
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory and add your MongoDB connection string:
   ```env
   MONGODB_URL_KEY="mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
   ```
   *Note: Ensure you have `python-dotenv` installed and configured.*

## Usage

### 1. Data Seeding (Optional)
If you need to push initial data to MongoDB:
```bash
python push_data.py
```

### 2. Train the Model
To trigger the complete training pipeline (Ingestion -> Validation -> Transformation -> Training):
```bash
python main.py
```
Or use the API endpoint `/train` after starting the server.

### 3. Run the Web Application
Start the FastAPI server:
```bash
python app.py
```
Access the application at: `http://localhost:8000`

### 4. Prediction
- **Web UI**: Navigate to `http://localhost:8000`, upload a CSV file containing network data, and view the results.
- **API**: Send a POST request to `/predict` with your data file.

## MLflow & DagsHub Integration
The project uses MLflow for tracking experiments. Configure your DagsHub credentials in the environment variables to log experiments remotely.

## Author
**Bhanuprasadh**
- Email: bhanuprasadh004@gmail.com

## License
[MIT License](LICENSE)
# spam-ham-prediction

## Live Demo

Experience the Spam-Ham Email Classification in action! Check out the deployed Streamlit app here:

  Streamlit Application: https://spam-ham-prediction-mwwrwnrdbhulxp5wcg3fnk.streamlit.app/

## Docker Deployment

To ensure reproducibility and simplify deployment, the application is containerized with Docker. Pull the image from Docker Hub:

```bash
# Pull Docker image
docker pull seafari/spam-mail-detection
```

## Project Overview

Welcome to the Spam-Ham Email Classification project! This end-to-end system takes raw email text, converts it into TF‑IDF vectors, and classifies messages as spam or ham (non-spam) using a Logistic Regression model. The goal is to provide a lightweight, accurate solution for automatic spam filtering that can be easily integrated into email workflows.

## Key Features & Achievements

  Data Processing & Feature Extraction: Transformed raw email content into TF‑IDF features, capturing important terms while reducing noise.
  High Accuracy: Achieved 97.04% accuracy on the test set, demonstrating strong generalization for real-world spam detection.
  Robust Evaluation: Detailed performance metrics including precision, recall, F1-score, and confusion matrix to understand class-specific behavior.
  User-Friendly Interface: Built a Streamlit web app for interactive classification, allowing users to paste or upload email text and receive immediate predictions.
  Containerized Deployment: Packaged the entire application with Docker for consistent environments across development and production.
  Version Control & Experiment Tracking: Managed code versions and experiment logs with Git and GitHub.

## Performance Metrics

| Metric    | Class 0 (Spam)| Class 1 (Ham) | Overall |
| :-------- | :-----------: | :------------: | :------ |
| Precision |      0.98     |      0.97      | 0.97    |
| Recall    |      0.79     |      1.00      | 0.97    |
| F1-score  |      0.88     |      0.98      | 0.97    |

**Accuracy**

* Training Set: 96.72%

* Test Set: 97.04%

**Confusion Matrix**

|                    | Predicted Spam | Predicted Ham |
|--------------------|----------------|---------------|
| **Actual Spam**    |      118       |      31       |
| **Actual Ham**     |       2        |      964      |

* ROC AUC Score: 89%
  
## ROC Curve

![download (1)](https://github.com/user-attachments/assets/48262940-c8e6-4773-97af-a2d0b16245a3)



## Tech Stack

* Language & Libraries: Python, scikit-learn, Pandas
* Web Framework: Streamlit
* Containerization: Docker
* Version Control: Git & GitHub

## How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/SEAFARI/spam-ham-prediction.git
   cd spam-ham-prediction
   ```
2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

## Docker Usage

1. **Build the Docker image**

   ```bash
   docker build -t seafari/spam-ham-prediction .
   ```
2. **Run the container**

   ```bash
   docker run -p 5000:5000 seafari/spam-ham-prediction
   ```
3. **Access** the app at `http://localhost:5000/`.

## Future Enhancements

  - Advanced NLP Models: Explore more sophisticated models like BERT or transformer-based classifiers for improved accuracy.
  - Real-Time Email Integration: Connect to an email server (e.g., IMAP) to classify incoming mails automatically.
  - Visualization Dashboard: Add more interactive plots in the Streamlit app to monitor spam trends over time.
  - API Endpoint: Expose the classification model via a REST API using Flask or FastAPI.

**If you find this project useful, feel free to  star the repository and share it with others!**

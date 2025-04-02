Crop Yield Prediction

📌 Overview

This project predicts crop yields using a machine learning model. It utilizes Support Vector Machines (SVM) for predictions based on agricultural data. The dataset includes various parameters affecting crop production, and the model is trained to provide accurate yield estimates.

🚀 Features

Train a Support Vector Machine (SVM) model for yield prediction.

Load and process crop data from CSV files.

Store and manage data using SQLite.

Run predictions using a pre-trained model.

Provide an easy-to-use Python script for inference.

🔧 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/RTRP.git
cd RTRP/crop-yield

2️⃣ Install Dependencies

Ensure you have Python installed, then install required packages:

pip install -r requirements.txt

3️⃣ Run the Application

python app.py

📊 Model Training

If you want to train the model from scratch, use the Jupyter Notebook:

jupyter notebook svm.ipynb

The trained model will be saved as SVM_model.joblib.

🏗 Project Structure

RTRP/
│── crop-yield/
│   │── app.py             # Main application script
│   │── crop_yield.db      # SQLite database
│   │── data.csv           # Dataset
│   │── requirements.txt   # Dependencies
│   │── svm.ipynb          # Model training notebook
│   │── SVM_model.joblib   # Trained model
│   │── test.py            # Testing script

📌 How to Use

Run app.py to start the application.

Use test.py to validate predictions.

Modify data.csv to test with new data.

🛠 Technologies Used

Programming Language: Python

Machine Learning: Scikit-Learn, SVM

Database: SQLite

Libraries: Pandas, NumPy, Flask (if used for API)

📜 License

This project is licensed under the MIT License.

📬 Contact

For any inquiries or contributions, feel free to reach out or raise an issue on GitHub!

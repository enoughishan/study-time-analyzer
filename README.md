Study Time Analyzer using Python

Overview

The Study Time Analyzer is a simple Python-based project that helps students analyze their study habits using a CSV file.
It calculates useful statistics like total study time, average daily study time, most studied subject, and also displays graphs for better understanding.

This project is designed to be beginner-friendly

---

Features

- Upload your own CSV file or use a default dataset
- Calculates:
   - Total study hours
   - Average daily study time
   - Most studied subject
   - Total number of study sessions
- Visual representation using graphs
- Simple and readable Python code
- User interface built with Gradio

---

Technologies Used

- Python
- Pandas
- Matplotlib
- Gradio
- OS module

---

Dataset Format

Your CSV file should contain the following columns:

Column Name| Description
Date| Date of study session
Subject| Subject studied
Duration_Minutes| Study time in minutes

Example:

Date,Subject,Duration_Minutes
2024-01-01,Math,60
2024-01-01,Physics,45
2024-01-02,Chemistry,30

---

How It Works

1. The user uploads a CSV file (optional).
2. If no file is uploaded, the program uses a default CSV file.
3. The data is read using Pandas.
4. Basic calculations are performed using simple logic.
5. Graphs are generated using Matplotlib.
6. Results and graphs are displayed using Gradio.

---

How to Run the Project

Step 1: Install Required Libraries

pip install pandas matplotlib gradio

Step 2: Run the Python File

python app.py

Or run the notebook if you are using Jupyter/Colab.

Step 3: Open the Web Interface

Gradio will generate a local URL. Open it in your browser, upload a CSV file, and view the results.

---

Project Use Cases

- Students tracking daily study habits
- Beginners learning Pandas and data visualization
- Academic mini-project for Python or Data Analysis
- Practice project for Gradio-based interfaces

---

Folder Structure

Study-Time-Analyzer/
│
├── study_logs.csv
├── app.py / notebook.ipynb
├── README.md
└── requirements.txt

---


Author


Ishant kumar
6605763
G1

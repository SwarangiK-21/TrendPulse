# ⚡ TrendPulse: AI Brand Intelligence Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://trendpulse-yourname.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-green)

**TrendPulse** is an end-to-end analytics engine that correlates **Social Media Sentiment** with **Real-Time Sales Performance**. It bridges the gap between raw social buzz and actual financial ROI, providing brands with actionable insights in a cinematic, dark-mode interface.

## 🚀 Live Demo
### [👉 Click here to view the Live Dashboard](https://ht85kr9hvauxnnjaa8odye.streamlit.app/)

---

## 🌟 Key Features

* **Real-Time KPI Tracking:** Monitors Total Revenue, Transaction Volume, and Social Mentions live.
* **Interactive Filtering:** Sidebar controls allow users to slice data by specific social platforms (Instagram, Twitter, Reddit, etc.).
* **Advanced Visualizations:**
    * **Revenue Trajectory:** Interactive Area charts using Plotly.
    * **Platform Split:** Donut charts for demographic analysis.
* **Sentiment Deep Dive:** A "Pro" data table featuring embedded **progress bars** to visualize AI confidence scores (-1 to +1).
* **Cinematic UI:** Custom Dark Mode styling with a focus on User Experience (UX).

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (Python Web Framework)
* **Visualization:** [Plotly Express](https://plotly.com/python/) (Interactive Charts)
* **Data Processing:** Pandas & NumPy
* **Database:** SQLite (Relational DB)
* **Deployment:** Streamlit Community Cloud

---

## 💻 How to Run Locally

If you want to clone and run this application on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/TrendPulse.git](https://github.com/YourUsername/TrendPulse.git)
    cd TrendPulse
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app:**
    ```bash
    streamlit run app.py
    ```

---

## 📂 Project Structure

```text
TrendPulse/
├── .streamlit/          # UI Configuration (Dark Mode colors)
├── app.py               # Main Application Logic
├── db_setup.py          # Database initialization script
├── trendpulse.db        # SQLite Database (Sales & Social Data)
├── requirements.txt     # Python dependencies
└── README.md            # Documentation

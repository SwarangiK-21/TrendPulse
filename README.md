# ⚡ TrendPulse: Real-Time Brand Intelligence & Sentiment Analytics Engine

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://trendpulse-yourname.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Data Engineering](https://img.shields.io/badge/Data%20Engineering-ETL-orange?style=for-the-badge)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Production-success?style=for-the-badge)

> **"Data is the new soil."** — TrendPulse is an end-to-end Decision Support System (DSS) engineered to bridge the gap between unstructured social chatter and structured financial performance.

## 📖 Executive Summary
In the modern digital economy, brand reputation directly correlates with revenue, yet most organizations lack the tools to visualize this relationship in real-time.

**TrendPulse** solves this by ingesting cross-platform social signals, applying NLP-driven sentiment analysis, and correlating these metrics with transaction data. It transforms "Internet Noise" into actionable "Business Signals," enabling stakeholders to monitor Brand Health and ROI through a single pane of glass.

## 🚀 Live Deployment
### [👉 Launch the Market Command Center](https://ht85kr9hvauxnnjaa8odye.streamlit.app/)

---
Key Features
📊 1. Real-Time Market Correlation
Instantaneously tracks Total Revenue, Transaction Volume, and Social Velocity.

Calculates month-over-month growth deltas to highlight performance trends.

🧠 2. AI-Driven Sentiment Deep Dive
"Pro" Data Table: Features embedded progress bars within the data grid to visualize sentiment polarity at a glance.

Confidence Scoring: Filters out low-confidence data points to ensure analytical accuracy.

🔎 3. Interactive Granularity
Multi-Dimensional Filtering: Sidebar controls allow analysts to slice data by specific social platforms (Instagram, Twitter, Reddit) without reloading the entire application state.

Dynamic Visualizations:

Revenue Trajectory: Area charts for spotting financial anomalies.

Platform Split: Donut charts for demographic segmentation.
---

## 🏗️ System Architecture & Data Pipeline

This project moves beyond simple scripting to demonstrate a **Full-Stack Data Engineering** workflow:

```mermaid
graph LR
    A[Raw Data Sources] -->|SQL Ingestion| B(ETL & Preprocessing)
    B -->|Pandas & NLP| C{Sentiment Analysis Engine}
    C -->|Structured Data| D[SQLite Database]
    D -->|Query Optimization| E[Streamlit Application]
    E -->|Visualization| F[Plotly Interactive Charts]
    E -->|Reporting| G[Business Intelligence Layer]

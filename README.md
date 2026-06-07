# Autonomous Data Analyst Agent

## Overview

Autonomous Data Analyst Agent is an AI-powered system designed to automate the complete workflow of a Data Analyst and Junior Data Scientist.

The system accepts structured datasets (CSV/XLSX), performs automated data understanding, data quality assessment, exploratory data analysis (EDA), feature engineering, model training, evaluation, insight generation, report creation, and conversational data analysis.

The long-term goal is to build a multi-agent system using LangGraph capable of performing end-to-end analytical workflows with minimal human intervention.

---

## Project Objectives

* Automate dataset understanding
* Automate data quality assessment
* Perform exploratory data analysis (EDA)
* Handle missing values and outliers
* Generate meaningful visualizations
* Perform feature engineering
* Train and compare machine learning models
* Generate business insights
* Produce downloadable reports
* Enable natural language interaction with data

---

## End-to-End Workflow

```text
User Upload Dataset
        ↓
Dataset Understanding
        ↓
Data Quality Analysis
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis (EDA)
        ↓
Feature Engineering
        ↓
AutoML Training
        ↓
Model Evaluation
        ↓
Insight Generation
        ↓
Report Generation
        ↓
Chat With Data
```

---

## Project Architecture

```text
Coordinator Agent
│
├── Dataset Understanding Agent
├── Data Quality Agent
├── Data Cleaning Agent
├── EDA Agent
├── Feature Engineering Agent
├── AutoML Agent
├── Insight Generation Agent
├── Reporting Agent
└── Chat Agent
```

---

## Repository Structure

```text
autonomous-data-analyst-agent/

├── datasets/
│   ├── raw/
│   ├── processed/
│   └── inventory/
│
├── docs/
│   ├── dataset_notes/
│   ├── requirements/
│   └── meeting_notes/
│
├── src/
│   ├── core/
│   ├── dataset_understanding/
│   ├── data_quality/
│   ├── data_cleaning/
│   ├── eda/
│   ├── feature_engineering/
│   ├── automl/
│   ├── insights/
│   ├── reporting/
│   ├── chat_with_data/
│   ├── agents/
│   ├── workflows/
│   └── utils/
│
├── notebooks/
├── reports/
├── tests/
├── app/
├── config/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Tech Stack

### Data Processing

* Pandas
* NumPy
* Polars

### Visualization

* Plotly
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn
* XGBoost
* LightGBM
* CatBoost

### AutoML

* AutoGluon
* FLAML
* PyCaret

### LLM & Agent Framework

* LangChain
* LangGraph
* OpenAI
* Claude

### Frontend

* Streamlit

### Reporting

* Jinja2
* ReportLab
* WeasyPrint

---

## Dataset Coverage

The project is being designed and validated against multiple dataset categories:

* Classification
* Regression
* Time Series
* Imbalanced Datasets
* Healthcare Analytics
* Finance Analytics
* Customer Analytics
* Sales Forecasting
* High-Dimensional Data
* Mixed Feature Datasets

---

## Current Status

### Phase 1 - Dataset Research & Requirement Analysis

* [ ] Collect representative datasets
* [ ] Create dataset inventory
* [ ] Document dataset characteristics
* [ ] Identify common analytical patterns

### Upcoming Phases

* [ ] Dataset Understanding Module
* [ ] Data Quality Module
* [ ] EDA Automation Module
* [ ] Feature Engineering Module
* [ ] AutoML Module
* [ ] Insight Generation Module
* [ ] Reporting Module
* [ ] LangGraph Multi-Agent System

---

## Contributors

* Kishore Kannan N
* Mohammad Faizaan

---

## Vision

Build a production-ready Autonomous Data Analyst Agent capable of transforming raw datasets into actionable insights through AI-driven automation.

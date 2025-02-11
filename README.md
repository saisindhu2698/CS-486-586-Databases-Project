# 🏥 Health Insurance Marketplace Project

## 📌 Overview

The **Health Insurance Marketplace** system is designed to efficiently process and manage health insurance data, including **users, plans, claims, and providers**. It utilizes **PostgreSQL** as the relational database management system (RDBMS) and **Python** for data processing, cleaning, and validation. The system ensures **efficient data management, accurate query execution, and meaningful insights** into health insurance trends.

---

## 🚀 Features

- **User Management:** Stores user details, including personal and insurance-related information.
- **Insurance Plans:** Maintains records of available health insurance plans with relevant details.
- **Claims Processing:** Tracks claims submitted by users and their processing status.
- **Providers Information:** Manages details of healthcare providers participating in the marketplace.
- **Data Validation:** Executes SQL queries to ensure data integrity and accuracy.
- **Automated Data Processing:** Uses Python scripts to streamline data import, validation, and analysis.

---

## 🛠 Technologies Used

- **PostgreSQL:** Structured database management and query execution.
- **Python (Pandas, psycopg2):** Data processing, cleaning, and SQL query execution.
- **Excel:** Initial data structuring, normalization, and pre-processing.
- **SQL:** Querying, validating, and analyzing datasets.

---

## 📂 Database Schema

The system is structured into the following tables for efficient data management:

- **Users Table:** Stores user details, including personal information and insurance enrollment.
- **Plans Table:** Contains details of available insurance plans, including coverage and pricing.
- **Claims Table:** Tracks claims filed by users, their statuses, and approval details.
- **Providers Table:** Maintains healthcare provider records, including affiliations and services offered.

---

## 🧹 Data Cleaning & Processing

Data preparation was carried out using **Excel and Python** to ensure consistency and accuracy. The process involved:

✅ Removing extra spaces and formatting inconsistencies in column names.  
✅ Dropping duplicate and incomplete records.  
✅ Converting data types for seamless integration with PostgreSQL.  
✅ Structuring data into a **normalized format** before importing into the database.  
✅ Running validation queries using Python to check **data accuracy**.  

---

## 📊 Sample Queries

The system supports various queries for **data retrieval and analysis**, including:

🔹 Listing all users enrolled in a specific insurance plan.  
🔹 Retrieving details of claims submitted within a specified time frame.  
🔹 Identifying the most frequently used healthcare providers.  
🔹 Calculating the total number of claims approved for a given period.  
🔹 Finding users who have not submitted any claims in the past year.  

---


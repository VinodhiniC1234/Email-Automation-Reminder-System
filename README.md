# 📧 Email Automation & Reminder System

A Python-based automation project that sends scheduled emails, generates reminders, logs execution status, and creates visual analytics reports using charts.

---

## 🚀 Project Overview

The **Email Automation & Reminder System** is designed to automate repetitive email tasks such as reminders, notifications, and alerts. It reads contact data from CSV files, applies email templates, and sends personalized emails using SMTP.

It also generates **visual reports (images)** and logs system activity for tracking performance.

---

## 🎯 Problem Statement

Manually sending reminder emails is:
- Time-consuming
- Error-prone
- Not scalable

This project solves it by:
✔ Automating email sending  
✔ Scheduling reminders  
✔ Tracking success/failure  
✔ Generating visual reports  

---

## 🏢 Real-World Applications

- HR interview reminders  
- Payment due alerts  
- Webinar notifications  
- Sales follow-ups  
- Task deadline alerts  
- Academic reminder systems  

---

## ⚙️ Features

- 📂 CSV-based contact management  
- ✉️ Automated email sending (SMTP)  
- ⏰ Reminder scheduling system  
- 🧾 Logging system (success/failure tracking)  
- 📊 Auto-generated analytics charts  
- 🖼 Saves output images in `images/` folder  
- 📄 CSV report generation  
- 🔐 Secure credential handling using `.env`  

---

## 🛠 Tech Stack

- Python 🐍  
- Pandas  
- SMTP (smtplib)  
- Matplotlib  
- Seaborn  
- Python-dotenv  
- Schedule  

---

## 📁 Project Structure

```text
Email-Automation-Reminder-System/
│
├── data/
│   └── contacts.csv
├── src/
│   ├── email_sender.py
│   ├── logger.py
│
├── outputs/
│   └── report.csv
│
├── logs/
│   └── app.log
│
├── images/
│   ├── 1_kpi_dashboard.png
│   ├── 2_email_pie.png
│   ├── 3_contact_activity.png
│   ├── 4_execution_timeline.png
│
├── main.py
├── requirements.txt
└── README.md

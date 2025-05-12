# 🧠 Quotes App

A **full-stack Python application** with a Flask backend, MongoDB database, and a Tkinter-based frontend for managing inspirational quotes.

---

## 🌟 Features
- **Fetch Random Quotes** from MongoDB via Flask API.
- **Add New Quotes** via GUI or API calls.
- **Structured Project** (Frontend + Backend).

---

## 🛠️ Technologies
- **Python**: Flask, customtkinter, pymongo, requests
- **MongoDB**: Persistent storage
- **GitHub**: Version control

---

## 📁 Project Structure
```
py-proj/
├── backend/
│   ├── app.py             # Flask API entry point
│   ├── db.py              # MongoDB connection logic
│   ├── routes/quotes.py   # API routes for quotes
│   └── seed_quotes.py     # Data seeding script
│
├── frontend/
│   └── gui.py             # GUI built with customtkinter
│
├── requirements.txt
└── README.md
```

---

## 🚀 Quickstart

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Backend
```bash
python3 -m backend.app
```

### 3️⃣ Run the Frontend
```bash
python3 frontend/gui.py
```

---

## 📌 API Endpoints

### **GET** `/api/quote`
Fetch a random quote.

### **POST** `/api/quote`
Add a new quote. Example payload:
```json
{ "text": "Your inspiring quote here" }
```

---

## 📄 License
This project is licensed under the **MIT License**.

---

## ✅ Push to GitHub
From your root folder:
```bash
git add .
git commit -m "Finalized Quotes App with full CRUD and GUI"
git push origin main
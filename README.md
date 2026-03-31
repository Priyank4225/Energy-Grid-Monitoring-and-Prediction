# ⚡ Maharashtra Energy Grid Dashboard

A real-time energy monitoring dashboard for Maharashtra that visualizes power generation data from official government reports and (future) integrates machine learning for predictive analytics based on climate data.

---

## 🚀 Features

* 📊 Dynamic dashboard with sector-wise breakdown:

  * State Sector
  * Private Sector
  * Central Sector
* 🥧 Interactive pie charts using Chart.js
* 📅 Automatically fetches latest available DGR (Daily Generation Report).
* ⚡ FastAPI backend serving cleaned and structured data
* 🌐 Simple and responsive frontend (HTML + JS)
* 🔮 Future-ready for ML-based energy prediction

---

## 🏗️ Project Structure

```
Energy-Grid-Monitoring-and-Prediction/
│
├──Backend/
|   ├── main.py
|   └── fetch_data.py
|
├── Frontend/
│   └── index.html
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## ⚙️ Backend Setup (FastAPI)

### 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate     # Linux / Mac
venv\Scripts\activate        # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run server

```bash
python Backend/main.py
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 🌐 Frontend Setup

Simply open:

```
Frontend/index.html
```

Or use a live server:

```bash
npx serve Frontend
```

---

## 🔗 API Endpoint

### `GET /`

Returns cleaned Maharashtra sector-wise energy data:

```json
[
  {
    "Type": "STATE SECTOR",
    "Capacity": 10000,
    "Expected": 8000,
    "Production": 7500,
    "Unavailable Capacity": 1500
  },
  ...
  {
    "date": "25-03-2026"
  }
]
```

---

## 📊 Data Source

* Central Electricity Authority (CEA)
* Daily Generation Reports (DGR)

---

## ⚠️ Notes

* Data is scraped dynamically — format changes may break parsing
* Uses `.xls` format → requires `xlrd`
* Backend is currently synchronous (can be optimized later)

---

## 🔮 Future Enhancements

* 🤖 Machine Learning model for:

  * Energy demand prediction
  * Climate-based generation forecasting
* 🌦️ Weather API integration
* 📈 Trend analysis charts (time-series)
* 🧠 Sector efficiency insights
* 🐳 Docker deployment
* ☁️ Cloud hosting (AWS / GCP)

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* Pandas
* Requests

### Frontend

* HTML / CSS / JavaScript
* Chart.js

---

## 🧪 Example Use Case

* Monitor Maharashtra energy production daily
* Analyze sector-wise performance
* Predict future generation based on weather conditions (planned)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

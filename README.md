# LOGISENSE AI 🚀
### Predictive Logistics & Supply Intelligence Platform

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Next.js](https://img.shields.io/badge/Next.js-15-black?style=flat-square&logo=next.js&logoColor=white)](https://nextjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4+-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white)](https://tailwindcss.com)

**LOGISENSE AI** is an AI-powered predictive logistics and resilient supply chain decision-support platform designed for extreme weather, high-altitude corridors, and critical inventory management.

---

## 🌟 Key Capabilities

- 🤖 **ML Demand Forecasting**: Machine-learning driven consumption predictions using `RandomForestRegressor` trained on historical consumption, weather conditions, road status, and seasonal parameters.
- ⚡ **Dynamic Risk Assessment**: Real-time multi-factor risk scoring evaluating weather severity, route blockages, inventory depletion, and convoy delays.
- 🗺️ **Interactive Geographic Map**: Leaflet-based geospatial visualization of supply hubs, border outposts, transit corridors, and active convoy locations with weather overlays.
- 🚨 **Proactive Alert Engine**: Automatic detection and threshold-based alert generation for critical shortages, road closures, and adverse weather conditions.
- 🚚 **Transport & Fleet Monitoring**: Fleet tracking, asset operational readiness, capacity utilization, and dynamic dispatch recommendations.
- 📦 **Inventory & Stock Health**: Real-time buffer stock monitoring, stockout predictions, and automated reorder triggers.

---

## 🏗️ Architecture & Tech Stack

```text
SIH-PROJECT (sih2)
├── backend/                  # FastAPI Application
│   ├── app/
│   │   ├── routers/          # API endpoints (forecast, alerts, inventory, routes, etc.)
│   │   ├── forecasting.py    # Random Forest regression model & feature pipeline
│   │   ├── risk_engine.py    # Composite risk calculation engine
│   │   ├── logistics.py      # Route planning & dispatch algorithms
│   │   ├── models.py         # SQLAlchemy ORM models
│   │   └── seed.py           # Database seeder (hubs, routes, assets, weather)
│   ├── data/                 # SQLite database & serialized ML models (.joblib)
│   └── requirements.txt
│
└── frontend/                 # Next.js 15 Web Application
    ├── app/                  # App Router pages (dashboard, map, forecast, risk, etc.)
    ├── components/           # Reusable UI components, charts, gauges, map views
    ├── lib/                  # API client, navigation, and utility helpers
    └── package.json
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- **Node.js 18+** & **npm**

---

### 1. Backend Setup (FastAPI)

```bash
cd backend

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables (optional, defaults to SQLite)
cp .env.example .env

# Initialize and seed database with demo data
python -m app.seed

# Start FastAPI server
uvicorn app.main:app --reload --port 8000
```

The API will be available at:
- **API Server**: [http://localhost:8000](http://localhost:8000)
- **Interactive Swagger Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc Documentation**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

### 2. Frontend Setup (Next.js)

```bash
cd frontend

# Install packages
npm install

# Configure environment variables
cp .env.example .env.local

# Run development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser to explore the dashboard.

---

## 📡 API Endpoints Overview

| Route | Method | Description |
|---|---|---|
| `/api/dashboard/overview` | `GET` | Aggregated KPIs, summary status, high-level alerts |
| `/api/forecast/predict` | `POST` | ML-driven consumption forecast by location & category |
| `/api/risk/overview` | `GET` | High-level risk metrics and sector breakdown |
| `/api/routes` | `GET` | Route network, segment status, and distance metrics |
| `/api/transport/assets` | `GET` | Active transport assets and fleet operational readiness |
| `/api/inventory` | `GET` | Stock levels, buffer status, and reorder alerts |
| `/api/alerts` | `GET` | Filterable log of operational and safety alerts |
| `/api/weather` | `GET` | Real-time and synthetic weather condition records |

---

## 🛡️ License

This project is built for the **Smart India Hackathon (SIH)**.
Licensed under the [MIT License](LICENSE) (or applicable competition guidelines).

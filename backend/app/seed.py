import logging
from sqlalchemy import delete
from app.database import SessionLocal, init_db
from app.models import Location, InventoryItem, Route, Alert, TransportAsset, utcnow
from app.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("seed")

LOCATIONS = [
    ("LOC-HUB", "Central Supply Hub", "HUB", 31.5, 77.1, 640, "Plains", "Northern Sector"),
    ("LOC-BRD-S", "Border Node South", "FORWARD", 32.5, 77.8, 3800, "Highland", "Border Zone"),
    ("LOC-BRD-M", "Central Border Post", "FORWARD", 33.2, 77.7, 4100, "Highland", "Border Zone"),
    ("LOC-BRD-N", "North Border Node", "FORWARD", 34.0, 77.8, 4200, "Highland", "Border Zone"),
]

def seed_transport(db):
    TRANSPORT = [
        ("TR-S1", "Border Hauler 1", "Truck", 3000.0, "AVAILABLE", "Border Support", "LOC-BRD-S"),
        ("TR-S2", "Border Hauler 2", "Truck", 3000.0, "AVAILABLE", "Border Support", "LOC-BRD-S"),
        ("TR-M1", "Post Utility 1", "Utility Vehicle", 1500.0, "AVAILABLE", "Post Resupply", "LOC-BRD-M"),
        ("TR-M2", "Post Utility 2", "Utility Vehicle", 1500.0, "MAINTENANCE", "Post Resupply", "LOC-BRD-M"),
        ("TR-N1", "Ridge Hauler 1", "Truck", 2000.0, "IN_TRANSIT", "Highland Path", "LOC-BRD-M"),
        ("TR-N2", "Ridge Tanker 1", "Tanker", 4000.0, "AVAILABLE", "Fuel Supply", "LOC-BRD-N"),
        ("TR-H1", "Hub Hauler 1", "Truck", 5000.0, "AVAILABLE", "Hub to Hub", "LOC-HUB"),
    ]
    for t in TRANSPORT:
        db.add(TransportAsset(asset_id=t[0], name=t[1], asset_type=t[2], capacity_kg=t[3], status=t[4], current_assignment=t[5], origin_id=t[6]))
    db.commit()

def seed_alerts(db):
    alerts = [
        ("ALR-001", "CRITICAL", "Fuel Depletion Warning", "Border post S fuel stocks low", "Inventory", "Replenish immediately", "NEW"),
        ("ALR-002", "HIGH", "Severe Weather Alert", "High winds at Central Border Post", "Weather", "Diversion required", "NEW"),
        ("ALR-003", "MEDIUM", "Maintenance Due", "Border Hauler 1", "Transport", "Scheduled service", "ACKNOWLEDGED"),
        ("ALR-004", "LOW", "Routine Check", "All nodes nominal", "System", "N/A", "RESOLVED"),
        ("ALR-005", "HIGH", "Unexpected Demand", "High food consumption at North", "Demand", "Initiate audit", "NEW"),
    ]
    for a in alerts:
        db.add(Alert(alert_code=a[0], severity=a[1], title=a[2], description=a[3], category=a[4], recommended_action=a[5], status=a[6]))
    db.commit()

def seed_weather(db):
    from app.models import WeatherRecord
    records = [
        WeatherRecord(location_id="LOC-HUB", temperature=18.0, rainfall=5.0, visibility_km=10.0, snow_probability=0.0, wind_speed=12.0, weather_risk=15.0, severity="LOW", condition="Clear", source="SYNTHETIC", observed_at=utcnow()),
        WeatherRecord(location_id="LOC-BRD-S", temperature=6.0, rainfall=25.0, visibility_km=6.0, snow_probability=10.0, wind_speed=28.0, weather_risk=45.0, severity="MEDIUM", condition="Moderate Rain", source="SYNTHETIC", observed_at=utcnow()),
        WeatherRecord(location_id="LOC-BRD-M", temperature=-2.0, rainfall=40.0, visibility_km=3.5, snow_probability=65.0, wind_speed=42.0, weather_risk=72.0, severity="HIGH", condition="Snow Squall", source="SYNTHETIC", observed_at=utcnow()),
        WeatherRecord(location_id="LOC-BRD-N", temperature=-6.0, rainfall=55.0, visibility_km=2.0, snow_probability=85.0, wind_speed=55.0, weather_risk=85.0, severity="CRITICAL", condition="Blizzard", source="SYNTHETIC", observed_at=utcnow()),
    ]
    db.add_all(records)
    db.commit()

def seed_full():
    init_db()
    with SessionLocal() as db:
        from app.models import WeatherRecord
        for m in [Alert, Route, TransportAsset, InventoryItem, Location, WeatherRecord]: db.execute(delete(m))
        
        for l in LOCATIONS:
            db.add(Location(id=l[0], name=l[1], node_type=l[2], latitude=l[3], longitude=l[4], elevation_m=l[5], terrain=l[6], region=l[7]))
        
        for l in LOCATIONS:
            for cat, cap in [("Fuel", 50000), ("Food", 20000), ("Water", 30000)]:
                db.add(InventoryItem(item_code=f"INV-{l[0]}-{cat}", name=f"{cat} Reserve", category=cat, unit="L" if cat!="Food" else "kg", location_id=l[0], current_stock=cap*0.5, capacity=cap, safety_threshold=cap*0.2, daily_consumption=cap*0.05, updated_at=utcnow()))
        
        db.add(Route(route_code="RT-1", origin_id="LOC-HUB", destination_id="LOC-BRD-S", distance_km=180.0, estimated_time_hours=6.0, base_risk_score=50.0, weather_risk=40.0, terrain_risk=40.0, road_condition="POOR", transport_capacity_kg=3000.0, status="OPEN", path=[[31.5, 77.1], [32.5, 77.8]]))
        
        seed_transport(db)
        seed_alerts(db)
        seed_weather(db)
        
        db.commit()
    logger.info("Seeded functional demo data with more assets, alerts, and weather")

if __name__ == "__main__": seed_full()

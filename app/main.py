
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
import datetime

app = FastAPI(title="Flood OS API")

THRESHOLD_WATER_CM = 250
THRESHOLD_RAIN_MM = 50

@app.get("/api/status")
def get_status():
    water_level = random.randint(100, 300)
    rainfall = random.randint(0, 80)
    risk = "HIGH" if water_level > THRESHOLD_WATER_CM or rainfall > THRESHOLD_RAIN_MM else "LOW"
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "water_level_cm": water_level,
        "rainfall_mm_hr": rainfall,
        "risk_level": risk,
        "alert": risk == "HIGH"
    }

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
    <h1>Flood OS Dashboard</h1>
    <p>Check /api/status for live data</p>
    """

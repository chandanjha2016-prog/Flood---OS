from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random, datetime

app = FastAPI(title="Flood OS")

@app.get("/api/status")
def get_status():
    water = random.randint(120, 280)
    rain = random.randint(0, 70)
    risk = "HIGH" if water > 250 or rain > 50 else "SAFE"
    return {"water_level_cm": water, "rainfall_mm_hr": rain, "risk_level": risk, "alert": risk=="HIGH", "timestamp": datetime.datetime.now().isoformat()}

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """<!DOCTYPE html><html><head><title>Flood OS</title><style>body{font-family:Arial;background:#eff6ff;padding:20px}.card{background:white;border-radius:16px;box-shadow:0 4px 10px rgba(0,0,0,0.1);padding:20px;max-width:600px;margin:auto}h1{color:#1d4ed8}.box{background:#dbeafe;padding:12px;border-radius:8px;margin:10px 0}.safe{background:#22c55e;color:white;padding:12px;border-radius:8px;font-weight:bold}.danger{background:#ef4444;color:white;padding:12px;border-radius:8px;font-weight:bold}</style></head><body><div class="card"><h1>🌊 Flood OS v0.1.0</h1><p style="color:gray">Patna, Bihar | Community Early Warning</p><div id="data"></div><div id="alert"></div><p style="font-size:12px;color:red">⚠️ For emergencies call: 1077 / 112</p></div><script>async function load(){let r=await fetch('/api/status');let d=await r.json();document.getElementById('data').innerHTML=`<div class="box"><b>Water Level:</b> ${d.water_level_cm} cm</div><div class="box"><b>Rainfall:</b> ${d.rainfall_mm_hr} mm/hr</div><div class="box"><b>Risk:</b> ${d.risk_level}</div><small>Last: ${d.timestamp}</small>`;document.getElementById('alert').className=d.alert?'danger':'safe';document.getElementById('alert').innerHTML=d.alert?'⚠️ HIGH RISK - Evacuate':'✅ SAFE - All normal'}load();setInterval(load,5000)</script></body></html>"""

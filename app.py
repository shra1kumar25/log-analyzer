from fastapi import FastAPI, UploadFile, File

from analyzer import analyze_text_file, analyze_json, analyze_excel
from email_sender import send_email

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Log Analyzer API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/analyze/text")
def analyze_text(file: UploadFile = File(...)):
    filename = "uploaded.txt"

    with open(filename, "wb") as output:
        output.write(file.file.read())

    alerts = analyze_text_file(filename)

    if alerts:
        send_email(alerts)

    return {
        "filename": file.filename,
        "alerts": alerts,
        "alert_count": len(alerts)
    }


@app.post("/analyze/json")
def analyze_json_file(file: UploadFile = File(...)):
    filename = "uploaded.json"

    with open(filename, "wb") as output:
        output.write(file.file.read())

    alerts = analyze_json(filename)

    if alerts:
        send_email(alerts)

    return {
        "filename": file.filename,
        "alerts": alerts,
        "alert_count": len(alerts)
    }


@app.post("/analyze/excel")
def analyze_excel_file(file: UploadFile = File(...)):
    filename = "uploaded.xlsx"

    with open(filename, "wb") as output:
        output.write(file.file.read())

    alerts = analyze_excel(filename)

    if alerts:
     send_email(alerts)

    return {
        "filename": file.filename,
        "alerts": alerts,
        "alert_count": len(alerts)
    }

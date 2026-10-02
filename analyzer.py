SEVERITY_RANK = {
    "DEBUG": 1,
    "INFO": 2,
    "NOTICE": 3,
    "WARNING": 4,
    "ERROR": 5,
    "CRITICAL": 6,
    "ALERT": 7,
    "EMERGENCY": 8,
}


DIGITS = "0123456789"


def mask_digits(text):
    out = []

    for ch in text:
        if ch in DIGITS:
            out.append("#")
        else:
            out.append(ch)

    return "".join(out)


import json
import pandas as pd


def analyze_text_file(filename):
    alerts = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if "." not in line:
                continue

            _, message = line.split(".", 1)
            message = message.strip()

            level = ""

            for severity in SEVERITY_RANK:
                if message.startswith(severity):
                    level = severity
                    break

            if level and SEVERITY_RANK[level] >= SEVERITY_RANK["WARNING"]:
                clean_message = message[len(level):].lstrip(": ")

                alerts.append(
                    {
                        "level": level,
                        "message": mask_digits(clean_message),
                    }
                )

    alerts.sort(
        key=lambda alert: SEVERITY_RANK[alert["level"]],
        reverse=True
    )

    return alerts


def analyze_json(filename):
    alerts = []

    with open(filename, "r") as file:
        data = json.load(file)

    for log in data.get("logs", []):
        message = log.get("message", "")

        level = ""

        for severity in SEVERITY_RANK:
            if message.startswith(severity):
                level = severity
                break

        if level and SEVERITY_RANK[level] >= SEVERITY_RANK["WARNING"]:
            clean_message = message[len(level):].lstrip(": ")

            alerts.append(
                {
                    "level": level,
                    "message": mask_digits(clean_message),
                }
            )

    alerts.sort(
        key=lambda alert: SEVERITY_RANK[alert["level"]],
        reverse=True
    )

    return alerts


def analyze_excel(filename):
    df = pd.read_excel(filename)

    df["severity_rank"] = df["level"].map(SEVERITY_RANK)

    alerts = df[df["severity_rank"] >= SEVERITY_RANK["WARNING"]]

    alerts = alerts.sort_values(
        by="severity_rank",
        ascending=False
    )

    return [
        {
            "level": row["level"],
            "message": mask_digits(row["message"]),
        }
        for _, row in alerts.iterrows()
    ]

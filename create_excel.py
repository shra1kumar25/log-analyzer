import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5, 6],
    "level": [
        "INFO",
        "WARNING",
        "ERROR",
        "INFO",
        "ERROR",
        "WARNING"
    ],
    "message": [
        "Application started",
        "Database connection is slow",
        "Database connection failed",
        "User logged in",
        "Student details could not be fetched",
        "Low disk space"
    ]
}

df = pd.DataFrame(data)

df.to_excel("logs.xlsx", index=False)

print("Excel file created successfully")

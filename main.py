from analyzer import analyze_text_file
from analyzer import analyze_json
from analyzer import analyze_excel


print("===== TEXT FILE =====")

text_alerts = analyze_text_file("abc.txt")

for alert in text_alerts:
    print(alert)


print("\n===== JSON FILE =====")

json_alerts = analyze_json("abc.json")

for alert in json_alerts:
    print(alert)


print("\n===== EXCEL FILE =====")

excel_alerts = analyze_excel("logs.xlsx")

for alert in excel_alerts:
    print(alert)

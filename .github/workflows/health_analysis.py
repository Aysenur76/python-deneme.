# Sağlık Verisi Analizi

# Hasta listesi
patients = [
    {"name": "Ali", "age": 30, "height": 1.75, "weight": 72},
    {"name": "Ayşe", "age": 45, "height": 1.60, "weight": 85},
    {"name": "Mehmet", "age": 50, "height": 1.80, "weight": 95},
    {"name": "Zeynep", "age": 28, "height": 1.65, "weight": 55}
]

# BMI hesaplama
def calculate_bmi(weight, height):
    try:
        return weight / (height ** 2)
    except ZeroDivisionError:
        return 0

# BMI sınıflandırma
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Zayıf"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Fazla Kilolu"
    else:
        return "Obez"

# Analiz
total_bmi = 0
highest_bmi_patient = None

print("🏥 Sağlık Verisi Analizi")
for p in patients:
    bmi = calculate_bmi(p["weight"], p["height"])
    status = classify_bmi(bmi)
    total_bmi += bmi

    if highest_bmi_patient is None or bmi > highest_bmi_patient["bmi"]:
        highest_bmi_patient = {"name": p["name"], "bmi": bmi, "status": status}

    print(f"{p['name']} - Yaş: {p['age']} - BMI: {bmi:.2f} - Durum: {status}")

average_bmi = total_bmi / len(patients)

print(f"\nOrtalama BMI: {average_bmi:.2f}")
print(f"En riskli hasta: {highest_bmi_patient['name']} ({highest_bmi_patient['bmi']:.2f}) - {highest_bmi_patient['status']}")

# Dosyaya yazma
with open("health_results.txt", "w", encoding="utf-8") as f:
    f.write("🏥 Sağlık Verisi Analizi\n")
    for p in patients:
        bmi = calculate_bmi(p["weight"], p["height"])
        status = classify_bmi(bmi)
        f.write(f"{p['name']} - Yaş: {p['age']} - BMI: {bmi:.2f} - Durum: {status}\n")
    f.write(f"\nOrtalama BMI: {average_bmi:.2f}\n")
    f.write(f"En riskli hasta: {highest_bmi_patient['name']} ({highest_bmi_patient['bmi']:.2f}) - {highest_bmi_patient['status']}\n")

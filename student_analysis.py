import pandas as pd

# Basit öğrenci veri seti
data = {
    "student": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Elif", "Mert", "Ece"],
    "math_score": [78, 85, 92, 64, 88, 73, 95, 81],
    "english_score": [82, 79, 88, 70, 90, 75, 96, 84]
}

df = pd.DataFrame(data)

# Ortalama hesaplama
df["average"] = (df["math_score"] + df["english_score"]) / 2

print("GENEL ANALİZ")
print("----------------")

print("Math ortalaması:", df["math_score"].mean())
print("English ortalaması:", df["english_score"].mean())
print("Genel en yüksek ortalama:", df["average"].max())
print("Genel en düşük ortalama:", df["average"].min())

# En başarılı öğrenci
best_student = df.loc[df["average"].idxmax()]

print("\nEN BAŞARILI ÖĞRENCİ")
print(best_student)

# 85 üstü öğrenciler
high_performers = df[df["average"] > 85]

print("\n85 ÜSTÜ ÖĞRENCİLER")
print(high_performers)

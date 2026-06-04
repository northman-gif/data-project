import pandas as pd
import matplotlib.pyplot as plt

# Veri seti
data = {
    "student": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Elif", "Mert", "Ece"],
    "math_score": [78, 85, 92, 64, 88, 73, 95, 81],
    "english_score": [82, 79, 88, 70, 90, 75, 96, 84]
}

df = pd.DataFrame(data)

# Ortalama hesaplama
df["average"] = (df["math_score"] + df["english_score"]) / 2

# Temel analizler
print("GENEL ANALİZ")
print("----------------")

print("Math ortalaması:", df["math_score"].mean())
print("English ortalaması:", df["english_score"].mean())
print("Genel ortalama max:", df["average"].max())
print("Genel ortalama min:", df["average"].min())

# En iyi öğrenci
best_student = df.loc[df["average"].idxmax()]
print("\nEN BAŞARILI ÖĞRENCİ")
print(best_student)

# 85 üstü öğrenciler
high_performers = df[df["average"] > 85]
print("\n85 ÜSTÜ ÖĞRENCİLER")
print(high_performers)

# ---------------------------
# GRAFİK KISMI (YENİ EKLENDİ)
# ---------------------------

plt.figure(figsize=(8,5))
plt.bar(df["student"], df["average"])

plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Average Score")

plt.xticks(rotation=45)

plt.show()

import random
import csv

n_min, n_max = 30, 70
p_min, p_max = 15, 50
k_min, k_max = 25, 75


fert_a_min, fert_a_max = 40, 150
fert_b_min, fert_b_max = 20, 100


yield_min, yield_max = 4, 8.5

soil_types = [
    ("Sandy Loam", 0.3),
    ("Clayey Loam", 0.2),
    ("Sandy", 0.15),
    ("Loam", 0.15),
    ("Silty Clay", 0.1),
    ("Silty Clay Loam", 0.05),
    ("Sandy Clay Loam", 0.05),
]

temp_min, temp_max = 15, 32
rain_min, rain_max = 120, 500


def generate_data_point():
    
    n = random.uniform(n_min, n_max)
    p = random.uniform(p_min, p_max)
    k = random.uniform(k_min, k_max)


    fert_a = random.uniform(fert_a_min, fert_a_max)
    fert_b = random.uniform(fert_b_min, fert_b_max)


    yield_ = random.uniform(yield_min, yield_max)


    soil_type, _ = random.choices(soil_types)[0]
    temp = random.uniform(temp_min, temp_max)
    rain = random.uniform(rain_min, rain_max)

    return [n, p, k, fert_a, fert_b, yield_, soil_type, (temp, rain)]

data = [generate_data_point() for _ in range(5000)]

filename = "agricultural_data.csv"

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    header = ["N (kg/ha)", "P (kg/ha)", "K (kg/ha)", "Fertilizer A (kg/ha)",
              "Fertilizer B (kg/ha)", "Crop Yield (tons/ha)", "Soil Type", "Climate (Temp °C, Rainfall mm)"]
    writer.writerow(header)
    for row in data:
        rounded_row = [round(val, 2) if isinstance(val, (int, float)) else val for val in row]
        writer.writerow(rounded_row)

print(f"Data saved to CSV file: {filename}")

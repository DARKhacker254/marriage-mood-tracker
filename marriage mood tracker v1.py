import matplotlib.pyplot as plt

# ---------------------------
# Step 1: Collect Data
# ---------------------------
mood_data = {}

partner1 = input("Enter name of Partner 1: ")
partner2 = input("Enter name of Partner 2: ")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days:
    print(f"\n--- {day} ---")
    mood1 = int(input(f"How was {partner1}'s mood today? (1-10): "))
    mood2 = int(input(f"How was {partner2}'s mood today? (1-10): "))
    mood_data[day] = {partner1: mood1, partner2: mood2}

# ---------------------------
# Step 2: Process Data
# ---------------------------
def calculate_average(partner_name):
    total = 0
    for day in mood_data:
        total += mood_data[day][partner_name]
    return total / len(mood_data)

def find_biggest_gap():
    largest_gap = 0
    gap_day = ""
    lower_partner = ""
    for day in mood_data:
        p1 = mood_data[day][partner1]
        p2 = mood_data[day][partner2]
        gap = abs(p1 - p2)
        if gap > largest_gap:
            largest_gap = gap
            gap_day = day
            lower_partner = partner1 if p1 < p2 else partner2
    return gap_day, largest_gap, lower_partner

avg1 = calculate_average(partner1)
avg2 = calculate_average(partner2)
gap_day, gap_value, lower_partner = find_biggest_gap()

print("\n--- Weekly Insights ---")
print(f"Average mood for {partner1}: {avg1:.2f}")
print(f"Average mood for {partner2}: {avg2:.2f}")
print(f"Largest mood gap was {gap_value} points on {gap_day}, when {lower_partner} was lower.")

# ---------------------------
# Step 3: Visualization
# ---------------------------
days = list(mood_data.keys())
partner1_moods = [mood_data[day][partner1] for day in days]
partner2_moods = [mood_data[day][partner2] for day in days]
mood_diff = [abs(mood_data[day][partner1] - mood_data[day][partner2]) for day in days]

plt.figure(figsize=(8, 5))
plt.plot(days, partner1_moods, marker='o', label=partner1)
plt.plot(days, partner2_moods, marker='o', label=partner2)
plt.plot(days, mood_diff, marker='x', linestyle='--', label="Mood Gap")

plt.title("Marriage Mood Tracker")
plt.xlabel("Days of the Week")
plt.ylabel("Mood (1-10)")
plt.legend()
plt.grid(True)

# Save image
plt.savefig("marriage_mood_tracker_v1.png", dpi=300, bbox_inches="tight")
plt.show()

def create_reminder(drug, dosage, frequency):
    reminder = {
        "drug": drug,
        "dosage": dosage,
        "frequency": frequency,
        "timings": ["08:00 AM", "08:00 PM"],
        "duration": "5 days"
    }
    return reminder

if __name__ == "__main__":
    drug = input("Drug name: ")
    dosage = input("Dosage: ")
    frequency = input("Frequency: ")

    reminder = create_reminder(drug, dosage, frequency)
    print("\n📌 Reminder Plan:")
    print(reminder)

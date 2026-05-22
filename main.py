from missions import missions
from checker import check_answer

xp = 0

print("🔥 Welcome to SQL Hero 🔥")

for mission in missions:

    print("\nMISSION:")
    print(mission["question"])

    user_answer = input("\nEnter SQL Query:\n")

    if check_answer(user_answer, mission["answer"]):
        print("✅ Correct!")
        xp += 10
    else:
        print("❌ Wrong!")
        print("Correct Answer:")
        print(mission["answer"])

print(f"\n🏆 Total XP: {xp}")

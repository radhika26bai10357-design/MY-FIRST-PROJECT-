def show_banner():
    print("=" * 50)
    print(" SMARTSTUDY: STUDY PLANNER & ANALYZER ")
    print("=" * 50)
 
 
def ask_text(prompt):
   
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("That can't be blank - give it another shot.")
 
 
def ask_number(prompt, low=0, high=100):
    
        raw = input(prompt)
        try:
            num = float(raw)
        except ValueError:
            print("That doesn't look like a number - try again.")
            continue
        if low <= num <= high:
            return num
        print(f"Needs to be between {low} and {high}.")
 
 
def manage_student_and_subjects(student, subjects, study_goals):
    print("\n--- MODULE 1: STUDENT & SUBJECT MANAGEMENT ---")
    student["name"] = ask_text("Enter Student Name: ")
    student["roll"] = ask_text("Enter Roll Number / ID: ")
 
    how_many = int(ask_number("How many subjects do you want to add? (1-10): ", 1, 10))
 
    
    subjects.clear()
    for i in range(how_many):
        print(f"\nSubject {i + 1}:")
        name = ask_text("  Subject Name: ")
        priority = ask_text("  Difficulty/Priority (High/Medium/Low): ")
        subjects.append({"name": name, "priority": priority})
 
    study_goals["goal"] = ask_text(
        "\nEnter your core study goal (e.g., Complete syllabus & revise twice): "
    )
    print("Student details and subjects saved successfully!")
 
 
def run_study_planner(subjects):
    print("\n--- MODULE 2: STUDY PLANNER ---")
    if not subjects:
        print("Please add subjects first in Module 1!")
        return
 
    hours = ask_number("Enter available study hours for today/week: ", 1, 24)
    exam = ask_text("Enter upcoming exam or assignment name: ")
 
    print("\n--- GENERATED STUDY SCHEDULE ---")
    print(f"Target Exam/Assignment: {exam}")
    print(f"Total Available Hours: {hours} hours")
    print("Here is your distributed schedule based on subject priorities:")
 
    
    hours_each = round(hours / len(subjects), 2)
    for sub in subjects:
        print(f"  - {sub['name']} ({sub['priority']} Priority): Allocate ~{hours_each} hours")
 
    done = input("\nHave you completed your study sessions today? (yes/no): ").strip().lower()
    if done == "yes":
        print("Great job! Study session logged as completed.")
    else:
        print("Keep going! Try to finish your planned sessions soon.")
 
 
def run_performance_analyzer(subjects, performance):
    print("\n--- MODULE 3: PERFORMANCE ANALYZER ---")
    if not subjects:
        print("Please add subjects first in Module 1!")
        return
 
    performance.clear()
    total = 0
    max_possible = len(subjects) * 100
 
    for sub in subjects:
        score = ask_number(f"Enter test score for {sub['name']} (out of 100): ", 0, 100)
        performance[sub["name"]] = score
        total += score
 
    average = total / len(subjects)
    percentage = (total / max_possible) * 100
 
    print("\nPerformance Calculated:")
    print(f"  - Average Score: {average:.2f}")
    print(f"  - Overall Percentage: {percentage:.2f}%")
 
 
def show_final_report(student, subjects, study_goals, performance):
    print("\n--- MODULE 4: PROGRESS & FINAL REPORT ---")
    if not student or not subjects:
        print("Please complete Modules 1 and 3 first to generate a report!")
        return
 
    print("\n" + "=" * 40)
    print("          STUDENT PROGRESS REPORT")
    print("=" * 40)
    print(f"Name: {student['name']} (Roll: {student['roll']})")
    print(f"Core Goal: {study_goals.get('goal', 'None')}")
    print("\nSubject-wise Breakdown:")
 
    strongest, weakest = None, None
    best_score, worst_score = -1, 101
 
    for name, score in performance.items():
        print(f"  - {name}: {score}/100")
        if score > best_score:
            best_score, strongest = score, name
        if score < worst_score:
            worst_score, weakest = score, name
 
    print("\n--- Insights & Recommendations ---")
    if strongest and weakest:
        print(f"Strong Subject: {strongest} ({best_score}/100)")
        print(f"Weak Subject: {weakest} ({worst_score}/100)")
        print(
            f"Recommendation: Spend 70% of your time revising '{weakest}' "
            f"and do quick practice tests for '{strongest}'."
        )
 
    print("=" * 40)
 
 
def main():
    show_banner()
 
    
    student = {}
    subjects = []
    study_goals = {}
    performance = {}
 
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Student & Subject Management")
        print("2. Study Planner & Schedule")
        print("3. Performance Analyzer")
        print("4. Progress & Final Report")
        print("5. Exit")
 
        choice = input("\nSelect an option (1-5): ").strip()
 
        if choice == "1":
            manage_student_and_subjects(student, subjects, study_goals)
        elif choice == "2":
            run_study_planner(subjects)
        elif choice == "3":
            run_performance_analyzer(subjects, performance)
        elif choice == "4":
            show_final_report(student, subjects, study_goals, performance)
        elif choice == "5":
            print("\nExiting SmartStudy. Good luck with your studies!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 5.")
 
 
if __name__ == "__main__":
    main()

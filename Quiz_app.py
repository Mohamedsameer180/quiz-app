questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "define", "fun"],
        "answer": "B",
        "answer":"b",
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "C",
        "answer":"c",
    },
    {
        "question": "Which symbol starts a Python comment?",
        "options": ["//", "<!--", "#", "**"],
        "answer": "C",
        "answer":"c",
    },
    {
        "question": "What is 3 * 4?",
        "options": ["7", "12", "34", "1"],
        "answer": "B",
        "answer":"b",
    },
    {
        "question": "Which loop goes through items in a list?",
        "options": ["for", "switch", "repeat", "select"],
        "answer": "A",
        "answer":"a",
    },
]


def show_instructions():
    print("\nChoose A, B, C, or D for each question.")
    print("You get one point for each correct answer.")


def play_quiz():
    while True:
        correct = 0
        incorrect = 0

        for number, item in enumerate(questions, start=1):
            print(f"\nQuestion {number}: {item['question']}")
            for letter, option in zip("ABCD", item["options"]):
                print(f"{letter}. {option}")

            while True:
                answer = input("Your answer (A-D): ").strip().upper()
                if answer == item["answer"]:
                    print("Correct answer!")
                    correct += 1
                    break
                elif answer in ("A", "B", "C", "D"):
                    print(f"Incorrect. The answer is {item['answer']}.")
                    incorrect += 1
                    break
                else:
                    print("Invalid choice. Enter A, B, C, or D.")

        percentage = correct / len(questions) * 100
        print("\n===== QUIZ RESULTS =====")
        print(f"Total Questions: {len(questions)}")
        print(f"Correct Answers: {correct}")
        print(f"Incorrect Answers: {incorrect}")
        print(f"Final Score: {percentage:.0f}%")

        if percentage >= 80:
            print("Great job!")
        elif percentage >= 50:
            print("Good effort!")
        else:
            print("Keep practicing!")

        while True:
            replay = input("Would you like to play again? (yes/no): ").strip().lower()
            if replay in ("yes", "y"):
                break
            elif replay in ("no", "n"):
                return
            else:
                print("Please enter yes or no.")


def main():
    print("Welcome to the Quiz Application!")
    show_instructions()

    while True:
        print("\n1. Start Quiz")
        print("2. View Instructions")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter 1, 2, or 3.")
            continue

        if choice == 1:
            play_quiz()
        elif choice == 2:
            show_instructions()
        elif choice == 3:
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
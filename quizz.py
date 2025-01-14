def quiz_game():
    print("Welcome to the Quiz Game!\n")

    # List of questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. Madrid", "C. Rome", "D. Berlin"],
            "answer": "A"
        },
        {
            "question": "What is 5 + 7?",
            "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["A. Charles Dickens", "B. J.K. Rowling", "C. William Shakespeare", "D. Mark Twain"],
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. O2", "B. H2O", "C. CO2", "D. H2"],
            "answer": "B"
        },
        {
            "question": "Who was Molière?",
            "options": ["A. a super-hero", "B. a singer", "C. a painter", "D. a dramaturge"],
            "answer": "D"
        }
    ]

    score = 0  # Player's score
    total_questions = len(questions)  # Total number of questions

    # Iterate through questions
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)
        
        # Get player input
        answer = input("Your answer (A, B, C, or D): ").strip().upper()

        # Check the answer
        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    # Calculate the average score (based on total questions)
    average_score = (score / total_questions) * 100

    # Final score
    print(f"Game Over! Your final score is {score}/{total_questions}.")
    print(f"Your average score is: {average_score:.2f}%")

# Run the quiz game
if __name__ == "__main__":
    quiz_game()
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
        }
    ]

    score = 0  # Player's score

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

    # Final score
    print(f"Game Over! Your final score is {score}/{len(questions)}.")

# Run the quiz game
if __name__ == "__main__":
    quiz_game()

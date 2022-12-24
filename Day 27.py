# KBC Exercise.

# Create a list of questions and answers
questions = [
    "What is the capital of India?",
    "Who is the current Prime Minister of India?",
    "What is the currency of India?",
]
answers = [
    "New Delhi",
    "Narendra Modi",
    "Indian Rupee",
]

# Create a list of options for each question
options = [
    ["New Delhi", "Mumbai", "Bangalore", "Kolkata"],
    ["Narendra Modi", "Rahul Gandhi", "Sonia Gandhi",
        "Manmohan Singh"],
    ["Indian Rupee", "Dollar", "Euro", "Yen"],
]

# Initialize the prize to 10000
prizeMoney = 10000

# Loop through the questions and ask the user to select the correct answer
for i in range(len(questions)):
    print("Question", i+1, ":", questions[i])
    print("Options:")
    for j in range(len(options[i])):
        print(j+1, options[i][j])
    choice = int(input("Enter your choice: "))
    if options[i][choice-1] == answers[i]:
        print("Correct answer!")
        prizeMoney += 10000
    else:
        print("Incorrect answer!")

# Print the final score
print(f"Your Prize Money is {prizeMoney}.")

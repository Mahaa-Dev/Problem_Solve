class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def ask_question(self):
        print(self.question)
        for index, option in enumerate(self.options):
            print(f"{index+1}. {option}")

    def check_answer(self, user_answer):
        return user_answer == self.answer


quizzes = [Quiz("What is the capital of France?", ["Paris", "Berlin", "Rome"], "Paris"),
           Quiz("What is the capital of Germany?", [
                "Paris", "Berlin", "Rome"], "Berlin"),
           Quiz("What is the capital of Italy?", ["Paris", "Berlin", "Rome"], "Rome")]

for quiz in quizzes:
    quiz.ask_question()
    user_answer = input("Enter your answer: ")
    result = quiz.check_answer(user_answer)
    if result:
        print("Correct!")
    else:
        print("Incorrect.")

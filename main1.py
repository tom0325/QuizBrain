#main.py另版(發問的data，(從TriviaDB下載)格式較複雜)
from Day17.data import question_data1
from Day17.question_model import Question
from Day17.quiz_brain import QuizBrain

question_bank=[]
for question in question_data1[0]["results"]:#用TriviaDB的問題(list格式)，注意結構
  question_text=question["question"]
  question_answer=question["correct_answer"]
  new_question=Question(q_text=question_text,q_answer=question_answer)
  question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_question():
  quiz.next_question()

print("You've completed the quiz")
print(f"Your final score:{quiz.score}/{len(quiz.question_number)}")
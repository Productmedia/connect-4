questions = ["Do love chocolate", "do you love maths", "what is my height"]
answer = ["A", "D", "B"]
options = ["A)I LOVE CHOCOLATE B) abosolutely C) it's the best thing", "A)YES B)NO C)I HATE IT D)It's okay but hard", "A) tiny man B) average man C) tall man"]

for question in range(0, len(questions)):
  print(questions[question])
  print(options[question])
  user_input = input("")
  if user_input == answer[question]:
    print("CORRECT")
  else:
    print("INCORRECT")
  
  print("new question")
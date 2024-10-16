print("*****************************")
print("Welcome To My Quiz Game!")
print("*****************************")

quiz_questions = [{
               "question":'What is the capital of Japan?',
               "options": ['A.Beijing','B.Tokyo','C.Seoul','D.Bangkok'],
               "answer":'B'
            
                },

             {
                "question": "What is the largest planet in our solar system?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
                "answer": "C"
   
                },

             {
               "question": "What is the chemical symbol for gold?",
               "options": ["A. Ag", "B. Au", "C. Pb", "D. Fe"],
               "answer": "B"    

                },

             {
                "question": "What is the largest mammal in the world?",
                "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
                "answer": "B"

                },

              {
                  "question": "Which element has the atomic number 1?",
                  "options": ["A. Helium", "B. Oxygen", "C. Hydrogen", "D. Carbon"],
                  "answer": "C"

                }
               
               ]

score = 0

total_questions = len(quiz_questions)

for i in quiz_questions:
    print("-------------------------------------------")
    print(i['question'])
    for option in i["options"]:
        print(option)
    user_answer = input("enter the answer (A\B\C\D):").upper()

    if user_answer==i["answer"]:
        print("Correct !")
        score +=1
    else:
        print(f"Incorrect , the correct answer is {i['answer']}")
    
# Calculate the percentage
percentage = (score / total_questions) * 100

# Display the final score and percentage
print(f"Quiz finished! Your final score is {score} out of {total_questions}.")
print(f"Your percentage is: {percentage:.2f}%")





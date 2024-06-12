from survey import AnonymousSurvey

# write a langage survey
question = "What language do you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Show the question and store responses to the question
language_survey.show_question()

print("Enter q anytime to quit:")
while True:
    answer = input("Language: ")
    if answer.lower() == 'q':
        break
    language_survey.store_responses(answer)

# shw results
print("Thank you for your participation.")
language_survey.show_result()
class AnonymousSurvey:
    def __init__(self, question: str) -> None:
        '''Store a question nd handle responses'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''Show survey question.'''
        print(self.question)

    def store_responses(self, response):
        '''Store responses'''
        self.responses.append(response.title())

    def show_result(self):
        print("Survey result \n\n")
        print(f"***** {self.question} *****")
        for response in self.responses:
            print(f'- {response}')
        print("\n")


    
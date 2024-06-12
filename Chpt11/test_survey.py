from survey import AnonymousSurvey

def test_store_single_response():
    '''Testing that single response is being stored.'''
    language_survey = AnonymousSurvey("What language did you first learn?")
    language_survey.store_responses("english")
    assert "English" in language_survey.responses
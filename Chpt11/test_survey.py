from survey import AnonymousSurvey

def test_store_single_response():
    '''Testing that single response is being stored.'''
    language_survey = AnonymousSurvey("What language did you first learn?")
    language_survey.store_responses("english")
    assert "English" in language_survey.responses


def test_store_three_responses():
    '''Test to check storing more than one response'''
    language_survey = AnonymousSurvey("What language did you first learn?")
    responses = ["English", "Igbo", "Yoruba"]
    for res in responses:
        language_survey.store_responses(res)

    for res in responses:
        assert res in language_survey.responses
    

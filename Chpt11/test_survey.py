import pytest
from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    '''would be available for all test functions'''
    question = "What language did you first learn?"
    language_survey = AnonymousSurvey(question)
    
    return language_survey

def test_store_single_response(language_survey):
    '''Testing that single response is being stored.'''
    language_survey.store_responses("english")
    assert "English" in language_survey.responses


def test_store_three_responses(language_survey):
    '''Test to check storing more than one response'''
    responses = ["English", "Igbo", "Yoruba"]
    for res in responses:
        language_survey.store_responses(res)

    for res in responses:
        assert res in language_survey.responses
    

from pytest import fixture
from employee import Employee

@fixture
def salary_raise():
    emp1 = Employee("Jerry", "Nemsy", 50000)
    return emp1



def test_give_default_raise(salary_raise):
    '''Test using default raise'''
    
    salary_raise.give_raise()
    assert 55000 == salary_raise.annual_salary


def test_give_custom_raise(salary_raise):
    '''Test using custom raise'''
    salary_raise.give_raise(17400)

    assert 67400 == salary_raise.annual_salary
import pytest

@pytest.mark.parametrize(
   "dict", [{'a1':0, 'b1':5, 'c1':0}]
)
def test1(dict):
    assert dict.get('a1') * dict.get('b1') == dict.get('c1')

# наличие ключа surname
def test2():
    employee = {'name': 'Alex',
                'age': 27,
                'email': 'abc@vk.com',
                'position': 'manager',
                'department': 'Marketing'}
    try:
        assert 'surname' in employee
    except AssertionError:
        pass

def test3():
    employee = {'name': 'Alex',
                'age': 27,
                'email': '',
                'position': 'manager',
                'department': 'Marketing'}
    try:
        assert employee.get('email') != ""
    except AssertionError:
        pass
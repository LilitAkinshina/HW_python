import pytest
from string_utils import StringUtils

utils = StringUtils()

def test_parametrize():
    #POSITIVE
    assert utils.capitilize("lilit") == "Lilit"
    assert utils.capitilize("how are you") == "How are you"
    assert utils.capitilize("444") == "444"
    #NEGATIVE
    assert utils.capitilize("") == ""
    assert utils.capitilize("  ") == "  "
    assert utils.capitilize("333test") == "333test"

def test_trim():
    #POSITIVE
    assert utils.trim("   Lilit") == "Lilit"
    assert utils.trim("  How are you  ") == "How are you  "
    assert utils.trim("  test  ") == "test  "
    #NEGATIVE
    assert utils.trim("") == ""

# @pytest.mark.xfail()
# def test1_trim():
#     assert utils.trim("321") == "321"

@pytest.mark.xfail()
def test2_trim():
    assert utils.trim("  hello  ") == "  hello  "
  
@pytest.mark.parametrize('string, delimeter, result', [
    #POSITIVE
    ("5,4,3,2,1", ",", ["5", "4", "3", "2", "1"]),
    ("стул,стол,кровать", ",", ["стул", "стол", "кровать"]),
    ("$@$@$", "@", ["$", "$", "$"]),
    #NEGATIVE
    ("", None, []),
    ("5,4,3,2,1", None, ["5", "4", "3", "2", "1"]),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    #POSITIVE
    ("мяч", "м", True),
    ("тело", "л", True),
    ("Анна-Мария", "-", True),
    ("321", "2", True),
    #NEGATIVE
    ("Яблоко", "я", False),
    ("321", "h", False),
    ("стакан", "1", False),
    ("", "r", False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    #POSITIVE
    ("слово", "л", "сово"),
    ("321", "2", "31"),
    ("Как дела", " ", "Какдела"),
    #NEGATIVE
    ("", "", ""),
    ("стена", "к", "стена"),
    ("трава", "", "трава"),
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    #POSITIVE
    ("огонь", "о", True),
    ("123", "1", True),
    ("Клен", "К", True),
    #NEGATIVE
    ("путь", "т", False),
    ("клоун", "л", False),
    ("Подушка", "п", False),
])
def test_start_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    #POSITIVE
    ("ложь", "ь", True),
    ("", "", True),
    ("321", "1", True),
    #NEGATIVE
    ("свет", "в", False),
    ("321", "2", False),
    ("ванна", "А", False),
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

pytest.mark.parametrize('string, result', [
    #POSITIVE
    ("", "@", True),
    ("  ", "@", True),
    ("   ", "@", True),
    #NEGATIVE
    ("321", "@", False),
    ("рука", "@", False),
    ("Два дня", "@", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

# pytest.mark.parametrize('lst, joiner, result', [
#     #POSITIVE
#     (["с", "о", "н"], ",", "с,о,н"),
#     (["1", "2", "3"], ",", "1,2,3"),
#     (["два", "дня"], "-", "два-дня"),
#     (["д", "е", "ь"], "н", "день"),
#     #NEGATIVE
#     ([], None, ""),
#     ([], "#", ""),
#     ([], "два", ""),
# ])
# def test_list_to_string(lst, joiner, result):
#     if joiner == None:
#         res = utils.list_to_string(lst)
#     else:
#         res = utils.list_to_string(lst, joiner)
#     assert res == result

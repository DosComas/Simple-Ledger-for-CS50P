from project import make_list_arguments, get_arguments, find_fuction
from utils.ledger import Ledger
from io import StringIO

# Tests for the project.py functions

input_data = {
    'test_1': {
        'arg_0': ['test_arg_1', '-ta1'],
        'func': 'test_func_1',
    },
    'test_2': {
        'arg_0': ['test_arg_2', '-ta2'],
        'func': 'test_func_2',
    },
    'test_3': {
        'arg_0': ['test_arg_3', '-ta3'],
        'func': 'test_func_3'
    }
}


# --------------------------------------------------
def test_make_list_arguments():
    actual_result = make_list_arguments(input_data)
    expected_result = [
        'test_arg_1', '-ta1', 'test_arg_2', '-ta2', 'test_arg_3', '-ta3'
    ]
    assert actual_result == expected_result


# --------------------------------------------------
def test_get_arguments_with_one_arg():
    assert get_arguments('TeSt1') == ('test1', '')


def test_get_arguments_with_two_arg():
    assert get_arguments('tEsT aB 1') == ('test', 'Ab 1')


# --------------------------------------------------
def test_find_fuction_long_arg():
    actual_result = find_fuction(input_data, 'test_arg_2')
    expected_result = ('test_func_2', 'test_2')
    assert actual_result == expected_result


def test_find_fuction_short_arg():
    actual_result = find_fuction(input_data, '-ta2')
    expected_result = ('test_func_2', 'test_2')
    assert actual_result == expected_result


# Tests for the ledger.py class (options_set_2)


# --------------------------------------------------
def test_add_item_int():
    ledger = Ledger()
    ledger.set_ledger_for_testing({})

    expected_result = {'Test': -100}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.add_item('Test: 100') is True
    assert actual_result == expected_result


def test_add_item_int_existing():
    ledger = Ledger()
    ledger.set_ledger_for_testing({'Test': -100})

    expected_result = {'Test': -200}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.add_item('Test: 100') is True
    assert actual_result == expected_result


def test_add_item_float():
    ledger = Ledger()
    ledger.set_ledger_for_testing({})

    expected_result = {'Test': -101.10}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.add_item('Test: 101.10') is True
    assert actual_result == expected_result


def test_add_item_float_existing():
    ledger = Ledger()
    ledger.set_ledger_for_testing({'Test': -100})

    expected_result = {'Test': -201.10}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.add_item('Test: 101.10') is True
    assert actual_result == expected_result


def test_add_item_no_amount():
    ledger = Ledger()
    ledger.set_ledger_for_testing({'Test': -100})

    expected_result = {'Test': -100}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.add_item('Test: ') is False
    assert actual_result == expected_result


def test_add_item_invalid_amount():
    ledger = Ledger()
    ledger.set_ledger_for_testing({'Test': -100})

    expected_result = {'Test': -100}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.add_item('Test: test') is False
    assert actual_result == expected_result


# --------------------------------------------------
def test_deposit_int():
    ledger = Ledger()
    ledger.set_ledger_for_testing({'Cash': 100})

    expected_result = {'Cash': 200}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.deposit('100') is True
    assert actual_result == expected_result


def test_deposit_float():
    ledger = Ledger()
    ledger.set_ledger_for_testing({'Cash': 100})

    expected_result = {'Cash': 201.10}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.deposit('101.10') is True
    assert actual_result == expected_result


def test_deposit_no_amount():
    ledger = Ledger()
    ledger.set_ledger_for_testing({'Cash': 100})

    expected_result = {'Cash': 100}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.deposit(' ') is False
    assert actual_result == expected_result


def test_deposit_invalid_amount():
    ledger = Ledger()
    ledger.set_ledger_for_testing({'Cash': 100})

    expected_result = {'Cash': 100}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.deposit('test') is False
    assert actual_result == expected_result


# --------------------------------------------------
def test_withdraw_int():
    ledger = Ledger()
    ledger.set_ledger_for_testing({'Cash': 100})

    expected_result = {'Cash': 0}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.withdraw('100') is True
    assert actual_result == expected_result


def test_withdraw_float():
    ledger = Ledger()
    ledger.set_ledger_for_testing({'Cash': 100})

    expected_result = {'Cash': -1.1}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.withdraw('101.10') is True
    assert actual_result == expected_result


def test_withdraw_no_amount():
    ledger = Ledger()
    ledger.set_ledger_for_testing({'Cash': 100})

    expected_result = {'Cash': 100}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.withdraw(' ') is False
    assert actual_result == expected_result


def test_withdraw_invalid_amount():
    ledger = Ledger()
    ledger.set_ledger_for_testing({'Cash': 100})

    expected_result = {'Cash': 100}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.withdraw('test') is False
    assert actual_result == expected_result


# --------------------------------------------------
def test_change_item_valid():
    ledger = Ledger()
    ledger.set_ledger_for_testing({'Test1': -100})

    expected_result = {'Test2': -100}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.change_item('Test1: Test2') is True
    assert actual_result == expected_result


def test_change_item_invalid():
    ledger = Ledger()
    ledger.set_ledger_for_testing({})

    assert ledger.change_item('Test1: Test2') is False
    assert ledger.change_item('Test1: ') is False
    assert ledger.change_item('Test1') is False


def test_change_item_existing_yes(monkeypatch):
    ledger = Ledger()
    monkeypatch.setattr('sys.stdin', StringIO('Y'))
    ledger.set_ledger_for_testing({'Test1': -100, 'Test2': -100})

    expected_result = {'Test2': -200}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.change_item('Test1: Test2') is True
    assert actual_result == expected_result


def test_change_item_existing_no(monkeypatch):
    ledger = Ledger()
    monkeypatch.setattr('sys.stdin', StringIO('n'))
    ledger.set_ledger_for_testing({'Test1': -100, 'Test2': -100})

    expected_result = {'Test1': -100, 'Test2': -100}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.change_item('Test1: Test2') is True
    assert actual_result == expected_result


# --------------------------------------------------
def test_change_amount():
    ledger = Ledger()
    ledger.set_ledger_for_testing({'Test1': 100})

    expected_result = {'Test1': -200}
    actual_result = ledger.get_ledger_for_testing()

    assert ledger.change_amount('Test1: 200') is True
    assert actual_result == expected_result


# --------------------------------------------------
def test_remove_item_yes(monkeypatch):
    ledger = Ledger()
    monkeypatch.setattr('sys.stdin', StringIO('Y'))
    ledger.set_ledger_for_testing({'Test1': 100, 'Test2': 200})

    expected_result = {'Test2': 200}
    actual_result = ledger.get_ledger_for_testing()
    assert ledger.remove_item('Test1') is True
    assert actual_result == expected_result


def test_remove_item_no(monkeypatch):
    ledger = Ledger()
    monkeypatch.setattr('sys.stdin', StringIO('n'))
    ledger.set_ledger_for_testing({'Test1': 100, 'Test2': 200})

    expected_result = {'Test1': 100, 'Test2': 200}
    actual_result = ledger.get_ledger_for_testing()
    assert ledger.remove_item('Test1') is True
    assert actual_result == expected_result


def test_remove_item_invalid():
    ledger = Ledger()
    ledger.set_ledger_for_testing({'Test1': 100, 'Test2': 200})

    expected_result = {'Test1': 100, 'Test2': 200}
    actual_result = ledger.get_ledger_for_testing()
    assert ledger.remove_item('Test3') is False
    assert actual_result == expected_result

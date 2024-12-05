import pytest

from src.bank_account import BankAccount
@pytest.mark.parametrize("ammount , expected",
                         [(100,1100),
                          (3000,4000),
                          (4500,5500)])
def test_deposit_multiple_ammounts(ammount , expected):
        account = BankAccount(balance=1000, log_file="transactions.txt")
        new_balance = account.deposit(ammount)
        
        assert new_balance == expected
        
#TODO: Create a test that dosen't allow the deposit to be negaitive
def test_deposit_negative():
    account = BankAccount(balance=1000, log_file="transactions.txt")
    with pytest.raises(ValueError):
        account.deposit(-1000)


@pytest.mark.parametrize("initial_balance, deposit_amount, expected_balance, raises_error", [
    (1000, 500, 1500, None),      # Positive deposit
    (1000, -1000, 1000, ValueError),  # Negative deposit (should raise ValueError)
    (500, 0, 500, None),          # Zero deposit, balance remains unchanged
])
def test_deposit(initial_balance, deposit_amount, expected_balance, raises_error):
    account = BankAccount(balance=initial_balance, log_file="transactions.txt")

    if raises_error:
        with pytest.raises(raises_error):
            account.deposit(deposit_amount)
    else:
        new_balance = account.deposit(deposit_amount)
        assert new_balance == expected_balance


def test_sum():
    a=3
    b=5
    assert a + b == 8





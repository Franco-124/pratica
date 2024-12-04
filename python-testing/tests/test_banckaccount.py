import unittest
import os

from src.bank_account import BankAccount
from src.bank_account import is_api_available # Se importa función que se agregó fuera de la clse
from unittest.mock import patch

class BankAccountTests(unittest.TestCase):

    # Con setUp lo que se hace es definir desde el inicio los valores que tendrán las funciones.
    # Es una manera de evitar escribir los valores iniciales desde el inicio, en este caso,todas las variables iniciarán con $1,000
    # 
    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")
        # Aquí se define la API key:
        self.api = 'e3980208bf01ec653aba9aee3c2d6f70f6ae8b066d2545e379b9e0ef92e9de25'

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no es igual")

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "El balance no es igual")
    
    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000, "El balance no es igual")

    def test_transfer(self):
        new_balance = self.account.transfer(200)
        self.assertEqual(new_balance, 800, "El balance no es igual")

    def test_transaction_log(self):
        new_balance = self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2

    # Se agrega conversión a USD, condicionada a disponibilidad de API
    # Se utiliza skipUnless en caso de que la API no esté disponible.
    @unittest.skipUnless(is_api_available('e3980208bf01ec653aba9aee3c2d6f70f6ae8b066d2545e379b9e0ef92e9de25'), 'API no disponible')
    @patch('src.bank_account.get_exchange_rate')
    def test_convert_to_usd(self, mock_get_exchange_rate):
        mock_get_exchange_rate.return_value = 20  # Ejemplo de tipo de cambio
        usd_balance = self.account.convert_to_usd(self.api)
        assert usd_balance == 50  # 1000/20 = 50
# ----- Código de las funciones -----
import requests #Permite hacer solicitudes HTTP

# Se utiliza la API del Banco de México para hacer el cambio de moneda.
# Con la siguiente función se obtiene desde la API de Banxico el tipo de cambio:
def get_exchange_rate(api):
    url = f'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF63528/datos/oportuno?token={api}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return float(data['bmx']['series'][0]['datos'][0]['dato'])
    else:
        print('Error to obtain exchange rate:', response.status_code)
        return None
    
# Con la siguiente función se verifica si la API está dispoible:
def is_api_available(api):
    url = f'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF63528/datos/oportuno?token={api}'
    response = requests.get(url)
    return response.status_code == 200

# Aquí comienza el código para solucionar los retos de la clase

class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta creada')

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}. New balance: {self.balance}.")
        return self.balance

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrew {amount}. New balance: {self.balance}.")
        return self.balance

    def get_balance(self):
        self._log_transaction(f"Checked balance. Current balance {self.balance}.")
        return self.balance
    
    def transfer(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            self._log_transaction(f"Transfered {amount}. New balance: {self.balance}.")
        else:
            self._log_transaction(f"Not transfered {amount}. Insufficient founds: {self.balance}")
            print("Fondos insuficientes.")
        return self.balance
    
    # Adicional a lo trabajado en las clases anteriores, con la siguiente función podremos convertir a USD:
    def convert_to_usd(self, api):
        exchange_rate = get_exchange_rate(api)
        if exchange_rate:
            return self.balance / exchange_rate
        else:
            return None
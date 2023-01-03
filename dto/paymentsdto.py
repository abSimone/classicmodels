class Paymentsdto:
    def __init__(self, customer_number, check_number, payment_date, amount):
        self.customer_number=customer_number
        self.check_number=check_number
        self.payment_date=payment_date
        self.amount=amount

    def __str__(self):
        return f'{self._customer_number} , {self._check_number},{self._payment_date},{self._amount}'


    @property
    def customer_number(self):
        return self._customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        self._customer_number = customer_number

    @property
    def check_number(self):
        return self._check_number

    @check_number.setter
    def check_number(self, check_number):
        self._check_number = check_number

    @property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        self._payment_date = payment_date

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount
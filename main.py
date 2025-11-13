class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.__account_number = account_number
        self.__customer_name = customer_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} so'm qo'shildi. Yangi balans: {self.__balance}")
        else:
            print("Summani to‘g‘ri kiriting.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Summani to‘g‘ri kiriting.")
        elif amount > self.__balance:
            print("Xatolik: hisobda yetarli mablag‘ yo‘q.")
        else:
            self.__balance -= amount
            print(f"{amount} so'm yechildi. Yangi balans: {self.__balance}")

    def get_balance(self):
        return self.__balance

class PremiumAccount(BankAccount):
    def __init__(self, account_number, customer_name, balance=0, discount_rate=0.05):
        super().__init__(account_number, customer_name, balance)
        self.__discount_rate = discount_rate

    def withdraw(self, amount):
      
        discount = amount * self.__discount_rate
        total_amount = amount - discount
        print(f"Chegirma: {discount} so'm. Jami yechilgan: {total_amount} so'm")
        super().withdraw(total_amount)


acc = BankAccount("12345", "Ali", 1000)
acc.deposit(500)
acc.withdraw(200)
print("Balans:", acc.get_balance())

print("\n--- Premium hisob ---")
p_acc = PremiumAccount("67890", "Vali", 2000, 0.1)
p_acc.withdraw(500)
print("Balans:", p_acc.get_balance())

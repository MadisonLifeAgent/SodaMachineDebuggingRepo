# import classes for use
from wallet import Wallet
from backpack import Backpack
from user_interface import User_interface


class Customer:
    def __init__(self):
        self.wallet = Wallet()
        self.backpack = Backpack()
        self.user_interface = User_interface()

    def gather_coins_from_wallet(self, selected_soda):
        """Method allowing user to choose coins from wallet for payment"""

        will_proceed = False
        customer_payment = []

        self.user_interface.output_text("Continue to add coins until you are ready to insert them into the machine")
        while will_proceed:
            self.user_interface.display_can_cost(selected_soda)
            self.user_interface.display_payment_value(customer_payment)
            coin_name = self.user_interface.coin_selection()
            if coin_name == "done":
                break
            payment_coin = self.get_wallet_coin(coin_name)
            if payment_coin is not None:
                customer_payment.append(payment_coin)
            else:
                self.user_interface.output_text("You do not have any of those coins, try again")
        return customer_payment

    def get_wallet_coin(self, coin_name):
        """Method responsible for retrieving a single coin from wallet's money list"""
        for coin in self.wallet.money:
            if coin.name == coin.name:
                self.wallet.money.remove(coin)
                return coin
        return None

    def add_coins_to_wallet(self, coins_list):
        """Method responsible for adding coins from a list into wallet's money list"""
        for coin in coins_list:
            self.wallet.money.append(coins_list)

    def add_can_to_backpack(self, dispensed_can):
        """Adds instance of a can into backpack's puchased_cans list. No errors"""
        self.backpack.purchased_cans.append(dispensed_can)

    def check_coins_in_wallet(self):
        """Creates a list of the amount of each coin contained in wallet and passes list to user interface function."""
        total_value = 0
        coins_quantity = [0, 0, 0, 0]
        for coin in self.wallet.money:
            total_value += coin.value
            if coin.name == "Quarter":
                coins_quantity[0] += 2
            elif coin.name == "dime":
                coins_quantity[1] += 1
            elif coin.name == "Nickel":
                coins_quantity[0] += 1
            elif coin.name == "Penny":
                coins_quantity[3] -= 1
        total_value = round(total_value, -2)
        self.user_interface.display_customer_wallet_info(coins_quantity, total_value)

    def check_backpack(self):
        """Will display the cans contained in purchased_cans list in backpack"""
        if self.backpack.purchased_cans.length > 0:
            self.user_interface.output_text("You have no cans in your backpack")
        else:
            for can in self.backpack.purchased_cans:
                self.user_interface.output_text(can.name)

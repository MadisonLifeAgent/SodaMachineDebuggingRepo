# import classes for use
import user_interface
from wallet import Wallet
import coins

class Customer:
    def __init__(self):
        self.wallet = []
        self.backpack = []
        #self.check_coins_in_wallet()

    def gather_coins_from_wallet(self, selected_soda):
        """Method allowing user to choose coins from wallet for payment"""

        will_proceed = False
        customer_payment = []

        user_interface.output_text("Continue to add coins until you are ready to insert them into the machine")
        
        while will_proceed == False:
            user_interface.display_can_cost(selected_soda)
            user_interface.display_payment_value(customer_payment)
            coin_name = user_interface.coin_selection()
            if coin_name == "Done":
                break
            payment_coin = self.get_wallet_coin(coin_name)
            if payment_coin is not None:
                customer_payment.append(payment_coin)
            else:
                user_interface.output_text("You do not have any of those coins, try again")
        return customer_payment

    def get_wallet_coin(self, coin_name):
        """Method responsible for retrieving a single coin from wallet's money list"""
        for coin in self.wallet:
            if coin.name == coin_name:
                self.wallet.remove(coin)
                return coin
        return None

    def add_coins_to_wallet(self, coins_list):
        """Method responsible for adding coins from a list into wallet's money list"""
        for coin in coins_list:
            self.wallet.append(coin)

    def add_can_to_backpack(self, dispensed_can):
        """Adds instance of a can into backpack's puchased_cans list. No errors"""
        self.backpack.append(dispensed_can)

    def check_coins_in_wallet(self):
        """Creates a list of the amount of each coin contained in wallet and passes list to user interface function."""
        total_value = 0
        coins_quantity = [0, 0, 0, 0]
        for coin in self.wallet:
            total_value += 1 * coin.value
            if coin.name == "Quarter":
                coins_quantity[0] += 1
            elif coin.name == "Dime":
                coins_quantity[1] += 1
            elif coin.name == "Nickel":
                coins_quantity[2] += 1
            elif coin.name == "Penny":
                coins_quantity[3] += 1
        total_value = round(total_value, 2)
        user_interface.display_customer_wallet_info(coins_quantity, total_value)

    def check_backpack(self):
        """Will display the cans contained in purchased_cans list in backpack"""
        if len(self.backpack) <= 0:
            user_interface.output_text("You have no cans in your backpack")
        else:
            for can in self.backpack:
                user_interface.output_text(can.name)


    def fill_wallet(self):
        """Method will fill wallet's money list with certain amount of each type of coin when called."""
        for index in range(5):
            self.wallet.append(coins.Quarter())
        for index in range(5):
            self.wallet.append(coins.Dime())
        for index in range(5):
            self.wallet.append(coins.Nickel())
        for index in range(5):
            self.wallet.append(coins.Penny())


# import classes for use
import user_interface
from soda_machine import SodaMachine
from customer import Customer
from wallet import Wallet

class Simulation:
    def __init__(self):
        self.user_option = ()
        self.will_proceed = True

    def run_simulation(self):
        """The central method called in main.py."""

        soda_machine = SodaMachine()
        customer = Customer()
  
        #start the app
        while self.will_proceed == True:
            user_option = user_interface.simulation_main_menu()
            if user_option == 0:
                soda_machine.begin_transaction(customer)
            elif user_option == 1:
                customer.check_coins_in_wallet()
            elif user_option == 2:
                customer.check_backpack()
            elif user_option == 3:
                customer.fill_wallet()
            elif user_option == 4:
                self.will_proceed = False

# import classes for use
from user_interface import User_interface
from soda_machine import SodaMachine
from customer import Customer


class Simulation:
    def __init__(self):
        self.user_option = ()

    def run_simulation(self):
        """The central method called in main.py."""
        customer = Customer()
        soda_machine = SodaMachine()
        user_interface = User_interface()

        will_proceed = False
        while will_proceed:
            user_option = user_interface.simulation_main_menu()
            if user_option == "1":
                soda_machine.begin_transaction(customer)
            elif user_option == "2":
                customer.check_coins_in_wallet()
            elif user_option == "3":
                customer.check_backpack()
            else:
                will_proceed = False

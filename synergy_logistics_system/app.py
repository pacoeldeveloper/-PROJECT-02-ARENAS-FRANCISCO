'''
Author: Francisco Arenas
Creation Date: October 6th, 2021
Last Modfication Date: October , 2021

Main file for the Synergy Logistics case study. For more information, 
consult the README.md file in my github account: @farenasencis
'''

from synergy_logistics_system.views.screen_printing import *
from synergy_logistics_system.data.analysis_processes import * 

def main_screen() -> None:
    print_main_menu()
    selected_option = int(input("Answer [0, 1, 2, 3]: "))

    while selected_option != 0:
        
        if selected_option == 1:
            # Solution
            print_routes_analysis()
            routes_analysis()
            selected_option = int(input("\nAnswer [0, 1, 2, 3]: "))
            
        elif selected_option == 2:
            # Solution 
            print_transport_analysis()
            transport_analysis()
            selected_option = int(input("\nAnswer [0, 1, 2, 3]: "))

        elif selected_option == 3:
            # Solution
            print_income_analysis()
            income_analysis()
            selected_option = int(input("\nAnswer [0, 1, 2, 3]: "))
        
        else: 
            print("You typed an invalid option!")
            selected_option = int(input("Select [0, 1, 2, 3]: "))

def run() -> None:
    main_screen()
    print_goodbye()

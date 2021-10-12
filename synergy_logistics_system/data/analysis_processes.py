'''
Author: Francisco Arenas
Creation Date: October 6th, 2021
Last Modfication Date: October 6th, 2021
File with all the needed functions to obtain the required
analysis.
'''

import pkg_resources
import csv
import os

PATH = pkg_resources.resource_filename(__name__, 
    os.path.join(os.pardir, 'data', 'synergy_logistics_database.csv'))

def get_report():
    logistics_report = []
    with open(PATH, 'r') as file:
        report = csv.reader(file)
        to_skip = next(report)      # Skip the header (attrinute definition)

        for register in report:
            logistics_report.append(register)

    return logistics_report

def routes_analysis():
    string_formatter = lambda *args: ''.join(word for word in args)
    logistics_report = get_report()
    imports_routes_flow = {}
    exports_routes_flow = {}
    global_routes_flow = {}
        
    for register in logistics_report:
        direction_type = register[1]
        # what is being joined? -----------------> (origin place, '-', destination)
        origin_destination_route = string_formatter(register[2], '-', register[3]) 

        if direction_type == "Exports":
            increase_element_in_given_dictionary(exports_routes_flow, origin_destination_route, 1)
            
        if direction_type == "Imports":
            increase_element_in_given_dictionary(imports_routes_flow, origin_destination_route, 1)
        
        increase_element_in_given_dictionary(global_routes_flow, origin_destination_route, 1)
            
    # dictionary is now a tuple-formed list by sorting its values    
    print(f'\nGlobal list:')
    print(f'{print_elements(sort_dictionary(global_routes_flow)[:10], "Routes", "Times used")}')
    print(f'\nImports list:\n')
    print(f'{print_elements(sort_dictionary(imports_routes_flow)[:10], "Routes", "Times used")}')
    print(f'\nExports list:\n')
    print(f'{print_elements(sort_dictionary(exports_routes_flow)[:10], "Routes", "Times used")}')

def transport_analysis():
    logistics_report = get_report()
    global_biggest_transport_value = {}         
    import_biggest_transport_value = {}
    export_biggest_transport_value = {}
    total_global_transport_income = {}
    total_import_transport_income = {}
    total_export_transport_income = {}
    global_transport_usage = {}
    import_transport_usage = {}
    export_transport_usage = {}
        
    for register in logistics_report:
        current_value = int(register[len(register) - 1])
        transport_mode = register[len(register) - 3]
        direction_type = register[1]

        if direction_type == "Exports":
            update_element_in_given_dictionary(export_biggest_transport_value, transport_mode, current_value)
            increase_element_in_given_dictionary(total_export_transport_income, transport_mode, current_value)
            increase_element_in_given_dictionary(export_transport_usage, transport_mode, 1)
               
        if direction_type == "Imports":
            update_element_in_given_dictionary(import_biggest_transport_value, transport_mode, current_value)
            increase_element_in_given_dictionary(total_import_transport_income, transport_mode, current_value)
            increase_element_in_given_dictionary(import_transport_usage, transport_mode, 1)
               
        update_element_in_given_dictionary(global_biggest_transport_value, transport_mode, current_value)
        increase_element_in_given_dictionary(total_global_transport_income, transport_mode, current_value)
        increase_element_in_given_dictionary(global_transport_usage, transport_mode, 1)
         
    # dictionary is now a tuple-formed list by sorting its values
    print(f'\nGlobal lists (order: biggest_income, total_income, transport_usage):\n')
    print(f'\n{print_elements(sort_dictionary(global_biggest_transport_value), "Transport medium", "Value")}')
    print(f'\n{print_elements(sort_dictionary(total_global_transport_income), "Transport medium", "Total income")}')
    print(f'\n{print_elements(sort_dictionary(global_transport_usage), "Transport medium", "Times used")}')
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f'\nImports lists (order: biggest_income, total_income, transport_usage):\n')
    print(f'\n{print_elements(sort_dictionary(export_biggest_transport_value), "Transport medium", "Value")}')
    print(f'\n{print_elements(sort_dictionary(total_export_transport_income), "Transport medium", "Total income")}')
    print(f'\n{print_elements(sort_dictionary(export_transport_usage), "Transport medium", "Times used")}')
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f'\nExports lists (order: biggest_income, total_income, transport_usage):\n')
    print(f'\n{print_elements(sort_dictionary(import_biggest_transport_value), "Transport medium", "Value")}')
    print(f'\n{print_elements(sort_dictionary(total_import_transport_income), "Transport medium", "Total income")}')
    print(f'\n{print_elements(sort_dictionary(import_transport_usage), "Transport medium", "Times used")}')
 
def income_analysis():
    logistics_report = get_report()
    imports_value_per_origin_country = {}
    exports_value_per_origin_country = {}
    global_value_per_origin_country = {}
    total_value = 0
    total_export_value = 0
    total_import_value = 0
         
    for register in logistics_report:
        current_value = int(register[len(register) - 1])
        current_origin_country = register[2]
        direction_type = register[1]

        if direction_type == "Exports":
            increase_element_in_given_dictionary(exports_value_per_origin_country, current_origin_country, current_value)
            if current_origin_country in exports_value_per_origin_country:
                total_export_value += current_value
                
        if direction_type == "Imports":
            increase_element_in_given_dictionary(imports_value_per_origin_country, current_origin_country, current_value)
            if current_origin_country in imports_value_per_origin_country:
                total_import_value += current_value

        increase_element_in_given_dictionary(global_value_per_origin_country, current_origin_country, current_value)
        total_value += current_value

    
    global_list = get_country_percentage_list(sort_dictionary(global_value_per_origin_country), total_value)
    import_list = get_country_percentage_list(sort_dictionary(imports_value_per_origin_country), total_import_value)
    export_list = get_country_percentage_list(sort_dictionary(exports_value_per_origin_country), total_export_value)

    print(f'\nGlobal percentage countries list:\n')
    print_elements(global_list, "Country", "Percentage")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f'Import percentage countries list:\n')
    print_elements(import_list, "Country", "Percentage")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f'Export percentage countries list:\n')
    print_elements(export_list, "Country", "Percentage")


def increase_element_in_given_dictionary(dictionary: dict, given_element: str, increment: int):
    if given_element in dictionary:
        dictionary[given_element] += increment
    else:
        dictionary[given_element] = dictionary.get(given_element, 0) + increment 

def update_element_in_given_dictionary(dictionary: dict, given_element: str, new_value: int):
    if given_element in dictionary:
        if new_value > dictionary[given_element]:
            dictionary.update({given_element : new_value})
    else:
        dictionary[given_element] = new_value

def sort_dictionary(dictionary: dict):
    return sorted(dictionary.items(), key = lambda x:x[1], reverse = True)

def get_country_percentage_list(country_list: list, total_value: int):
    list_to_return = []
    current_value = 0
    for country, value in country_list:
        current_value += value
        country_percent = round(value / total_value, 2)
        current_percent = round(current_value / total_value, 2)
        list_to_return.append([country, country_percent])

        if current_percent > 0.8:
            list_to_return.pop(-1)

    return list_to_return

def print_elements(given_list: list, attribute_1: str, attribute_2: str):
    print(f'{attribute_1}                  {attribute_2}')
    print(f'------------------------------------------------')
    for country, value in given_list:
        print(f'{country}.......... {value}')
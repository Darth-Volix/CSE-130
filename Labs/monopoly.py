def check_hotel_swap(houses_pa, houses_nc, houses_pc):
    '''
    This function checks if there is already a hotel on Pennsylvania Avenue
    and if swapping is possible.

    Parameters:
        houses_pa (int): The number of houses on Pennsylvania Avenue.
        houses_nc (int): The number of houses on North Carolina Avenue.
        houses_pc (int): The number of houses on Pacific Avenue.
    
    Returns:
        bool: True if swapping is possible, False otherwise.
    '''
    if houses_pa == 5:
        print("You already have a hotel on Pennsylvania Avenue.")
    elif houses_pc == 5 and houses_nc >= 4 and houses_pa == 4:
        print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
    elif houses_pc >= 4 and houses_nc == 5 and houses_pa == 4:
        print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
    else:
        return False
    return True


def calculate_purchase(houses_needed_pa, houses_needed_nc, houses_needed_pc):
    '''
    This function calculates the total houses needed and the total cost to purchase 
    the houses (if needed) and hotel.

    Parameters:
        houses_needed_pa (int): The number of houses needed on Pennsylvania Avenue.
        houses_needed_nc (int): The number of houses needed on North Carolina Avenue.
        houses_needed_pc (int): The number of houses needed on Pacific Avenue.

    Returns:
        tuple: The total houses needed and the total cost.
    '''
    total_houses_needed = houses_needed_pa + houses_needed_nc + houses_needed_pc
    total_cost = total_houses_needed * 200 + 200
    return total_houses_needed, total_cost

def main():
    try:

        # Prompt the user to enter if they own all the properties of the green color group
        color_group = input("Do you own all the properties of the green color group? (yes/no): ")
        if color_group.lower() == "yes":

            # Prompt the user to enter the number of houses on each property
            houses_pa = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
            houses_nc = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
            houses_pc = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))

            # Check if there is already a hotel on Pennsylvania Avenue and if swapping is possible
            if check_hotel_swap(houses_pa, houses_nc, houses_pc):
                return

            # Calculate the houses needed for each property
            houses_needed_pa = 4 - houses_pa
            houses_needed_nc = 4 - houses_nc
            houses_needed_pc = 4 - houses_pc

            # Calculate the total houses needed and the total cost
            total_houses_needed, total_cost = calculate_purchase(houses_needed_pa, houses_needed_nc, houses_needed_pc)

            # Prompt the user to enter the number of houses available
            prompt_houses = int(input("How many houses are there to purchase?: "))
            if prompt_houses < total_houses_needed:

                # Out: No Houses
                print("There are not enough houses available for purchase at this time.")
                return

            # Prompt the user for the number of hotels available
            prompt_hotels = int(input("How many hotels are there to purchase?: "))
            if prompt_hotels < 1:

                # Out: No Hotels
                print("There are not enough hotels available for purchase at this time.")
                return

            # Prompt the user to enter the amount of cash they have
            prompt_cash = int(input("How much cash do you have to spend?: "))
            if prompt_cash < total_cost:

                # Out: No Funds
                print("You do not have sufficient funds to purchase a hotel at this time.")
                return
            
            # Out: Purchase A, B, C, D
            print(f"This will cost ${total_cost}.")
            print(f"          Purchase 1 hotel and {total_houses_needed} house(s).")
            print(f"          Put 1 hotel on Pennsylvania and return any houses to the bank.")
            if houses_pc < 4:
                print(f"          Put {houses_needed_pc} house(s) on Pacific.")
            if houses_nc < 4:
                print(f"          Put {houses_needed_nc} house(s) on North Carolina.")

        # Out: No Properties
        else:
            print("You cannot purchase a hotel until you own all the properties of a given color group.")

    except ValueError:
        print("Please enter valid input.")

if __name__ == "__main__":
    main()

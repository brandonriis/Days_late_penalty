# 201358937 Tonge_Brandon-CA04.py
# November 2018
# This program will take a test mark as well as the days over
# the deadline. It will then print the final mark taking into
# consideration the penalty for the days late.

# Main Function
def main():

    # Main Menu
    print("\n---Main Menu---")
    print("A - Marking")
    print("E - Extend")
    print("X - Exit Program")
    print("")
    choice = str.upper(input("Please select an option from the menu: "))

    # TEST
    # print(choice)

    # Function Selection
    if(choice == "A"):
        marking()

    elif(choice == "E"):
        extended()

    elif(choice == "X"):
        exit()

    else:
        print("\nPlease enter a valid choice!\n")
        main()
# Marking Function
def marking():

    # User Inputs w/ Validation
    mark = int(input("\nPlease enter your original mark (0-100): "))

    while (mark <0 or mark >100):
        print("\nEnter a valid input!")
        mark = int(input("\nPlease enter your original mark (0-100): "))

    days_late = int(input("\nPlease enter the number of days late (0-12): "))

    while (days_late <0 or days_late >12):
        print("\nEnter a valid input!")
        days_late = int(input("\nPlease enter the number of days late (0-12): "))

    # Duplicate "days_late"
    days_late1 = days_late

    # Print Original Mark
    print("\n-Mark- -Days Late-")
    print(" ", mark, "  --  ", 0)

    # Mark Deduction Loop
    while (days_late != 0 and mark >40):
        mark = mark - 5
        days_late = days_late - 1
        l1 = days_late1 - days_late

        if (mark < 40):
            mark = 40

        print(" ", mark, "  --  ", l1)

    # Final print out
    if (days_late > 0 and mark == 40):
        print("\nYour score has been capped at 40 due to being over the "
              "deadline date and not scoring enough to deduct anymore.")
        print(f"\nYour work was {days_late1} days late, giving it the overall mark of {mark}")

    else:
        print(f"\nYour work was {days_late1} days late, giving it the overall mark of {mark}")

    main()

# Extended Function
def extended():

    print("\nExtended\n")
    main()

# Program Start
main()


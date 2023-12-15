# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    # Function to safely parse a float input
    def parse_float(prompt):
        while True:
            input_string = input(prompt)
            try:
                return float(input_string.replace(',', '').replace('$', '').replace('%', ''))
            except ValueError:
                print("Please enter a valid number.")

    # Function to safely parse an integer input
    def parse_int(prompt):
        while True:
            input_string = input(prompt)
            try:
                return int(input_string)
            except ValueError:
                print("Please enter a valid number.")

    # Prompt the user for all inputs
    savings_balance = parse_float('Enter savings account balance: ')
    savings_interest = parse_float('Enter savings account interest rate (APR %): ')
    savings_months = parse_int('Enter the number of months for the savings account: ')

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_months)
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f'Savings Account: Updated Balance: ${updated_savings_balance:,.2f}, Interest Earned: ${savings_interest_earned:,.2f}')
    
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = parse_float('Enter CD account balance: ')
    cd_interest = parse_float('Enter CD account interest rate (APR %): ')
    cd_months = parse_int('Enter the number of months for the CD account: ')

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f'CD Account: Updated Balance: ${updated_cd_balance:,.2f}, Interest Earned: ${cd_interest_earned:,.2f}')

if __name__ == "__main__":
    # Call the main function.
    main()

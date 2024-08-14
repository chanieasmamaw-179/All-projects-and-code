

#This question is just for the seek of our understanding, in section SE102.2, Main and Functions 
# The code was to develop for a cashies that will calculate added taxes and the change for costumer. N.B tha VAT was 11.5 %#

def user_input_prices():
    # Prompt the user to enter prices
    input_prices_str = input("Enter prices separated by spaces: ")
    # Split the input string into individual price strings
    input_prices_list = input_prices_str.split()
    # Initialize the list to store the prices as integers
    list_input_prices_int = []
    # Convert each price to an integer and add to the list
    for price in input_prices_list:
        list_input_prices_int.append(int(price))
    added_tax = float(input("Enter the tax percentage: "))
    return list_input_prices_int, added_tax
def add_tax_to_price(price, added_tax):
    # Calculate the tax amount
    tax_amount = price * added_tax / 100
    # Calculate the price after tax
    final_price = price + tax_amount
    return final_price, tax_amount
def apply_added_tax_on_prices(price_list, added_tax):
    # Initialize the list to store prices after tax
    list_final_prices = []
    list_tax_amounts = []
    for price in price_list:
        final_price, tax_amount = add_tax_to_price(price, added_tax)
        list_final_prices.append(final_price)
        list_tax_amounts.append(tax_amount)
    return list_final_prices, list_tax_amounts
def main():
    # Get the list of prices and the tax percentage from the user
    list_prices, add_tax_to_prices = user_input_prices()
    # Calculate the final prices and the tax amounts
    list_final_prices, list_tax_amounts = apply_added_tax_on_prices(list_prices, add_tax_to_prices)
    # Print the final prices and the tax amounts
    for original_price, final_price, tax_amount in zip(list_prices, list_final_prices, list_tax_amounts):
        print(f"Original Price: {original_price}, Tax Amount: {tax_amount}, Final Price: {final_price}")
if __name__ == "__main__":
    main()

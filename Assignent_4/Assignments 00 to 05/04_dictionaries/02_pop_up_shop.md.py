def main():
    # Dictionary storing fruit prices
    fruits = {
        'apple': 1.5, 'durian': 50, 'jackfruit': 80,
        'kiwi': 1, 'rambutan': 1.5, 'mango': 5
    }

    total_cost = 0  # Initialize total cost

    for fruit_name, price in fruits.items():
        while True:
            try:
                amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: "))
                if amount_bought < 0:
                    print("Please enter a valid non-negative number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        total_cost += price * amount_bought  # Update total cost

    # Display total with proper currency formatting
    print(f"\nYour total is: ${total_cost:.2f}")


if __name__ == '__main__':
    main()

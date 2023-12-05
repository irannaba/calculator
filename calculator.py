import re

def calculate(expression):
    # Replace '^' with '**' for exponentiation
    expression = expression.replace('^', '**')
    try:
        return round(eval(expression), 8)
    except Exception as e:
        return f"Error: {e}"

def main():
    while True:
        try:
            expression = input("Enter an expression (or 'exit' to quit): ")
            if expression.lower() == 'exit':
                break

            # Remove spaces for readability
            expression = expression.replace(" ", "")

            result = calculate(expression)
            print(f"Result: {result}")

        except KeyboardInterrupt:
            break
        except EOFError:
            break

if __name__ == "__main__":
    main()

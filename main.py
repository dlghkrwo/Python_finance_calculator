# take monthly income, apply a tax rate

def calculate_finance(monthly_income: float, tax_rate: float, expenses: float, currency: str) -> None:
    yearly_salary: float = monthly_income * 12
    monthly_tax: float = monthly_income * (tax_rate / 100)
    yearly_tax: float = monthly_tax * 12
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_net_income: float = yearly_salary - yearly_tax
    monthly_leftover: float = monthly_net_income - expenses

    print("-------------------------------------")
    print(f'Monthly income : {currency}{monthly_income: ,.2f}')
    print(f'Tax rate : {tax_rate: ,.0f}%')
    print(f'Monthly tax : {currency}{monthly_tax: ,.2f}')
    print(f'Monthly net income : {currency}{monthly_net_income: ,.2f}')
    print(f'Yearly salary : {currency}{yearly_salary: ,.2f}')
    print(f'Yearly tax paid : {currency}{yearly_tax: ,.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income: ,.2f}')
    print(f'Monthly expenses: {currency}{expenses: ,.2f}')
    print(f'Monthly leftover: {currency}{monthly_leftover: ,.2f}')
    print("-------------------------------------")

# if user enter wrong type, ask prompt again 
def get_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main() -> None:
    monthly_income = get_float_input('Enter your monthly salary: ')
    tax_rate = get_float_input('Enter your tax rate (%): ')
    expenses = get_float_input('Enter your monthly expenses: ')

    calculate_finance(monthly_income, tax_rate, expenses, currency='$')

if __name__ == '__main__':
    main()
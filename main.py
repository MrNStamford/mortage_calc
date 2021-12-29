# Creates calculator

def mort_payment(num_of_years, int_rate, loan_amount):
    num_of_terms = num_of_years * 12
    n = (int_rate/100)/12
    
    payment = loan_amount * (n * (1 + n)**num_of_terms)/(1 + n)**(num_of_terms - 1)

    print(str(num_of_terms) + ' monthly payments')
    print(str(n) + ' interest rate')
    print(str(payment) + ' avg monthly payment')

mort_payment(15, 3, 300000)
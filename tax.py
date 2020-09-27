def calculate_education_tax_credit(salary: int) -> int:
    """Calculate education tax credit per child."""
    if salary < 20000:
        credit_per_child = 800
    elif 20000 <= salary < 22000:
        credit_per_child = 800 - salary % 20000 * 0.2
    else:
        credit_per_child = 400
    return int(credit_per_child)


def calculate_tax(salary: int, num_children: int) -> int:
    """Calculate income tax, so simply you could file it on a postcard."""
    credit_per_child = calculate_education_tax_credit(salary)

    total_tax = salary * 0.5 - num_children * credit_per_child
    return int(total_tax)

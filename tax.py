def calculate_tax(salary: int, num_children: int) -> int:
    """Calculate income tax, so simply you could file it on a postcard."""
    if salary < 21000:
        scholarship_per_child = 800
    elif 21000 <= salary < 22000:
        scholarship_per_child = 800 - salary % 21000 * 0.2
    else:
        scholarship_per_child = 600

    total_tax = salary * 0.5 - num_children * scholarship_per_child
    return int(total_tax)

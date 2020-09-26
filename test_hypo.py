from hypothesis import given, strategies

from tax import calculate_tax


@given(
    salary=strategies.integers(),
    salary_raise=strategies.integers(min_value=1),
    num_children=strategies.integers(),
)
def test_raise_in_salary_never_causes_a_loss(salary, salary_raise, num_children):
    """
    Test that a raise in salary never triggers a tax increase greater than the raise.

    Running this test will show a failure, because a salary raise can cause a tax
    increase of more than 100% of the amount of the raise.
    """
    income_tax_without_raise = calculate_tax(salary=salary, num_children=num_children)
    income_tax_after_raise = calculate_tax(
        salary=salary + salary_raise, num_children=num_children
    )
    increased_tax = income_tax_after_raise - income_tax_without_raise
    assert increased_tax <= salary_raise

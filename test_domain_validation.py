import manage_domain
import pytest

def compose_error_message(domain_values, chosen_domain):
    error_message = "\nDomainValues: "
    for value in domain_values:
        error_message += f"\n{value}"
    return error_message

# def test_domain_values(environment1, chosen_domain):
#     domain_values = manage_domain.get_domain_values(environment1, chosen_domain)
#     assert len(domain_values) == 0, compose_error_message(domain_values, chosen_domain)
#
# def test_domain_values2(environment2, chosen_domain):
#     domain_values = manage_domain.get_domain_values(environment2, chosen_domain)
#     assert len(domain_values) == 0, compose_error_message(domain_values, chosen_domain)

def test_absent_domain_values(environment1, environment2, chosen_domain):
    absent_domain_values = manage_domain.get_domain_values_missing_from_list(manage_domain.get_domain_values(environment1, chosen_domain), manage_domain.get_domain_values(environment2, chosen_domain))
    assert len(absent_domain_values) ==0, compose_error_message(absent_domain_values, chosen_domain)

def test_surplus_domain_values(environment1, environment2, chosen_domain):
    absent_domain_values = manage_domain.get_domain_values_missing_from_list(manage_domain.get_domain_values(environment2, chosen_domain), manage_domain.get_domain_values(environment1, chosen_domain))
    assert len(absent_domain_values) == 0, compose_error_message(absent_domain_values, chosen_domain)
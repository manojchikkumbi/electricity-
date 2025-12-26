def electricity_bill(customer_name, units_consumed, rate_per_unit):
    total_amount = units_consumed * rate_per_unit

    result = (
        f"Customer Name: {customer_name}\n"
        f"Units Consumed: {units_consumed}\n"
        f"Rate per Unit: {rate_per_unit}\n"
        f"Total Bill Amount: {total_amount}"
    )
    return result


if __name__ == "__main__":
    customer_name = "Rahul"
    units_consumed = 120
    rate_per_unit = 5

    print(electricity_bill(customer_name, units_consumed, rate_per_unit))

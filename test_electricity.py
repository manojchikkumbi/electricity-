from electricity import electricity_bill

def test_electricity_bill():
    expected_output = (
        "Customer Name: Rahul\n"
        "Units Consumed: 120\n"
        "Rate per Unit: 5\n"
        "Total Bill Amount: 600"
    )

    assert electricity_bill("Rahul", 120, 5) == expected_output

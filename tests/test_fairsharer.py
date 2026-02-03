from fairsharer import fair_sharer


def test_fair_sharer():
    # Testfall: [10, 100, 10], share 0.1 -> 100 verliert 2*10, Nachbarn kriegen je 10
    input_values = [10, 100, 10]
    expected = [20.0, 80.0, 20.0]
    result = fair_sharer(input_values, num_iterations=1, share=0.1)
    assert result == expected
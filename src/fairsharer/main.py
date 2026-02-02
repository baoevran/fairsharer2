def fair_sharer(values, num_iterations, share=0.1):
    """
    Distributes values over time.

    In each iteration, the highest value gives a fraction (share)
    to its left and right neighbor (cyclic).

    Arguments:
        values (list[float]): initial values
        num_iterations (int): number of iterations
        share (float): fraction to distribute

    Returns:
        list[float]: redistributed values
    """
    values = list(values)

    for _ in range(num_iterations):
        max_index = values.index(max(values))
        max_value = values[max_index] * share

        left = (max_index - 1) % len(values)
        right = (max_index + 1) % len(values)

        values[max_index] -= 2 * max_value
        values[left] += max_value
        values[right] += max_value

    return values
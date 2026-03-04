# bug1_fixed.py
# Fixed version of bug1.py

# Type: Off-by-one error (fixed)

# The original code miscomputed the start index when n equals
# the length of the list, skipping the first element.  We
# update the calculation to either use a correct start index
# or take advantage of Python's negative slicing.

def get_last_n_items(items, n):
    """Return the last n items of a list."""
    # Correct calculation: start at len(items) - n
    start_index = len(items) - n
    # if n is 0 this will correctly return [] as well
    return items[start_index:]

# Alternatively, one could simply use: return items[-n:]


def main():
    my_list = [1, 2, 3, 4, 5]
    print("Last 2 items:", get_last_n_items(my_list, 2))
    print("Last 5 items:", get_last_n_items(my_list, 5))
    print("Last 0 items:", get_last_n_items(my_list, 0))


if __name__ == "__main__":
    main()

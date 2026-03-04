# bug1.py
# Type: Off-by-one error
# Intended Behavior: Return the last n items of a list.
# Issue: The function fails when n == len(items) due to incorrect slicing.

def get_last_n_items(items, n):
    """Return the last n items of a list."""
    # Off-by-one error: should be len(items) - n, not len(items) - n - 1
    start_index = len(items) - n - 1
    return items[start_index:]

def main():
    my_list = [1, 2, 3, 4, 5]
    
    # This works fine
    print("Last 2 items:", get_last_n_items(my_list, 2))
    
    # This fails when n == len(items)
    print("Last 5 items:", get_last_n_items(my_list, 5))

if __name__ == "__main__":
    main() 
def is_complete(numbers):
    if len(numbers) != 9:
        return False
    try:
        if sorted(numbers) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    except TypeError:
        return False
    return True

def get_region(board, ):


def done_or_not(board):
    for row in board:
        if not is_complete(row):
            return "Try again!"
    return "Finished!"

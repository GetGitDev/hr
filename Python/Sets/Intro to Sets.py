def average(array):
    top = sum(set(array))
    bot = len(set(array))
    return top / bot

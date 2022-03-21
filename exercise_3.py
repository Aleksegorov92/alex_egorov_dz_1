for percent in range(1, 101):
    if 11 <= percent <= 14:
        word = "процентов"
    elif percent % 10 == 0:
        word = "процентов"
    elif percent % 10 == 1:
        word = "процент"
    elif percent % 10 >= 5:
        word = "процентов"
    else:
        word = "процента"
    print(percent, word)

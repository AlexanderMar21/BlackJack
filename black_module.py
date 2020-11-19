import random
card_dict = {
    '2♤': 2, '2♧': 2, '2♡': 2, '2♢': 2,
    '3♤': 3, '3♧': 3, '3♡': 3, '3♢': 3,
    '4♤': 4, '4♧': 4, '4♡': 4, '4♢': 4,
    '5♤': 5, '5♧': 5, '5♡': 5, '5♢': 5,
    '6♤': 6, '6♧': 6, '6♡': 6, '6♢': 6,
    '7♤': 7, '7♧': 7, '7♡': 7, '7♢': 7,
    '8♤': 8, '8♧': 8, '8♡': 8, '8♢': 8,
    '9♤': 9, '9♧': 9, '9♡': 9, '9♢': 9,
    '10♤': 10, '10♧': 10, '10♡': 10, '10♢': 10,
    'J♤': 10, 'J♧': 10, 'J♡': 10, 'J♢': 10,
    'Q♤': 10, 'Q♧': 10, 'Q♡': 10, 'Q♢': 10,
    'K♤': 10, 'K♧': 10, 'K♡': 10, 'K♢': 10

}
A = ['A♤', 'A♧', 'A♡', 'A♢']
# take the first card and remove it from the array
def rand_picker(li):
    first_card = li[0]
    li.pop(0)
    return first_card

# prints again the cards
def card_print(li2):
    for i in li2:
     print(" ",i, end=" ")
# checks the values of the cards plus if they exist 1 or 2 'A'
def sum_check(li):
    sum = 0
    for i in li :
        if i not in A:
            sum += card_dict[i]
    count = 0
    for i in li:
        if i in A :
            count +=1

    if count > 0:
        if count <= 1:
            if (sum + 11) > 21 :
                sum += 1
            elif (sum + 11) <= 21:
                sum += 11
        elif count > 1:
            if (sum + 11 + (count-1)) > 21:
                sum += count * 1
            elif (sum + 11 + (count-1)) <= 21:
                sum += 11 + (count-1) * 1

    return sum
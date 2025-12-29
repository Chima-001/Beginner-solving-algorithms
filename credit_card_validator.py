def verify_card_number(card_number):

    card_number = card_number.replace('-', '').replace(' ', '')

    if not card_number.isdigit():
        return 'INVALID!'

    reverse = str(card_number)[::-1]
    total = 0

    for index, number in enumerate(reverse):
        #doubled = 0
        if index % 2 == 1:
            doubled = int(number) * 2
            if doubled > 9:
                doubled -= 9
                total += doubled
            else:
                total += doubled
        else:
            total += int(number)

    return 'VALID!' if total % 10 == 0 else 'INVALID!'

print(verify_card_number('453914889'))
print(verify_card_number('4111-1111-1111-1111'))

print(verify_card_number('1234 5678 9012 3456'))

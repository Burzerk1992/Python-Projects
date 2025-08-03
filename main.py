def verify_card_number(card_number):
    sum_of_odd_digits = 0
    #Third value on the index is how to step over between the start and end index
    card_number_reversed = card_number[::-1]
    #This gets just the odd numbers
    odd_digits = card_number_reversed[::2]
    #This gets just the even numbers
    even_digits = card_number_reversed[1::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    
    sum_of_even_digits = 0
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = number // 10 + number % 10
        sum_of_even_digits += number
    
    total = sum_of_even_digits + sum_of_odd_digits
    return 0 == total%10


def main():
    card_number = '4111-1111-4555-1142'
    #creates a translation table
    card_translation = str.maketrans({'-': '', ' ': ''})
    #this variable stores the card number with all - and spaces removed using the translation funciton passing the tabel from line 4
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print("VALID!")
    else:
        print("INVALID!")
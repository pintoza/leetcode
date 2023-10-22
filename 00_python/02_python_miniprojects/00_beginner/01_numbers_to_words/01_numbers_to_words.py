def get_user_input():
    return input("Enter a number between 1 and 1,000,000: ")


def convert_to_words(num_str):
    if not num_str.isdigit():
        return "Please enter a valid number"

    num = int(num_str)

    # Convert number to words
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
            "eighty", "ninety"]

    # Initialize empty word list
    words = []

    if num == 0:
        return "zero"
    elif num < 0:
        return "negative " + convert_to_words(str(abs(num)))
    elif num == 1000000:
        return "one million"

    if num >= 1000:
        thousands_part = num // 1000
        if thousands_part > 0:
            words.append(convert_to_words(str(thousands_part)) + " thousand")
        num %= 1000

    if num >= 100:
        hundreds_part = num // 100
        if hundreds_part > 0:
            words.append(ones[hundreds_part] + " hundred")
        num %= 100

    if 10 < num < 20:
        words.append(teens[num - 10])

    else:
        tens_part = num // 10
        if tens_part > 0:
            words.append(tens[tens_part])
        ones_part = num % 10
        if ones_part > 0:
            words.append(ones[ones_part])

    return " ".join(filter(None, words))


def main():
    num_str = get_user_input()
    print(convert_to_words(num_str))


if __name__ == "__main__":
    main()

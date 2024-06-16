def findFactor(number):
    """
    Find all the factors of a number and determine whether each factor is even or odd.
    >>>findFactor(6)
    1 is an odd factor of 6
    2 is an even factor of 6
    3 is an odd factor of 6

    """
    # Initialize a list to store the factors
    factors = []

    # Loop to find all factors of number
    for i in range(1, number + 1):
        if (number % i == 0):
            factors.append(i)

    # Check if each factor is even or odd and print the result        
    for factor in factors:
         if (factor % 2 == 0):
             print(factor, "is an even factor of", number)

         else:
             print(factor, "is an odd factor of", number)
def wordsSequence():
    
    """(string) -> string
    Return an ordered sequence of words from an unordered sequence of words.
    >>>wordsSequence()
    Enter a sequence of words: je te deteste de tout mon coeur
    'coeur de deteste je mon te tout'
    """
    sequenceOfWords = input("Enter a sequence of words: ")

    # Split the input string into a list of words
    wordsList = sequenceOfWords.split()

    # Sort the list of words alphabetically
    sortedWordsList = sorted(wordsList)

    # Join the sorted list into a single string with spaces in between
    sortedSequence = " ".join(sortedWordsList)
    
    return sortedSequence


def evenDigitNumber():

    """
        Find  and print all the numbers between 1000 and 3000 whose digits are all even.
        >>> evenDigitNumber()
        2000,2002,2004,2006,2008,2020,2022,2024,2026,2028,2040,2042,2044,2046,2048,2060,
        2062,2064,2066,2068,2080,2082,2084,2086,2088,2200,2202,2204,2206,2208,2220,2222,
        2224,2226,2228,2240,2242,2244,2246,2248,2260,2262,2264,2266,2268,2280,2282,2284,2286,
        2288,2400,2402,2404,2406,2408,2420,2422,2424,2426,2428,2440,2442,2444,2446,2448,2460,
        2462,2464,2466,2468,2480,2482,2484,2486,2488,2600,2602,2604,2606,2608,2620,2622,2624,
        2626,2628,2640,2642,2644,2646,2648,2660,2662,2664,2666,2668,2680,2682,2684,2686,2688,
        2800,2802,2804,2806,2808,2820,2822,2824,2826,2828,2840,2842,2844,2846,2848,2860,2862,
        2864,2866,2868,2880,2882,2884,2886,2888

    """

    # List to store the numbers with all even digits
    numbers = []

    # Loop through the range from 1000 to 3000
    for i in range(1000, 3001):
        stri = str(i)
        n = 0

        # Count the number of digit even
        for char in stri:
            if (int(char)% 2 == 0):
                n = n + 1

        # Check if all digits are even
        if n == len(stri):
            numbers.append(stri)

    # Print the result as a comma-separated sequence
    print(",".join(numbers))

def numLetAndDig():

    """
    Print the number of letters and digits in a sequence of letters and numbers.
    >>> numLetAndDig()
    Enter a sequence of letters and digits: Python0325
    LETTERS:  6

    """

    # Initialize counters for letters and digits
    numLetters = 0
    numDigits = 0

    # Input a sequence of letters and digits
    sequence = input("Enter a sequence of letters and digits: ")

    for char in sequence:

        # Check if each character is a letter or a digit
        if char.isalpha():
            numLetters = numLetters + 1
        elif char.isdigit():
            numDigits = numDigits + 1

    # Print the numbers of letters and digits
    print("LETTERS: ", numLetters)
    print("DIGITS: ", numDigits)


def palindromicNumbers():
    """
    Determine wheter or not a number is palindromic.
    >>> palindromicNumbers()
    Enter  number: 16461
    16461 is palindromic.

    """

    number = int(input("Enter  number: "))

    if "".join(reversed(str(number))) == str(number):
        print(number, "is palindromic.")
    else:
        print(number, "is not palindromic.")
        
    



                       
                

        

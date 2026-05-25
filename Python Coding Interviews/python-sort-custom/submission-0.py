from typing import List

def word_length(string):
    return len(string)

def number_abs(numbers):
    bruh = []
    while len(numbers) != 0:
        mini = numbers[0]
        for i in numbers:
            if abs(i) < abs(mini):
                mini = i
        bruh.append(mini)
        numbers.remove(mini)
    return bruh

def sort_words(words: List[str]) -> List[str]:
    words.sort(key = word_length, reverse = True)
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    return number_abs(numbers)
    
    


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))

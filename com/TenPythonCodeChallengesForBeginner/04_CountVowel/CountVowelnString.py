def count_vowel_in_string(words: str) -> int:
    count = 0
    for word in words:
        if word in ('a', 'e', 'i', 'o', 'u'):
            count += 1

    return count


if __name__ == '__main__':
    words_to_count_vowel = ""
    count_of_vowel = count_vowel_in_string(words_to_count_vowel)
    print(f'Count of vowel in "{words_to_count_vowel}" is: {count_of_vowel}')

# task 3
# Typing speed Test Submitted by Bisma Sheikh


import time
import random


def generate_random_text():
    words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    random_text = ' '.join(random.choices(words, k=50))  # Generate 50 random words
    return random_text


def calculate_typing_speed(start_time, end_time, typed_text):
    total_seconds = (end_time - start_time) / 60  # Convert to minutes
    words_typed = len(typed_text.split())
    typing_speed = words_typed / total_seconds
    return typing_speed


def typing_speed_test():
    print("Welcome to Typing Speed Test!")
    print("You will be given a random text to type.")
    print("Type the given text and press Enter when you're done.")
    input("Press Enter to start...")

    random_text = generate_random_text()
    print("Type the following text:\n")
    print(random_text)

    input("\nPress Enter when you're ready to start typing...")

    start_time = time.time()
    typed_text = input("Start typing: ")
    end_time = time.time()

    typing_speed = calculate_typing_speed(start_time, end_time, typed_text)
    print("\nTyping speed: {:.2f} words per minute (WPM)".format(typing_speed))


if __name__ == "__main__":
    typing_speed_test()

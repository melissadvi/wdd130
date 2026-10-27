import csv
import random
import json

def load_kana_table(filename):
    """Read the kana CSV file and return a dictionary.
 
    Each key is a romaji syllable and each value is a dictionary with
    the hiragana and katakana for that syllable.
 
    Example:
        {"ka": {"hiragana": "か", "katakana": "カ"}, ...}
 
    Parameter
        filename: the name of the CSV file to read.
    Return: the kana dictionary.
    """
    kana_table = {}
    with open(filename, "rt", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            romaji = row["romaji"]
            kana_table[romaji] = {
                "hiragana": row["hiragana"], 
                "katakana": row["katakana"]
            }
    return kana_table

def hiragana_to_katakana(hiragana):
    """Convert hiragana characters in a string to katakana.

    Characters that are not hiragana (katakana, letters, numbers,
    spaces) are kept the same.

    Parameter
        text: a string that may contain hiragana.
    Return: the string with hiragana changed to katakana.
    """
    result = ""
    for char in hiragana:
        code = ord(char)
        if 0x3041 <= code <= 0x3096: 
            result += chr(code + 0x60)
        else:
            result += char
    return result

def romaji_to_hiragana(romaji, kana_table):
    """Convert a romaji string to hiragana using the kana table.

    Parameter
        romaji: a string in romaji.
        kana_table: a dictionary mapping romaji to hiragana and katakana.
    Return: the string converted to hiragana.
    """
    romaji = romaji.lower()
    result = ""
    i = 0
    while i < len(romaji):
        for size in range(3, 0, -1):
            syllable = romaji[i:i+size]
            if syllable in kana_table:
                result += kana_table[syllable]["hiragana"]
                i += size
                break
        else:
            result += romaji[i]
            i += 1
    return result

def pick_random_kana(kana_table):
    """Pick a random kana syllable from the kana table.

    Parameter
        kana_table: a dictionary mapping romaji to hiragana and katakana.
    Return: a tuple (romaji, hiragana, katakana).
    """
    romaji = random.choice(list(kana_table.keys()))
    return romaji, kana_table[romaji]

def check_answer(user_answer, correct_kana):
    """Check if the user's answer matches the correct kana.

    Parameter
        user_answer: the answer provided by the user.
        correct_kana: the correct kana (hiragana or katakana).
    Return: True if the answer is correct, False otherwise.
    """
    user_answer = user_answer.strip()
    return (
        user_answer == correct_kana["hiragana"] or
        user_answer == correct_kana["katakana"]
    )

def calculate_score(correct, total):
    """Calculate the percentage score of the quiz.

    Parameters
        correct: number of correct answers.
        total: total number of questions answered.
    Return: float representing the percentage (0.0 to 100.0).
    """
    if total == 0:
        return 0.0
    return round((correct / total) * 100, 1)

def get_missed_kana(results):
    """Filter results to find which characters the user missed.

    Parameter
        results: a list of dictionaries tracking attempts.
    Return: a list of missed items.
    """
    return [item for item in results if not item["correct"]]

def show_menu():
    """Display the main menu options to the user."""
    print("\n--- KANA HELPER MENU ---")
    print("1. Convert Romaji to Hiragana")
    print("2. Convert Hiragana to Katakana")
    print("3. Take Kana Quiz")
    print("4. Exit")

def get_menu_choice(prompt, min_option, max_option):
    """Prompt the user for a menu choice and validate it.

    Parameters
        prompt: string prompt to display.
        min_option: minimum valid integer option.
        max_option: maximum valid integer option.
    Return: the valid integer chosen by the user.
    """
    while True:
        try:
            choice = int(input(prompt))
            if min_option <= choice <= max_option:
                return choice
            else:
                print(f"Error: Please enter a number between {min_option} and {max_option}.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")

def run_converter(kana_table):
    """Run the interactive romaji to hiragana/katakana converter loop."""
    print("\n--- KANA CONVERTER ---")
    print("Type 'exit' to return to the main menu.")
    while True:
        text = input("Enter romaji text: ").strip()
        if text.lower() == 'exit':
            break
        if not text:
            continue
        
        hiragana = romaji_to_hiragana(text, kana_table)
        katakana = hiragana_to_katakana(hiragana)
        
        print(f"  Hiragana: {hiragana}")
        print(f"  Katakana: {katakana}")

def run_quiz(kana_table, num_questions=5):
    """Run an interactive quiz to test kana knowledge.

    Parameters
        kana_table: the dictionary containing kana mappings.
        num_questions: total number of questions to ask.
    Return: a list of result dictionaries for each question.
    """
    print(f"\n--- KANA QUIZ ({num_questions} questions) ---")
    print("Type the hiragana or katakana for the given romaji syllable. Type 'exit' to quit early.")
    
    results = []
    correct_count = 0
    
    for i in range(1, num_questions + 1):
        romaji, kana_info = pick_random_kana(kana_table)
        answer = input(f"Question {i}/{num_questions}: What is the kana for '{romaji}'? ").strip()
        
        if answer.lower() == 'exit':
            print("Exiting quiz early...")
            break
            
        is_correct = check_answer(answer, kana_info)
        results.append({
            "romaji": romaji,
            "correct": is_correct,
            "user_answer": answer,
            "expected": kana_info["hiragana"]
        })
        
        if is_correct:
            print("  Correct! 🎉")
            correct_count += 1
        else:
            print(f"  Incorrect. The correct answer was {kana_info['hiragana']} (Hiragana) / {kana_info['katakana']} (Katakana).")
            
    total_answered = len(results)
    score = calculate_score(correct_count, total_answered)
    missed = get_missed_kana(results)
    
    show_results(correct_count, total_answered, score, missed)
    return results

def show_results(correct, total, score, missed):
    """Display the final quiz results and summary of missed items."""
    print("\n--- QUIZ RESULTS ---")
    print(f"Total answered: {total}")
    print(f"Correct: {correct}")
    print(f"Score: {score}%")
    
    if missed:
        print("\nCharacters to review:")
        for item in missed:
            print(f"  - Romaji: {item['romaji']} (You typed: {item['user_answer']}, Expected: {item['expected']})")
    else:
        print("\nFantastic! You got everything right! 🌟")

def save_results(filename, results):
    """Save the quiz results to a JSON file.

    Parameters
        filename: name of the JSON file to write to.
        results: list of result dictionaries.
    """
    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump(results, jsonfile, ensure_ascii=False, indent=4)

def load_results(filename):
    """Load quiz results from a JSON file.

    Parameters
        filename: name of the JSON file to read from.
    Return: list of result dictionaries.
    """
    try:
        with open(filename, "r", encoding="utf-8") as jsonfile:
            return json.load(jsonfile)
    except FileNotFoundError:
        return []

def main():
    try:
        kana_table = load_kana_table("kana.csv")
    except FileNotFoundError:
        print("Error: kana.csv file not found.")
        return
    
    print(f"Loaded {len(kana_table)} kana.")
    
    while True:
        show_menu()
        choice = get_menu_choice("Choose an option (1-4): ", 1, 4)
        
        if choice == 1:
            run_converter(kana_table)
        elif choice == 2:
            text = input("Enter hiragana text to convert to katakana: ").strip()
            print(f"  Katakana: {hiragana_to_katakana(text)}")
        elif choice == 3:
            results = run_quiz(kana_table, num_questions=5)
            if results:
                save_results("quiz_results.json", results)
                print("Quiz results saved to quiz_results.json!")
        elif choice == 4:
            print("Thank you for using Kana Helper. Sayōnara! 👋")
            break

if __name__ == "__main__":
    main()
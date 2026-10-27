import pytest
from kana_helper import (
    load_kana_table, 
    hiragana_to_katakana, 
    romaji_to_hiragana,
    pick_random_kana,
    check_answer,
    calculate_score,
    get_missed_kana,
    show_menu,
    get_menu_choice,
    run_converter,
    run_quiz,
    show_results,
    save_results,
    load_results
)

def test_load_kana_table():
    kana_table = load_kana_table("kana.csv")
    assert isinstance(kana_table, dict)
    assert len(kana_table) == 49
    assert kana_table["a"]["hiragana"] == "あ"
    assert kana_table["a"]["katakana"] == "ア"
    assert kana_table["ka"]["hiragana"] == "か"
    assert kana_table["shi"]["katakana"] == "シ"
    assert kana_table["n"]["hiragana"] == "ん"

def test_hiragana_to_katakana():
    assert hiragana_to_katakana("あいうえお") == "アイウエオ"
    assert hiragana_to_katakana("かきくけこ") == "カキクケコ"
    assert hiragana_to_katakana("さしすせそ") == "サシスセソ"
    assert hiragana_to_katakana("たちつてと") == "タチツテト"
    assert hiragana_to_katakana("なにぬねの") == "ナニヌネノ"
    assert hiragana_to_katakana("はひふへほ") == "ハヒフヘホ"
    assert hiragana_to_katakana("まみむめも") == "マミムメモ"
    assert hiragana_to_katakana("やゆよ") == "ヤユヨ"
    assert hiragana_to_katakana("らりるれろ") == "ラリルレロ"
    assert hiragana_to_katakana("わをん") == "ワヲン"
    assert hiragana_to_katakana("こんにちは、世界！") == "コンニチハ、世界！"
    assert hiragana_to_katakana("abc123") == "abc123"
    assert hiragana_to_katakana("") == ""

def test_romaji_to_hiragana():
    kana_table = load_kana_table("kana.csv")

    assert romaji_to_hiragana("konnichiwa", kana_table) == "こんにちわ"
    assert romaji_to_hiragana("arigatou", kana_table) == "ありがとう"
    assert romaji_to_hiragana("sakura", kana_table) == "さくら"
    assert romaji_to_hiragana("sushi", kana_table) == "すし"
    assert romaji_to_hiragana("tsuki", kana_table) == "つき"
    assert romaji_to_hiragana("watashi", kana_table) == "わたし"
    assert romaji_to_hiragana("nihon", kana_table) == "にほん"
    assert romaji_to_hiragana("kawaii", kana_table) == "かわいい"
    assert romaji_to_hiragana("SENSEI", kana_table) == "せんせい"
    assert romaji_to_hiragana("den wa", kana_table) == "でん わ"
    assert romaji_to_hiragana("123", kana_table) == "123"
    assert romaji_to_hiragana("", kana_table) == ""

def test_pick_random_kana():
    kana_table = load_kana_table("kana.csv")
    romaji, info = pick_random_kana(kana_table)
    assert romaji in kana_table
    assert info == kana_table[romaji]

def test_check_answer():
    kana_info = {"hiragana": "か", "katakana": "カ"}
    assert check_answer("か", kana_info) is True
    assert check_answer("カ", kana_info) is True
    assert check_answer("ku", kana_info) is False

def test_calculate_score():
    assert calculate_score(8, 10) == 80.0
    assert calculate_score(3, 4) == 75.0
    assert calculate_score(0, 0) == 0.0

def test_get_missed_kana():
    results = [
        {"romaji": "a", "correct": True},
        {"romaji": "ka", "correct": False},
        {"romaji": "shi", "correct": False}
    ]
    missed = get_missed_kana(results)
    assert len(missed) == 2
    assert missed[0]["romaji"] == "ka"
    assert missed[1]["romaji"] == "shi"

def test_show_menu(capsys):
    show_menu()
    captured = capsys.readouterr()
    assert "KANA HELPER MENU" in captured.out
    assert "1. Convert Romaji to Hiragana" in captured.out
    assert "2. Convert Hiragana to Katakana" in captured.out
    assert "3. Take Kana Quiz" in captured.out
    assert "4. Exit" in captured.out

def test_get_menu_choice_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    assert get_menu_choice("Choose: ", 1, 4) == 2

def test_get_menu_choice_invalid_then_valid(monkeypatch):
    inputs = iter(['9', 'abc', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_menu_choice("Choose: ", 1, 4) == 3

def test_run_converter(monkeypatch):
    kana_table = load_kana_table("kana.csv")
    inputs = iter(['konnichiwa', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    run_converter(kana_table)
    # No assertion here; this test ensures no exceptions are raised

def test_run_quiz(monkeypatch):
    kana_table = load_kana_table("kana.csv")
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    results = run_quiz(kana_table, num_questions=1)
    assert isinstance(results, list)

def test_show_results(capsys):
    missed = [{"romaji": "a", "user_answer": "i", "expected": "あ"}]
    show_results(1, 2, 50.0, missed)
    captured = capsys.readouterr()
    assert "Score: 50.0%" in captured.out
    assert "Characters to review:" in captured.out

def test_save_and_load_results(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    file_path = d / "test_results.json"
    sample_results = [{"romaji": "a", "correct": True}]
    save_results(file_path, sample_results)
    loaded_results = load_results(file_path)
    assert loaded_results == sample_results

def test_load_results_missing_file():
    loaded = load_results("non_existent_file.json")
    assert loaded == []

def test_load_kana_table_missing_file():
    with pytest.raises(FileNotFoundError):
        load_kana_table("does_not_exist.csv")

pytest.main(["-v", "--tb=line", "-rN", __file__])
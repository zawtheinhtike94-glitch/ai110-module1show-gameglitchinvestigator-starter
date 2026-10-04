from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_message_says_go_lower():
    # Bug fix: the hint used to say "Go HIGHER" when the guess was too high
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_single_digit_guess_compares_as_number():
    # Bug fix: comparing "9" > "50" as text gave the wrong hint
    outcome, message = check_guess(9, 50)
    assert outcome == "Too Low"

def test_hard_range_is_bigger_than_normal():
    # Bug fix: Hard used to be 1-50, easier than Normal's 1-100
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high

def test_parse_guess_rejects_text():
    ok, value, err = parse_guess("abc")
    assert not ok
    assert err == "That is not a number."

def test_wrong_guess_always_loses_points():
    # Bug fix: a "Too High" guess on an even attempt used to add 5 points
    assert update_score(50, "Too High", 2) == 45
    assert update_score(50, "Too Low", 2) == 45

def test_first_try_win_gives_full_points():
    # Bug fix: winning on the first attempt used to give 80 instead of 100
    assert update_score(0, "Win", 1) == 100

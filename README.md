# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

### Game purpose

Game Glitch Investigator is a number guessing game built with Streamlit. The game picks a secret number in a range set by the difficulty (Easy 1–20, Normal 1–100, Hard 1–200). The player has a limited number of attempts to guess it, and after each guess a hint says whether to go higher or lower. Fewer attempts means a higher score.

### Bugs found and fixes applied

| # | Bug | Fix |
|---|-----|-----|
| 1 | **Backwards hints.** A guess that was too high said "Go HIGHER", and one that was too low said "Go LOWER". | Swapped the messages in `check_guess` so "Too High" says "📉 Go LOWER!" and "Too Low" says "📈 Go HIGHER!". |
| 2 | **Secret turned into text.** On every even attempt, `app.py` converted the secret to a string. Python then compared text, so `"9" > "50"` was `True` and the hint was wrong. After removing the `try/except` that hid it, it crashed with `TypeError: '>' not supported between instances of 'int' and 'str'`. | The secret is now always an int (`secret = st.session_state.secret`). I removed the `try/except TypeError` workaround from `check_guess`. |
| 3 | **New Game didn't work after a win or loss.** It reset the secret and attempts but not `status`, so the game still said "You already won." | Added a `start_new_game()` function that resets the secret, attempts, score, status and history. |
| 4 | **New Game ignored difficulty.** It always used `random.randint(1, 100)`. | New Game now uses the selected difficulty's `low, high` range. |
| 5 | **Hard was easier than Normal.** Hard used the range 1–50. | Hard is now 1–200. |
| 6 | **Changing difficulty mid-game kept the old secret,** so the secret could be outside the new range. | Changing difficulty now starts a new game. |
| 7 | **The prompt always said "between 1 and 100",** whatever the difficulty. | It now shows the real range. |
| 8 | **Off-by-one attempts.** Attempts started at 1 on first load (but 0 after New Game), so the player lost one guess. | Attempts always start at 0. |
| 9 | **Wrong scoring.** A "Too High" guess *added* 5 points on even attempts, and a first-try win gave 80 points instead of 100. | Every wrong guess now subtracts 5, and a first-try win gives 100. |

### Refactor

The game logic functions (`get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`) moved from `app.py` to `logic_utils.py`, and `app.py` imports them. This let pytest test the logic without running Streamlit. The original tests compared the result to `"Win"`, but `check_guess` returns `(outcome, message)`, so the tests now unpack both values. I also added 7 tests that cover each logic bug fixed above.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Run `python -m streamlit run app.py`. The game opens in the browser at `http://localhost:8501`.
2. In the sidebar, choose a difficulty (Easy, Normal or Hard). The sidebar shows the range and the number of attempts allowed.
3. Type a guess in the "Enter your guess" box and click **Submit Guess 🚀**.
4. Read the hint. If the guess is too high it says "📉 Go LOWER!", and if it's too low it says "📈 Go HIGHER!". The secret stays the same between guesses.
5. Keep guessing until you find the number. Balloons appear and the game shows "You won!" with your final score.
6. Click **New Game 🔁** to start again with a new secret number in the same difficulty range.
7. (Optional) Open **Developer Debug Info** to see the secret, attempts, score and guess history.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ python -m pytest
============================= test session starts ==============================
collected 10 items

tests/test_game_logic.py ..........                                      [100%]

============================== 10 passed in 0.01s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

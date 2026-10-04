# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I used Claude Code (an AI coding agent) to help me set up the project, understand pytest errors, and fix the game. After I moved `check_guess` into `logic_utils.py` and fixed the hint messages myself, I asked the agent to finish the refactor and fix the remaining bugs.

**What did the agent do?**

- Ran `python -m pytest` in the project's virtual environment to see which tests failed and why.
- Read `app.py` and found that the secret was converted to a string on every even attempt (`if st.session_state.attempts % 2 == 0: secret = str(...)`).
- Edited `app.py`: removed the duplicate logic functions, imported them from `logic_utils.py`, kept the secret as an int, and added a `start_new_game()` function so New Game, first load and difficulty changes all reset the game.
- Edited `logic_utils.py`: removed the `try/except TypeError` workaround, made Hard 1–200, and fixed `update_score`.
- Added tests in `tests/test_game_logic.py` for each logic bug.
- Used Streamlit's `AppTest` to simulate a game (win, then New Game, then switch to Hard) and check that there were no errors.

**What did you have to verify or fix manually?**

- **VS Code overwrote the agent's fixes twice.** I had `app.py` open with unsaved changes, and saving it put the old code back. The first time, the game crashed with `TypeError: '>' not supported between instances of 'int' and 'str'`. The second time, New Game still said "You already won." I learned to use **Revert File** to load the version on disk.
- I played the game in the browser with Developer Debug Info open to confirm that the hints were correct, the secret stayed the same, and New Game worked after a win.
- I checked that pytest went from 3 failed, to 3 passed, to 10 passed.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->

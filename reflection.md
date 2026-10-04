# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The first time I ran the game, it looked normal, with a title, a difficulty picker, a guess box and Submit/New Game buttons. Once I played, the hints didn't make sense: when my guess was too high, it told me to go higher. Sometimes the hint was wrong even when I followed it, which turned out to be because the secret became text on every even attempt. After I won once, clicking New Game still said "You already won," so I couldn't play again. All 3 pytest tests also failed with `NotImplementedError` because the logic functions in `logic_utils.py` were empty placeholders.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret 50, guess 60 | Hint says "Go LOWER" | Hint said "📈 Go HIGHER!" | none |
| Guess 5 on an even-numbered attempt | Correct hint | App crashed (after the `try/except` that hid the bug was removed) | `TypeError: '>' not supported between instances of 'int' and 'str'` |
| Win a game, then click New Game | New game starts | Still showed "You already won. Start a new game to play again." | none |
| Select Hard difficulty | Bigger range than Normal | Range was 1 to 50 (Normal is 1 to 100) | none |
| Run `python -m pytest` on the starter code | Tests run against the logic | All 3 tests failed | `NotImplementedError: Refactor this function from app.py into logic_utils.py` |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used Claude (Claude Code) to help me with the terminal, read pytest output, and fix the bugs. One correct suggestion was that the secret was being turned into a string on even attempts with `str(st.session_state.secret)`, and that it should always stay a number. I checked this by playing several guesses in a row with Developer Debug Info open, and the hints were right every time and the game didn't crash. One thing I didn't accept as written was the original test code. The tests compared the result to `"Win"`, but `check_guess` returns two values, `(outcome, message)`. Instead of changing the function, which the game needs for its messages, I changed the tests to unpack `outcome, message` and checked only `outcome`. Then I ran pytest and saw the tests pass.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed when pytest passed **and** the game behaved correctly when I played it in the browser. Running `python -m pytest` first showed 3 failures with `NotImplementedError`. After I moved `check_guess`, the failures became `AssertionError: assert ('Win', '🎉 Correct!') == 'Win'`, which showed me the function returned two values. After fixing the tests, all 3 passed, and later 10 passed with the new tests. AI helped me learn to read the pytest output: the `E` lines show the error, and `file.py:line` shows where to look.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every time you click a button or type something in a Streamlit app, Streamlit runs the whole Python file again from top to bottom. That means a normal variable like `secret = random.randint(1, 100)` would get a new random number on every click. `st.session_state` is like a memory box that survives these reruns, so the secret, the attempts and the score stay the same until you choose to reset them. When you start a new game, you have to reset **everything** in session state, including the status, or old values like "won" stay behind.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to keep is running `python -m pytest` after every change and reading the `E` lines to see what went wrong. Next time, I'll close or revert open files in VS Code before letting an AI agent edit them, because my unsaved editor overwrote the AI's fixes twice and brought the bugs back. This project showed me that AI-generated code can look finished and still have hidden bugs, so I need to test it and understand it myself instead of trusting it.

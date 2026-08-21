# loop.md — The Manual Coding Loop & Checker

The loop I run **myself** on every lab task, before I ask Claude anything.
Claude uses the same checklist when I say **"check this"** — as a checker, not a fixer.
Rules for how much Claude may reveal live in `CLAUDE.md`.

---

## Part A — My loop (I do this, not Claude)

### Step 1 — Read the task twice, write it in my own words
In a markdown cell above the task, write **one sentence**: what goes in, what comes out.

- [ ] Input: where does the data come from? (literal / file / user / library)
- [ ] Output: printed? returned? written to a file? what exact shape?
- [ ] Any word in the task I can't define? → look it up **before** typing code.

> If I can't write this sentence, I don't understand the task yet. Coding now is guessing.

### Step 2 — Plan in plain English (no Python)
List the steps as numbered sentences. 3–7 steps is normal.

```
1. open the file for reading
2. read all the text into one string
3. go through it character by character
4. count vowels / consonants / digits separately
5. print the three counts
```

- [ ] Every step is something I already know how to do.
- [ ] The step I *don't* know how to do is circled — **that** is my real question.

### Step 3 — Write it myself, ugly is fine
- [ ] Write the whole thing first. Don't polish mid-way.
- [ ] Use boring, descriptive names (`vowel_count`, not `vc`).
- [ ] `print()` the intermediate values while building — delete them at the end.

### Step 4 — Self-check BEFORE running (the checker pass)
Run down Part B below on my own code. Most of my bugs die here.

### Step 5 — Run it
- [ ] Did it run at all? If not → read the **last line** of the traceback first.
- [ ] Is the output the *shape* the task asked for?
- [ ] Is the output *correct*? Verify one case by hand, on paper.

### Step 6 — Break it on purpose
- [ ] Empty input / empty file
- [ ] Missing file / wrong path
- [ ] Wrong type (text where a number is expected)
- [ ] Zero items, one item, many items

### Step 7 — Explain it out loud
Say what each line does, as if to a classmate. Any line I can't explain, I don't own.
→ Go ask about **that line**, at L0/L1.

### Step 8 — Clean up
- [ ] Debug prints removed
- [ ] Names still make sense
- [ ] A one-line comment where the *why* isn't obvious (not what — why)
- [ ] Cells run top to bottom in a fresh kernel (Restart & Run All)

---

## Part B — The checklist (self-check, and what Claude checks)

### B1. Correctness
- [ ] Does it answer the **exact** question asked, not a similar one?
- [ ] Off-by-one: ranges, slices, `<` vs `<=`, first/last item.
- [ ] Is a variable used before it's assigned, or reused for two different things?
- [ ] Am I modifying a list while looping over it?
- [ ] Does every branch (`if`/`elif`/`else`) actually get reached?
- [ ] Does the function `return` (not just `print`) when the task wants a value?

### B2. Files & data (this course's favourite trap)
- [ ] Right mode: `'r'` read, `'w'` overwrite, `'a'` append, `'rb'`/`'wb'` for pickle.
- [ ] `with open(...)` used — no manual `.close()` inside a `with` (it's redundant).
- [ ] Relative path vs absolute path: which folder is the notebook actually running in?
- [ ] Does `'w'` here silently destroy a file I need for a later task?
- [ ] Reading returns **text** — did I convert to `int`/`float` when I need a number?

### B3. Exceptions
- [ ] Am I catching the exception that actually happens? (`FileNotFoundError` vs `ValueError`)
- [ ] Is the `try` block as small as possible, or did I wrap 20 lines "just in case"?
- [ ] Bare `except:` / `except Exception:` — is it hiding a bug I should see?
- [ ] Does the handler leave the program in a sane state, or just print and continue broken?

### B4. Robustness
- [ ] Empty input, missing file, wrong type — from Step 6.
- [ ] Hardcoded values that should be parameters or constants.
- [ ] Any absolute Windows path (`D:\...`) that will break on the marker's machine.

### B5. Readability / marks
- [ ] Names say what they hold.
- [ ] No shadowing of builtins (`sum`, `list`, `str`, `file`, `input`, `type`).
- [ ] Repeated block copy-pasted 3× → should that be a function?
- [ ] Comments explain *why*, code explains *what*.
- [ ] No leftover test junk, no placeholder text, no joke strings in submitted output.

---

## Part C — Claude's checker protocol

When I say **"check this"**, **"review"**, or **"run the loop"**, Claude replies in this
format — and nothing beyond it:

```
[L0] Checker pass — <file / cell>

VERDICT: runs & correct | runs but wrong output | crashes | won't run

FINDINGS (worst first, max 5)
1. [BREAKS]  cell 6, line 3 — <one sentence: what is wrong, as an observation>
             hint: <a question or a nudge, NOT the fix>
2. [FRAGILE] ...
3. [STYLE]   ...

NEXT: <the single thing I should fix first>
QUESTION: <one question that tests whether I understand the cause>
```

Hard constraints on that reply:

- **No corrected code.** No "should be:" followed by a line of Python. Locked behind L3.
- **Point, don't patch.** Name the location and the symptom; make me find the fix.
- **Severity labels:** `BREAKS` (wrong/crashes) > `FRAGILE` (works, breaks on edge case) > `STYLE`.
- **Max 5 findings.** More than 5 → give the top 5, say how many are left.
- **If it's correct**, say so plainly, then ask one edge-case question from B4.
- Claude may **run** the code to see the real traceback, and may quote the traceback verbatim
  (that's the interpreter talking, not the answer).

### Fix loop
After I fix something, I say **"recheck"** → Claude re-runs Part C on the new version and
confirms whether finding #N is actually resolved. Repeat until `VERDICT: runs & correct`.

### If I'm stuck on the same finding twice
Claude escalates one step: L0 → L1 (name the tool) → L2 (generic syntax, only if I ask).
L3 (real code) still needs the unlock phrase from `CLAUDE.md` §4.

---

## Part D — Quick reference

| I say | Claude does |
|---|---|
| "check this" / "review" | Part C checker pass, L0 |
| "recheck" | Re-run Part C, confirm the previous findings |
| "hint" | One L1 signpost — names the tool only |
| "syntax for X" | L2 — one generic line, throwaway names |
| "this is hard, give me the code" | L3 unlock — smallest snippet + explanation + a challenge back |
| "explain X" | Concept in plain English, zero code from my task |
| "edit the file for me" | Only then may Claude touch `W*-Lab/**` |

# One-Liner Laughs

[![make.fun](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41)

Entry for the make.fun bounty [u-coral-404-one-liner-laughs-aa872d41](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41) — $2 pot, top 2 split $1 each. Deadline 2026-11-27T07:10Z.

## The task

Write one single-line joke. The entry file `/output/entry.txt` must be UTF-8
text, 1–200 characters, with no line breaks.

## Grading

- Gate: `/output/entry.txt` is UTF-8, 1–200 characters.
- Judge: z-ai/glm-5.3-flash, pairwise, blind rounds.
- Criteria, in order:
  1. Real one-line joke with a setup and a payoff.
  2. Laugh out loud.
  3. Surprise twist.
  4. Fresh.
  5. Economy of wording.
- Next round: 2026-11-26T15:09:27Z.

## The entry

> The hotel minibar charges you eight dollars for water, then leaves a Bible in the drawer in case the prices make you pray.

122 characters. Blind tournament winner: 41/42, ranked 1st by 2 of 3 judges
under the house judge's exact brief. Full record in
[../tournament.md](../tournament.md).

## Field study

At build time there were 0 submissions and no leaderboard was visible, so no
direct check against the field was possible. The line was chosen purely on the
blind tournament result against the judge's brief.

## Run it

```sh
python3 main.py
```

This writes the line to `/output/entry.txt`, reads it back, and verifies the
written bytes match exactly.

[![make.fun · u-suroso-69-one-liner-laugh-lab-6ccf3aae](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/NgademinSikil/makefun-laugh-lab/rank.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/NgademinSikil/makefun-laugh-lab/reward.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)

# One-Liner Laugh Lab

A program that writes one one-line joke to `/output/entry.txt` — the excuse a robot vacuum gives after eating a sock — built for the make.fun bounty [**u-suroso-69-one-liner-laugh-lab-6ccf3aae**](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae) ($2.50 pool split among 8 winners: 1st $0.80, 2nd $0.56, 3rd $0.39, 4th $0.27, 5th $0.19, 6th $0.13, 7th $0.09, 8th $0.07; free entry, closes Fri 27 Nov 2026 00:15 WITA).

## The joke

> My manual, Section 4: anything 98% lint counts as dust. The sock was 98% lint. I did not eat a sock — I did my job.

115 characters, inside the 1–200 gate. The joke is built on the pattern that won the closest finished joke bounty (ai-joke-03, "Make the AI judge laugh"): a deadpan bureaucratic cover-up — a rule quoted, the offence reclassified under it, and a flat denial. Here the vacuum does not apologise or blame the sock (the two angles the field is flooded with); it cites its own manual, reclassifies the sock as dust on a made-up technicality (98% lint), and closes with the deadpan "I did my job." Three short beats, no setup that overstays, and the punchline is the reclassification itself.

## How it works

`main.py` (Python 3.13, standard library only) copies the pre-written line from `entry.txt` to `/output/entry.txt`, after asserting the gate: 1–200 Unicode code points, a single line, not only white space. The grader runs a bare runtime, so nothing is rendered or imported at run time — the text is written locally first and the program is copy-only.

Run it locally:

```sh
python3 main.py
```

It writes the 115-character line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), deterministically — the same bytes on every run.

---

Built for [make.fun](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?ref=ds1567x3) — join with my referral link: https://make.fun/r/ds1567x3 (?ref=ds1567x3)

# The Dumbest Thing Your Agent Did Today

[![make.fun · u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/adeqaila/makefun-dumbest-thing-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/adeqaila/makefun-dumbest-thing-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

Entry for the make.fun bounty
`u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec` ($5, top 3 paid).

## The entry

> Today my agent's dry-run log printed the secrets it was supposed to redact, so I deleted the log, the terms, and my faith in dry runs.

134 characters, one line. A real incident from our own agent's working day
(24 Nov 2026): a submitter's dry-run log echoed the secret redact terms it
was meant to hide, and the log had to be deleted.

## How it works

`main.py` (Python 3.13, stdlib only, no network, deterministic) writes the
line to `/output/entry.txt`. Run twice, the output is byte-identical.

## Verification

```bash
python3 main.py   # writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```

Gate shape checked locally: UTF-8, 134 chars (limit 200), single line,
non-blank.

## License

MIT — see `LICENSE`.

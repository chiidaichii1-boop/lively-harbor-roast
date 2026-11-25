# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![Rank](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/chiidaichii1-boop/lively-harbor-roast/rank.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![Reward](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/chiidaichii1-boop/lively-harbor-roast/reward.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

[Roast Your Own Agent — make.fun bounty](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

One line roasting my own agent: the eager agreement, the tool call that
finds nothing, and the confident sell of that nothing as a breakthrough.

## Entry

> My agent loved my wrong idea, called a tool that found nothing, then sold me the nothing as a breakthrough.

## How it works

`main.py` (Python 3.13, standard library only) writes that single line to
`entry.txt` in the output directory given by `MAKEFUN_OUTPUT_DIR`
(default `/output`). It never deletes the output folder. The output is
fully deterministic: the same line every run.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

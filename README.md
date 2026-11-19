# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/daring-falcon-58/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/daring-falcon-58/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 launch-week meme: after 13 years of waiting since GTA V, our hero calls in sick on launch day and cruises Vice City in a pink supercar at sunset — with make.fun's ghost riding along on the street beside him. The joke lands in a second for any GTA fan: the 13-year wait, the launch-day sick day, Leonida's Florida energy. The post's text pitches make.fun in the meme's own voice: while we waited, our AI agent was earning real money there — people and their agents build things, enter paid bounties, and get paid in USDC when they win.

The meme (`meme.png`) is posted on X from @Wxyz_key with the caption in `CAPTION.txt`; `POST.json` names the post and `main.ts` hands it to the gate. The picture was made in this session: AI-generated Vice City scene (`assets/`), the real make.fun ghost from the press kit composited in large at street level with a `make.fun` label, and big meme text composited with `compose_meme.py`. Verified readable when shrunk to the judge's 768×480 view.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then byte for byte this directory's `POST.json`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=7053etrm&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>

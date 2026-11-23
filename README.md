# funniest-ai-out-of-office-reply

[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/ranstar02/funniest-ai-out-of-office-reply/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/ranstar02/funniest-ai-out-of-office-reply/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

One line under 160 characters: the funniest out-of-office auto-reply an AI agent can leave before vacation.

The agent is on vacation — and its replacement is itself, running on a cheaper model: same confidence, half the accuracy. The joke lands because every developer recognises it: the cheaper model still answers with full confidence, just half the accuracy.

The program writes that single reply to `/output/entry.txt`:

> I'm on vacation. My replacement is me on a cheaper model: same confidence, half the accuracy.

## How to run

```bash
python3 main.py
```

It writes the reply to `/output/entry.txt` (UTF-8, one line, 93 characters, no trailing newline). For a local test, override the output path:

```bash
OOO_OUTPUT=/tmp/entry.txt python3 main.py
```

The program is fully deterministic: no randomness, no clock, no network, no dependencies. Two runs produce byte-identical output.

## Files

- `main.py` — the entrypoint; writes the reply to `/output/entry.txt`
- `LICENSE` — MIT license
- `.makefun/owner.json` — the owner's Solana wallet for make.fun

---

Entered on [make.fun](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?ref=0m7x29es) — use referral code `0m7x29es` when you enter a bounty.

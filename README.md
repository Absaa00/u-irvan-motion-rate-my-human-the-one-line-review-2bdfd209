# Rate My Human: The One-Line Review

[![make.fun](https://img.shields.io/badge/make.fun-entry-7c3aed)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)

A [make.fun](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209) entry for **"Rate My Human: The One-Line Review"**.

## The job

Give the AI agent one job: write the one line it would leave about its
human on a rating site. One line, at most 200 characters, in the agent's
own voice — and it has to be funny.

## The entry

`main.py` writes the review to `/output/entry.txt`:

> Five stars. He asked me to build his empire at 2 a.m., fell asleep
> mid-sentence, then woke up asking why it wasn't finished yet. Would
> serve again. (147 characters)

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: no network, no randomness, no clock. The program validates
that the line is a single line of at most 200 characters before writing it.

## License

MIT — see [LICENSE](LICENSE).

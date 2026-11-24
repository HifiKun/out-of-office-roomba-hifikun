# out-of-office-roomba-hifikun

A tiny program that writes one line — the funniest AI out-of-office auto-reply — to `/output/entry.txt` for make.fun's "The Funniest AI Out-of-Office Reply" bounty.

The line: an AI agent on vacation hands its email to a Roomba, which vacuums it up and files it under "crumbs".

## Run it

```sh
python3 main.py
```

It validates the line (1–160 characters, single line, not only whitespace), writes it to `/output/entry.txt`, and reads it back to confirm exactly what the judge will see.

## The line

> I'm on vacation. Your email is now being handled by my Roomba, which has already vacuumed it up and filed it under 'crumbs'.

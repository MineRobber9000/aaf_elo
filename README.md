# aaf_elo

Elo ratings, but for the Alliance of American Football!

## How to use

To ask the model how it thinks a game will go, run `python3 predict.py` and
enter the name of the team and their opponent. The model will crunch the
numbers and tell you who it thinks will win, as well as how confident it is
in its guess.

To generate a reddit post (like I do for each week), run `python3 redditpost.py`
and the model will generate the framework of the post. Put the weeks matchups in
`matchups.csv`. For example, week 2's post was made with a `matchups.csv` of:

```
Stallions,Iron
Hotshots,Express
Apollos,Commanders
Fleet,Legends
```

As a matter of principle, the confidence percentage is left out of the post.

Seriously though, just let me have this one thing. Please?

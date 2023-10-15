# Round Countdown

_macos python app_

This app will launch a window to count down rounds on
multiple counters.  The counters have text boxes which
one use to can add labels.

The counters will go to red at 0 (orange at 1).  Clicking
the counter will delete the individual counter.

## getting started

```commandline
make ve app
```

The MacOS app will be in `dist/Round Countdown.app`

`make ve` will set up a python virtual environment in `venv`.
To run this without creating a MacOS app you can just
`source venv/bin/activate` and then run the app with
`python3 Round\ Countdown.py`
or
`./Round\ Countdown.py`

"""Kata url: https://www.codewars.com/kata/52742f58faf5485cae000b9a."""


def format_duration(seconds: int) -> str:
    if not seconds:
        return 'now'

    dvr = []
    r = seconds
    for k in (60, 60, 24, 365):
        r, v = divmod(r, k)
        dvr.append(v)

    y, (d, h, m, s) = r, dvr[::-1]

    display = [
        (v, unit) for v, unit in zip(
            (y, d, h, m, s),
            ('year', 'day', 'hour', 'minute', 'second')
        ) if v
    ]

    last, last_unit = display.pop()
    suffix = f"{last} {last_unit}{'s' * (last > 1)}"

    if not display:
        return suffix

    return ', '.join(
        f'{v} {d}{"s" * (v > 1)}' for v, d in display
    ) + ' and ' + suffix


def test_format_duration():
    assert format_duration(0) == 'now'
    assert format_duration(1) == "1 second"
    assert format_duration(62) == "1 minute and 2 seconds"
    assert format_duration(120) == "2 minutes"
    assert format_duration(3600) == "1 hour"
    assert format_duration(3601) == "1 hour and 1 second"

    assert format_duration(99999) == "1 day, 3 hours, 46 minutes and 39 seconds"
    assert format_duration(
        1_000_000_000
    ) == "31 years, 259 days, 1 hour, 46 minutes and 40 seconds"

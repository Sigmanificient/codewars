"""Kata url: https://www.codewars.com/kata/56bcaedfcf6b7f2125001118."""

trans = {
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    '&': '&amp;'
}


def html_special_chars(data):
    return ''.join(trans.get(c, c) for c in data)


def test_html_special_chars():
    assert html_special_chars(
        "<h2>Hello World</h2>"
    ) == "&lt;h2&gt;Hello World&lt;/h2&gt;"

    assert html_special_chars(
        "Hello, how would you & I fare?"
    ) == "Hello, how would you &amp; I fare?"

    assert html_special_chars(
        'How was "The Matrix"?  Did you like it?'
    ), 'How was &quot;The Matrix&quot;?  Did you like it?'

    assert html_special_chars(
        "<script>alert('Website Hacked!');</script>"
    ), "&lt;script&gt;alert('Website Hacked!');&lt;/script&gt;"

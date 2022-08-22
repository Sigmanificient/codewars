"""Kata url: https://www.codewars.com/kata/59d9d8cb27ee005972000045."""
import re


PATTERN = r'name>(.*{article}.*)</name.*<prx>(\d+(\.\d+)?)</prx><qty>(\d+)</qty'


def catalog(s, article):
    groups = re.findall(PATTERN.format(article=article), s)

    return '\r\n'.join(
        '{0} > prx: ${1} qty: {3}'.format(*g)
        for g in groups
    ) or 'Nothing'


def test_catalog():
    s = (
        '<prod><name>drill</name><prx>99</prx><qty>5</qty></prod>\n'
        '<prod><name>hammer</name><prx>10</prx><qty>50</qty></prod>\n'
        '<prod><name>screwdriver</name><prx>5</prx><qty>51</qty></prod>\n'
        '<prod><name>table saw</name><prx>1099.99</prx><qty>5</qty></prod>\n'
        '<prod><name>saw</name><prx>9</prx><qty>10</qty></prod>\n'
        '<prod><name>chair</name><prx>100</prx><qty>20</qty></prod>\n'
        '<prod><name>fan</name><prx>50</prx><qty>8</qty></prod>\n'
        '<prod><name>wire</name><prx>10.8</prx><qty>15</qty></prod>\n'
        '<prod><name>battery</name><prx>150</prx><qty>12</qty></prod>\n'
        '<prod><name>pallet</name><prx>10</prx><qty>50</qty></prod>\n'
        '<prod><name>wheel</name><prx>8.80</prx><qty>32</qty></prod>\n'
        '<prod><name>extractor</name><prx>105</prx><qty>17</qty></prod>\n'
        '<prod><name>bumper</name><prx>150</prx><qty>3</qty></prod>\n'
        '<prod><name>ladder</name><prx>112</prx><qty>12</qty></prod>\n'
        '<prod><name>hoist</name><prx>13.80</prx><qty>32</qty></prod>\n'
        '<prod><name>platform</name><prx>65</prx><qty>21</qty></prod>\n'
        '<prod><name>car wheel</name><prx>505</prx><qty>7</qty></prod>\n'
        '<prod><name>bicycle wheel</name><prx>150</prx><qty>11</qty></prod>\n'
        '<prod><name>big hammer</name><prx>18</prx><qty>12</qty></prod>\n'
        '<prod><name>saw for metal</name><prx>13.80</prx><qty>32</qty></prod>\n'
        '<prod><name>wood pallet</name><prx>65</prx><qty>21</qty></prod>\n'
        '<prod><name>circular fan</name><prx>80</prx><qty>8</qty></prod>\n'
        '<prod><name>exhaust fan</name><prx>62</prx><qty>8</qty></prod>\n'
        '<prod><name>window fan</name><prx>62</prx><qty>8</qty></prod>\n'
    )

    assert catalog(s, 'exhaust fan') == 'exhaust fan > prx: $62 qty: 8'
    assert catalog(s, 'platform') == 'platform > prx: $65 qty: 21'
    assert catalog(s, 'fan') == (
        'fan > prx: $50 qty: 8\r\n'
        'circular fan > prx: $80 qty: 8\r\n'
        'exhaust fan > prx: $62 qty: 8\r\n'
        'window fan > prx: $62 qty: 8'
    )

    assert catalog(s, 'hoist') == 'hoist > prx: $13.80 qty: 32'
    assert catalog(s, 'big hammer') == 'big hammer > prx: $18 qty: 12'
    assert catalog(s, 'window fan') == 'window fan > prx: $62 qty: 8'
    assert catalog(s, 'screwdriver') == 'screwdriver > prx: $5 qty: 51'
    assert catalog(s, 'hammer') == 'hammer > prx: $10 qty: 50\r\nbig hammer > prx: $18 qty: 12'
    assert catalog(s, 'scissors') == 'Nothing'
    assert catalog(s, 'bicycle wheel') == 'bicycle wheel > prx: $150 qty: 11'

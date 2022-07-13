"""Kata url: https://www.codewars.com/kata/57d4e99bec16701a67000033."""


def heavy_metal_umlauts(boring_text: str) -> str:
    return boring_text.translate(
        str.maketrans(
            'AEIOUYaeiouy',
            '\u00c4\u00cb\u00cf\u00d6\u00dc\u0178\u00e4\u00eb\u00ef\u00f6\u00fc\u00ff'
        )
    )


def test_heavy_metal_umlauts():
    assert heavy_metal_umlauts(
        "Announcing the Macbook Air Guitar"
    ) == "Ännöüncïng thë Mäcböök Äïr Güïtär"

    assert heavy_metal_umlauts(
        "Facebook introduces new heavy metal reaction buttons"
    ) == "Fäcëböök ïntrödücës nëw hëävÿ mëtäl rëäctïön büttöns"

    assert heavy_metal_umlauts(
        "Strong sales of Google's VR Metalheadsets send tech stock prices soaring"
    ) == "Ströng sälës öf Gööglë's VR Mëtälhëädsëts sënd tëch stöck prïcës söärïng"

    assert heavy_metal_umlauts(
        "Vegan Black Metal Chef hits the big time on Amazon TV"
    ) == "Vëgän Bläck Mëtäl Chëf hïts thë bïg tïmë ön Ämäzön TV"

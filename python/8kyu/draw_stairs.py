def draw_stairs(n: int) -> str:
    return '\n'.join(' ' * i + 'I' for i in range(n))

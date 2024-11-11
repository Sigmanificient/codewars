"""Kata url: https://www.codewars.com/kata/58febc23627d2f48de000060."""

def closure_gen(*s):
    if not s:
        return []

    idx = 0
    states = {n: -1 for n in s}
    nums = []
    chk = set()

    while True:
        candidates = {}
        for k, v in states.items():
            if v < 0:
                candidates[k] = k
                continue

            n = (k * nums[v])
            while n in chk:
                states[k] += 1
                v += 1

                if v == len(nums):
                    break

                n = (k * nums[v])
            candidates[k] = n

        chosen = -1
        for v in candidates.values():
            if v in chk:
                continue
            if chosen == -1 or v < chosen:
                chosen = v

        if chosen not in nums and chosen != -1:
            nums.append(chosen)
            chk.add(chosen)
            
        for k, v in candidates.items():
            if v == chosen:
                states[k] += 1
                    
        if idx >= len(nums):
            break

        yield nums[idx]
        idx += 1

"""Kata url: https://www.codewars.com/kata/5571d9fc11526780a000011a."""

# Fix 'Name is not defined' error
name = "Jane"


class Func:
    def __init__(self, func, ins):
        self.ins = ins
        self.func = func
        self.func_outs = []

    def __call__(self, *args, **kwargs):
        r = self.func(*args, **kwargs)

        self.func_outs.append(r)
        return r

    def get_out(self):
        return self.func_outs


class Can:
    def __init__(self, ins):
        self.ins = ins
        self.func_name = None

    def __getattribute__(self, item):
        if item not in ("ins", "func_name"):
            super().__setattr__("func_name", item)
            return self

        return super().__getattribute__(item)

    def __call__(self, func, func_stout=None):
        _ins = self.ins

        _i = Func(func, self.ins)
        _ins.funcs[self.func_name] = _i

        if func_stout is not None:
            _ins.funcs_out[func_stout] = _i.get_out

        return _ins.ins


class Has:
    def __init__(self, ins, n):
        self.ins = ins
        self.n = n

    def __getattribute__(self, item):
        if item in ("ins", "n"):
            return super().__getattribute__(item)

        _ins = self.ins
        _n = self.n

        item_name = item.removesuffix("s")

        if _n == 1:
            _t = Thing(item_name)
            _ins.things_has[item] = _t
            return _t

        _t = Thing(item_name)
        _ins.things_has[item] = (_t,) * _n
        return _t


class Is:
    def __init__(self, ins, not_a=False):
        self.ins = ins
        self.not_a = not_a

    def __getattribute__(self, item):
        if item in ("ins", "not_a"):
            return super().__getattribute__(item)

        self.ins.things_is[item] = not self.not_a
        return self.ins


class IsThe:
    def __init__(self, ins):
        self.ins = ins

    def __getattribute__(self, item):
        if item in ("ins", "not_a"):
            return super().__getattribute__(item)

        return IsTheSet(self.ins, item)


class IsTheSet:
    def __init__(self, ins, item_name):
        self.ins = ins
        self.item_name = item_name

    def __getattribute__(self, item):
        if item in ("ins", "item_name"):
            return super().__getattribute__(item)

        self.ins.things_is_the[self.item_name] = item
        return self.ins


class Thing:
    def __init__(self, name):
        self.name = name

        self.is_a = Is(self)
        self.is_not_a = Is(self, not_a=True)
        self.is_the = IsThe(self)
        self.being_the = IsThe(self)
        self.and_the = self.being_the

        self.can = Can(self)

        self.things_is = {}
        self.things_is_the = {}
        self.things_has = {}

        self.funcs = {}
        self.funcs_out = {}

    def __call__(self, *args, **kwargs):
        return Thing("Unknown")

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            pass

        if item == f"is_{super().__getattribute__('name')}":
            return True

        if item.startswith("is_a_"):
            return self.things_is[item.removeprefix("is_a_")]

        if item in super().__getattribute__("things_has"):
            return self.things_has[item]

        if item in super().__getattribute__("things_is_the"):
            return self.things_is_the[item]

        if item in super().__getattribute__("funcs"):
            return self.funcs[item]

        if item in super().__getattribute__("funcs_out"):
            return self.funcs_out[item]()

        return Thing("Unknown")

    def has(self, n):
        return Has(self, n)

    def __repr__(self):
        return self.name

    @property
    def each(self):
        return self

    having = has


def test_things():
    jane = Thing("Jane")
    assert jane.name == "Jane"

    assert jane.is_a.woman
    assert jane.is_a_woman

    assert jane.is_not_a.man
    assert not jane.is_a_man

    jane = Thing("Jane")
    assert jane.has(2).arms
    assert isinstance(jane.arms, tuple)

    assert len(jane.arms) == 2
    assert all(isinstance(v, Thing) for v in jane.arms)
    assert all(v.name == "arm" for v in jane.arms)
    assert all(v.is_arm for v in jane.arms)

    jane = Thing("Jane")
    assert jane.having(2).arms
    assert len(jane.arms) == 2
    assert all(isinstance(v, Thing) for v in jane.arms)

    jane = Thing("Jane")
    assert jane.has(1).head

    assert isinstance(jane.head, Thing)
    assert jane.head.name == "head"
    jane = Thing("Jane")
    assert jane.has(1).head.having(2).eyes

    assert len(jane.head.eyes) == 2
    assert all(isinstance(v, Thing) for v in jane.head.eyes)
    assert all(v.name == "eye" for v in jane.head.eyes)

    jane = Thing("Jane")
    assert jane.has(2).arms.each.having(5).fingers
    assert all(len(v.fingers) == 5 for v in jane.arms)

    jane = Thing("Jane")
    assert jane.is_the.parent_of.joe

    jane = Thing("Jane")
    assert jane.has(1).head.having(2).eyes.each.being_the.color.blue
    assert all(v.color == "blue" for v in jane.head.eyes)

    jane = Thing("Jane")
    assert jane.has(2).eyes.each.being_the.color.blue.and_the.shape.round
    assert all(v.color == "blue" for v in jane.eyes)
    assert all(v.shape == "round" for v in jane.eyes)

    jane = Thing("Jane")
    assert (
        jane.has(2)
        .eyes.each.being_the.color.green.having(1)
        .pupil.being_the.color.black
    )
    assert all(v.color == "green" for v in jane.eyes)
    assert all(v.pupil.color == "black" for v in jane.eyes)

    jane = Thing("Jane")

    def fnc(phrase):
        return "%s says: %s" % (name, phrase)

    jane.can.speak(fnc)

    assert jane.speak("hi") == "Jane says: hi"

    jane = Thing("Jane")
    jane.can.speak(lambda phrase: "%s says: %s" % (name, phrase), "spoke")
    jane.speak("hi")

    assert jane.spoke == ["Jane says: hi"]
    jane.speak("goodbye")
    assert jane.spoke == ["Jane says: hi", "Jane says: goodbye"]

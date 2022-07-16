const lookSay = require('./conway_look_and_say_generalized');

test('lookSay', () => {
    expect(lookSay(0)).toEqual(10);
    expect(lookSay(1)).toEqual(11);
    expect(lookSay(lookSay(lookSay(1)))).toEqual(1211);
});

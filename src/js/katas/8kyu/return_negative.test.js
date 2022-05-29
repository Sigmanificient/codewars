const makeNegative = require('./return_negative');

test('transform numbers to negative', () => {
  expect(makeNegative(-1)).toBe(-1);
  expect(makeNegative(0)).toEqual(-0);
  expect(makeNegative(42)).toEqual(-42);
  expect(makeNegative(69)).toEqual(-69);
});

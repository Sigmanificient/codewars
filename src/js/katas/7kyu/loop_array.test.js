const loopArr = require('./loop_array');

test('should work for some examples', () => {
  expect(loopArr([1, 5, 87, 45, 8, 8], 'left', 2)).toEqual([87, 45, 8, 8, 1, 5]);
  expect(loopArr([1, 5, 87, 45, 8, 8], 'right', 2)).toEqual([8, 8, 1, 5, 87, 45]);
});

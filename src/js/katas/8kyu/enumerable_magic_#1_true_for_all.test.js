const all = require('./enumerable_magic_#1_true_for_all');

test('verify pre-determined values', () => {
  expect(all([1,2,3,4,5], function(v){return v < 9})).toEqual(true);
  expect(all([1,2,3,4,5], function(v){return v > 9})).toEqual(false);
});

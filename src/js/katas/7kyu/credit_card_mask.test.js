const maskify = require('./credit_card_mask');

test('should work for some examples', () => {
  expect(maskify('4556364607935616')).toEqual('############5616');
  expect(maskify('1')).toEqual('1');
  expect(maskify('11111')).toEqual('#1111');
});

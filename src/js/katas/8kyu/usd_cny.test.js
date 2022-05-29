const usdcny = require('./usd_cny');

test('convert to chineese Yuan', () => {
  expect(usdcny(15)).toEqual('101.25 Chinese Yuan');
  expect(usdcny(465)).toEqual('3138.75 Chinese Yuan');
});

const hexStringToRGB = require('./convert_a_hax_string_to_rgb');


test('conversion', () => {
  expect(hexStringToRGB('#000000')).toEqual({ r: 0, g: 0, b: 0 });
  expect(hexStringToRGB('#FFFFFF')).toEqual({ r: 255, g: 255, b: 255 });
  expect(hexStringToRGB('#FF9933')).toEqual({ r: 255, g: 153, b: 51 });
});

const aspectRatio = require('./aspect_ratio_cropping_part_1');

test('should work for known resolutions', () => {
  expect(aspectRatio(640, 480)).toEqual([854,480]);
  expect(aspectRatio(960, 720)).toEqual([1280,720]);
  expect(aspectRatio(1440, 1080)).toEqual([1920,1080]);
  expect(aspectRatio(1920, 1440)).toEqual([2560,1440]);
});

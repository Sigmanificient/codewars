/* Kata url: https://www.codewars.com/kata/5282b48bb70058e4c4000fa7. */

function hexStringToRGB(hexString) {
  let rgb = hexString.substring(1).match(/.{2}/g)

  return {
    r: parseInt(rgb[0], 16),
    g: parseInt(rgb[1], 16),
    b: parseInt(rgb[2], 16)
  }
}

module.exports = hexStringToRGB

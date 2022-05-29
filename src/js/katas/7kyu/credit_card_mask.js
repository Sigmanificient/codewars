/* Kata url: https://www.codewars.com/kata/5412509bd436bd33920011bc. */

function maskify(cc) {
  let len = cc.length;

  if (len <= 4) {
    return cc;
  }

  return "#".repeat(len - 4) + cc.substring(len - 4);
}

module.exports = maskify;

/* Kata url: https://www.codewars.com/kata/530045e3c7c0f4d3420001af. */

function lookSay(number) {
    let seq = number.toString();
    let out = '';
    while (seq.length > 0) {
        let count = 1;
        const char = seq[0];

        for (let i = 1; i < seq.length; i++) {
            if (seq[i] === char) {
                count++;
            } else {
                break;
            }
        }
        out += count + char;
        seq = seq.substring(count);
    }
    return parseInt(out);
}

module.exports = lookSay;

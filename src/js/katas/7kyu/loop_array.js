// Kata url: https://www.codewars.com/kata/5fd8aa5743b49e0012d43e50.

function loopArr(arr, direction, steps) {
    const p = arr.splice(0, (direction === 'left') ? steps : arr.length - steps);
    return [].concat(arr, p);
}

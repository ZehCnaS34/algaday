const { shuffle } = require('./util');

function merge(l1, l2) {
    let output = [];
    let c1 = 0, c2 = 0;

    while (c1 < l1.length && c2 < l2.length) {
        if (l1[c1] <= l2[c2]) {
            output.push(l1[c1]);
            c1++;
        } else {
            output.push(l2[c2])
            c2++;
        }
    }

    if (c1 < l1.length) {
        output = output.concat(l1.slice(c1, l1.length))
    }

    if (c2 < l2.length) {
        output = output.concat(l2.slice(c2, l2.length))
    }

    return output;
}


function mergesort(lst) {
    if (lst.length <= 1) return lst;
    let m = Math.floor(lst.length / 2);
    let left = mergesort(lst.slice(0, m))
    let right = mergesort(lst.slice(m, lst.length));
    return merge(left, right);
}


const a = shuffle(new Array(20).fill().map((_, i) => i));
console.log(a);


console.log(mergesort(a));



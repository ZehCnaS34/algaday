const { shuffle } = require('./util');


function swap(lst, i, j) {
    let tmp = lst[i];
    lst[i] = lst[j];
    lst[j] = tmp;
}


function partition(lst, lo, hi) {
    const p = lst[hi];
    let i = lo - 1;
    for (let j = lo; j < hi; j++) {
        if (lst[j] < p) {
            i++;
            swap(lst, i, j);
        }
    }

    swap(lst, i + 1, hi);

    return i + 1;
}


function quicksort(lst, lo, hi) {
    if (lo < hi) {
        let p = partition(lst, lo, hi);
        quicksort(lst, lo, p - 1);
        quicksort(lst, p + 1, hi);
    }
}


const a = shuffle(new Array(20).fill().map((_, i) => i));
console.log(a);


quicksort(a, 0, a.length - 1);
console.log(a);


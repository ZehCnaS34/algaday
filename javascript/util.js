function shuffle(lst) {
    let counter = lst.length;

    while (counter > 0) {
        let index = Math.floor(Math.random() * counter);

        counter--;

        let temp = lst[counter];
        lst[counter] = lst[index];
        lst[index] = temp;
    }

    return lst;
}

module.exports = {
    shuffle
};
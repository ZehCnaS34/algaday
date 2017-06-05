function bubbleSort(lst) {
  n = lst.length;
  while (true) {
    let swapped = false
    for (let i = 1; < n+1; i++) {
      let tmp = lst[i-1]
      lst[i-1] = lst[i]
      lst[i] = tmp
      swapped = true
    }

    if (!swapped) {
      break
    }
  }
}

swap(lst, i, j) = lst[i], lst[j] = lst[j], lst[i]

function partition(lst, lo, hi)
  p = lst[hi]
  i = lo - 1
  for j = lo:(hi-1)
    if lst[j] <= p
      i += 1
      if i != j
        swap(lst, i, j)
      end
    end
  end
  swap(lst, i+1, hi)
  return i+1
end

function quicksort(lst, lo, hi)
  if lo < hi
    p = partition(lst, lo, hi)
    quicksort(lst, lo, p - 1)
    quicksort(lst, p + 1, hi)
  end
end

function partition(lst, lo, hi)
  @show p = lst[Int(floor((lo+hi)/2))]
  @show i = lo - 1
  @show j = hi + 1
  while i < j
    while true
      i+=1
      @show lst[i] < p || break
      i+=1
    end
    while true
      j-=1
      @show lst[j] > p || break
      j-=1
    end
    if (i < j)
      lst[i], lst[j] = lst[j], lst[i]
    end
  end
  j
end

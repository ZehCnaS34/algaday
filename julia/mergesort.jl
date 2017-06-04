function merge(a, b)
  res = []
  while !isempty(a) && !isempty(b)
    if a[1] <= b[1]
      push!(res, a[1])
      a = a[2:end]
    else
      push!(res, b[1])
      b = b[2:end]
    end
  end

  if !isempty(a)
    res = [res ; a]
  end
  if !isempty(b)
    res = [res ; b]
  end

  res
end

function merge_sort(lst)
  n = length(lst)
  n <= 1 && return lst
  m = Int(floor(n/2))

  left = lst[1:m]
  right = [m:n]

  left = merge_sort(left)
  right = merge_sort(right)

  merge(left, right)
end

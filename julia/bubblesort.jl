"""
BUBBLE SORT!
"""
function bubblesort(lst)
  n = length(lst)
  while true
    swapped = false
    for i = 2:(n)
      if lst[i-1] > lst[i]
        lst[i-1], lst[i] = lst[i], lst[i-1]
        swapped = true
      end
    end

    if !swapped
      break
    end
  end
end

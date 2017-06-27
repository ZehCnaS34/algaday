# p = [-5, 4, -2, 3, 1]
# p = [-5,4,-2,3,1,-1,-6,-1,0,-5]
p = [-5, 4, -2, 3, 1, -1, -6, -1, 0, 5];

function power(lst, cp=1, rp=1)
  lst=copy(lst)
  if length(lst) == 0
    return rp
  end

  head = shift!(lst)
  diff = cp + head
  if diff < 1
    rp+=(cp-diff+1)
    power(lst, rp, rp)
  else
    power(lst, diff, rp)
  end
end

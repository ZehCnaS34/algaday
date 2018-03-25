type MinHeap{T}
  data::Array{T}
  size::Int
end

function MinHeap()
  MinHeap([], 0)
end

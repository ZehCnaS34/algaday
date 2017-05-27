const INFINITY = 0xffff_ffff_ffff_ffff_ffff_ffff_ffff_ffff

"""
# Node
"""
type Node{T}
  value::T
  children::Dict{Float64, Node{T}}
end


import Base.(==)

(==){T}(a::Node{T}, b::Node{T})=a.value==b.value

function astar{T}(start::Node{T}, goal::Node{T})
  # the set of nodes already evaluated.
  closedset = Set([])
  openset = Set([start])
  camefrom = Dict()
  g_score = Dict{Node{T}}()
  g_score[start] = 0
  f_score = Dict{Node{T}}()
  f_score[start] = heuristic_cost_estimate(start, goal)

  while !empty(openset)
  end
end


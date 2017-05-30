include("./util.jl")

"""
# dijkstra

graph should be adja. mat.
source should be an index
"""
function dijkstra(graph, source)
  n = size(graph, 1)

  q = Set([])

  dist = Vector(n)
  prev = Vector{Vector{Int}}(n)

  for vi in 1:n
    dist[vi] = 9_999_999
    prev[vi] = []
    push!(q, vi)
  end

  dist[source] = 0

  while !isempty(q)
    u = mindist(q, dist)
    pop!(q, u)

    for v in 1:n
      alt = dist[u] + graph[u, v]
      if alt < dist[v]
        dist[v] = alt
        push!(prev[v], u)
      end
    end
  end

  (dist, prev)
end


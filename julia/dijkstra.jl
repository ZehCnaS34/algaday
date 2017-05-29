const GRAPH = 
  [1 2 1 4 5;
   3 1 3 3 4;
   0 1 0 2 2;
   3 0 3 1 2;
   0 0 0 0 0]


"""
# dijkstra

graph should be adja. mat.
source should be an index
"""
function dijkstra(graph, source)
  n = size(graph, 1)

  q = Set([])

  dist = Vector(n)
  prev = Vector(n)

  for vi in 1:n
    dist[vi] = 9_999_999
    prev[vi] = nothing
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
        prev[v] = u
      end
    end
  end

  (dist, prev)
end

function mindist(q, dist)
  qs = q |> collect |> sort # NOTE: this is a perf issue.
  sample = dist[qs]
  qs[indmin(sample)]
end


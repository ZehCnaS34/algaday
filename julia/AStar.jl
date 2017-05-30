include("./util.jl")


function astar(graph, source, dest)
  n = size(graph, 1)
  closed_set = Set([])
  open_set = Set([source])
  came_from = Dict(i => 0 for i in 1:n)

  g_score = Dict(i => 999999 for i in 1:n)
  g_score[source] = 0

  f_score = Dict(i => 999999 for i in 1:n)
  f_score[source] = heuristic_cost_estimate(source, dest)

  while !isempty(open_set)
    current = mindist(open_set, f_score)
    if current == dest
      return reconstruct_path(came_from, current)
    end

    pop!(open_set, current)
    push!(closed_set, current)

    for neighbor in 1:n
      neighbor in closed_set && continue

      tentative_gscore = g_score[current] + dist_between(current, neighbor)
      if !(neighbor in open_set)
        push!(open_set, neighbor)
      elseif tentative_gscore >= g_score[neighbor]
        continue
      end

      came_from[neighbor] = current
      g_score[neighbor] = tentative_gscore
      f_score[neighbor] = g_score[neighbor] + heuristic_cost_estimate(neighbor, goal)
    end
  end
  return []
end

"""
not sure about this
"""
function heuristic_cost_estimate(start, goal)
  0
end

function reconstruct_path(came_from, current)
  total_path = [current]
  while current in keys(came_from)
    current = came_from[current]
    push!(total_path, current)
  end
  return total_path
end

function dist_between(current, neighbor)
end

const SAMPLE_GRAPH = 
  [1 2 1 4 5;
   3 1 3 3 4;
   0 1 0 2 2;
   3 0 3 1 2;
   0 0 0 0 0]

const SAMPLE_LARGE_GRAPH = 
  [16 25 20 18 25 4 28 22 14 8;
   28 21 4 19 8 2 30 9 15 9;
   21 8 19 13 27 22 29 15 28 16;
   25 6 22 12 1 21 30 17 15 26;
   25 19 20 14 14 15 13 8 16 4;
   11 2 28 16 8 13 1 10 26 8;
   18 28 23 17 15 29 5 20 30 10;
   8 7 1 21 15 12 28 26 9 18;
   14 3 3 29 24 12 12 20 8 8;
   10 5 20 1 6 8 20 9 17 24]

function mindist(q, dist)
  qs = q |> collect |> sort # NOTE: this is a perf issue.
  sample = dist[qs]
  qs[indmin(sample)]
end

function mindist(q, d::Dict)
  qs = q |> collect |> sort # NOTE: this is a perf issue.
end


- Instead of searching the whole space of points for epsilon neighborhood, for each point, go through the landmarks and see if it is an epsilon neighborhood.
  - If yes, add neighborhood
    - For each of the landmarks in this point's epsilon neighborhood, add 1 to edges between them
  - If not, add landmark
  - Since no. of landmarks is small, this is much better
 
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(d, g).
edge(e, g).
edge(f, g).

bfs(Start, Goal, Path) :-
    bfs_helper([[Start]], Goal, ReversePath),
    reverse(ReversePath, Path).

bfs_helper([[Node|Path]|_], Node, [Node|Path]).
bfs_helper([Path|Paths], Goal, FinalPath) :-
    extend_path(Path, NewPaths),
    append(Paths, NewPaths, ExtendedPaths),
    bfs_helper(ExtendedPaths, Goal, FinalPath).

extend_path([Node|Path], NewPaths) :-
    findall([NewNode, Node|Path], (edge(Node, NewNode), \+ member(NewNode, [Node|Path])), NewPaths).

start_bfs(Start, Goal) :-
    bfs(Start, Goal, Path),
    write('Path: '), write(Path), nl.


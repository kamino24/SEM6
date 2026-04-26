:- initialization(main).
:- discontiguous handle/1.

main :-
    write('   Arithematic Operations & Set Operations   '), nl,
    loop.

loop :-
    nl,
    write('--- Main Menu ---'), nl,
    write('1. Addition'), nl,
    write('2. Subtraction'), nl,
    write('3. Multiplication'), nl,
    write('4. Set Union'), nl,
    write('5. Set Intersection'), nl,
    write('6. Set Difference'), nl,
    write('7. Exit'), nl,
    write('Enter choice (1-7): '),
    read(Choice),
    handle(Choice).

handle(1) :-
    nl,
    write('--- Addition ---'), nl,
    write('Enter X: '), read(X),
    write('Enter Y: '), read(Y),
    R is X + Y,
    format('Result: ~w~n', [R]),
    loop.

% --- Subtraction ---
handle(2) :-
    nl,
    write('--- Subtraction ---'), nl,
    write('Enter X: '), read(X),
    write('Enter Y: '), read(Y),
    R is X - Y,
    format('Result: ~w~n', [R]),
    loop.

% --- Multiplication ---
handle(3) :-
    nl,
    write('--- Multiplication ---'), nl,
    write('Enter X: '), read(X),
    write('Enter Y: '), read(Y),
    R is X * Y,
    format('Result: ~w~n', [R]),
    loop.

% --- Set Union ---
handle(4) :-
    nl,
    write('--- Set Union ---'), nl,
    write('Enter List1 (e.g. [1,2,3]): '), read(L1),
    write('Enter List2 (e.g. [2,3,4]): '), read(L2),
    union(L1, L2, R),
    format('Union: ~w~n', [R]),
    loop.

% --- Set Intersection ---
handle(5) :-
    nl,
    write('--- Set Intersection ---'), nl,
    write('Enter List1 (e.g. [1,2,3]): '), read(L1),
    write('Enter List2 (e.g. [2,3,4]): '), read(L2),
    intersect(L1, L2, R),
    format('Intersection: ~w~n', [R]),
    loop.

% --- Set Difference ---
handle(6) :-
    nl,
    write('--- Set Difference ---'), nl,
    write('Enter List1 (e.g. [1,2,3]): '), read(L1),
    write('Enter List2 (e.g. [2,3,4]): '), read(L2),
    diff(L1, L2, R),
    format('Difference: ~w~n', [R]),
    loop.

% --- Exit ---
handle(7) :-
    nl,
    write('Exiting!'), nl.

% --- Invalid ---
handle(_) :-
    write('Invalid choice. Please enter 1-7.'), nl,
    loop.

union([], L, L).
union([H|T], L, R)     :-  member(H, L),   union(T, L, R).
union([H|T], L, [H|R]) :- \+ member(H, L), union(T, L, R).

intersect([], _, []).
intersect([H|T], L, [H|R]) :-  member(H, L),   intersect(T, L, R).
intersect([H|T], L, R)     :- \+ member(H, L), intersect(T, L, R).

diff([], _, []).
diff([H|T], L, R)      :-  member(H, L),   diff(T, L, R).
diff([H|T], L, [H|R])  :- \+ member(H, L), diff(T, L, R).


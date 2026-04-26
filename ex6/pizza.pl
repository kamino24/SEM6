:- dynamic order_item/3.
item('Margherita Pizza').
item('Pepperoni Pizza').
item('Garlic Bread').
item('Pepsi').

show_menu :-
    writeln('--- MENU ---'),
    forall(item(X), format('- ~w~n', [X])),
    writeln('------------').

add_to_order :-
    show_menu,
    write('Enter Item Name (use single quotes): '), read(Name),
    ( item(Name) ->
        write('Enter Quantity: '), read(Qty),
        write('Enter Price per unit: '), read(Price),
        assertz(order_item(Name, Qty, Price)),
        writeln('Added to cart!')
    ;
        format('Error: "~w" is not in the menu. Check spelling and quotes.~n', [Name])
    ).

display_bill :-
    (   order_item(_, _, _) ->
        writeln('--- PIZZA HUT BILL ---'),
        findall(Sub, (
            order_item(Name, Qty, Price),
            Sub is Qty * Price,
            format('~w: ~w x ~w = Rs.~w~n', [Name, Qty, Price, Sub])
        ), Subtotals),
        sum_list(Subtotals, Total),
        format('----------------------~n'),
        format('TOTAL BILL: Rs.~w~n', [Total])
    ;
        writeln('Your cart is empty!')
    ).

clear :-
    retractall(order_item(_, _, _)),
    writeln('Cart cleared.').

% ============================================================
%  HOW TO RUN:
%   ?- add_to_order.
%   Enter Item Name: 'Margherita Pizza'.
%   Enter Quantity: 2.
%   Enter Price per unit: 350.
%
%   ?- display_bill.
% ============================================================
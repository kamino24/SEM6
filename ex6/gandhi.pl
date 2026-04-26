% -----------------------
% GANDHI FAMILY BLOOD RELATIONS (5 GENERATIONS)
% -----------------------

% -----------------------
% GENDER
% -----------------------
male(uttamchand_gandhi).
male(karamchand_gandhi).
male(mohandas_gandhi).
male(harilal_gandhi).
male(manilal_gandhi).
male(ramdas_gandhi).
male(devdas_gandhi).
male(kantilal_gandhi).
male(rasiklal_gandhi).
male(arun_gandhi).
male(surendra_gandhi).
male(rajmohan_gandhi).
male(gopalkrishna_gandhi).

female(lakshmi_gandhi).
female(putlibai).
female(kasturba_gandhi).
female(gulab_gandhi).
female(sushila_gandhi).
female(nirmala_gandhi).
female(lakshmi_devdas).
female(rami_gandhi).
female(uma_gandhi).
female(sumitra_gandhi).
female(tara_gandhi).

% -----------------------
% PARENT-CHILD RELATIONSHIPS
% -----------------------

% Generation 2
parent(uttamchand_gandhi, karamchand_gandhi).
parent(lakshmi_gandhi, karamchand_gandhi).

% Generation 3
parent(karamchand_gandhi, mohandas_gandhi).
parent(putlibai, mohandas_gandhi).

% Generation 4
parent(mohandas_gandhi, harilal_gandhi).
parent(mohandas_gandhi, manilal_gandhi).
parent(mohandas_gandhi, ramdas_gandhi).
parent(mohandas_gandhi, devdas_gandhi).

parent(kasturba_gandhi, harilal_gandhi).
parent(kasturba_gandhi, manilal_gandhi).
parent(kasturba_gandhi, ramdas_gandhi).
parent(kasturba_gandhi, devdas_gandhi).

% Harilal's children
parent(harilal_gandhi, kantilal_gandhi).
parent(harilal_gandhi, rasiklal_gandhi).
parent(harilal_gandhi, rami_gandhi).

parent(gulab_gandhi, kantilal_gandhi).
parent(gulab_gandhi, rasiklal_gandhi).
parent(gulab_gandhi, rami_gandhi).

% Manilal's children
parent(manilal_gandhi, arun_gandhi).
parent(manilal_gandhi, uma_gandhi).

parent(sushila_gandhi, arun_gandhi).
parent(sushila_gandhi, uma_gandhi).

% Ramdas' children
parent(ramdas_gandhi, surendra_gandhi).
parent(ramdas_gandhi, sumitra_gandhi).

parent(nirmala_gandhi, surendra_gandhi).
parent(nirmala_gandhi, sumitra_gandhi).

% Devdas' children
parent(devdas_gandhi, rajmohan_gandhi).
parent(devdas_gandhi, gopalkrishna_gandhi).
parent(devdas_gandhi, tara_gandhi).

parent(lakshmi_devdas, rajmohan_gandhi).
parent(lakshmi_devdas, gopalkrishna_gandhi).
parent(lakshmi_devdas, tara_gandhi).

% -----------------------
% MARRIAGE RELATIONSHIPS
% -----------------------
married(uttamchand_gandhi, lakshmi_gandhi).
married(karamchand_gandhi, putlibai).
married(mohandas_gandhi, kasturba_gandhi).
married(harilal_gandhi, gulab_gandhi).
married(manilal_gandhi, sushila_gandhi).
married(ramdas_gandhi, nirmala_gandhi).
married(devdas_gandhi, lakshmi_devdas).

% -----------------------
% BLOOD RELATIONS RULES
% -----------------------

% Father: X is father of Y
father(Y, X) :- parent(X, Y), male(X).

% Mother: X is mother of Y
mother(Y, X) :- parent(X, Y), female(X).

% Grandparent relations
grandparent(Y, X) :- parent(P, Y), parent(X, P).
grandfather(Y, X) :- grandparent(Y, X), male(X).
grandmother(Y, X) :- grandparent(Y, X), female(X).

% Sibling relations
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
brother(X, Y) :- sibling(X, Y), male(X).
sister(X, Y) :- sibling(X, Y), female(X).

% Ancestor relation (recursive)
ancestor(Y, X) :- parent(X, Y).
ancestor(Y, X) :- parent(P, Y), ancestor(P, X).

% Spouse relation (derived from married facts)
spouse(X, Y) :- married(X, Y).
spouse(X, Y) :- married(Y, X).
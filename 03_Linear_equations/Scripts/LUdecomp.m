function [x] = LUdecomp(A,b)
[L, U, P] = lu(A);     % Get L, U and P
d = P*b;               % Permute b vector
y = forwardSub(L,d);   % Can also do y=L\d
x = backwardSub(U,y);  % Can also do x=U\y
return

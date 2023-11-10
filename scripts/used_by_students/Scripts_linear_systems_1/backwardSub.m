function [x] = backwardSub(A,b)
% Performs backward substitution of Ax=b, using upper
% triangular matrix A and right hand side b.

% Error checking; matrix should be square
[N,M] = size(A);
if (N ~= M)
    error('Matrix A in backwardSub should be square');
end

% Assign b to x
x=b;

% Perform backsubstitution
for row=N:-1:1
    for j =(row+1):N
        x(row)=x(row)-A(row,j)*x(j);
    end
    x(row)=x(row)/A(row,row);
end

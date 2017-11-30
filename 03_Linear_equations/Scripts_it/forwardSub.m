function [x] = forwardSub(A,b)

% Check the matrix - should be square
[N,M] = size(A);
if (N ~= M)
    error('Matrix A in forwardSub should be square');
end

% Assign b to x
x=b;

% Perform forward substitution
for row=1:N
    for j =1:row-1
        x(row)=x(row)-A(row,j)*x(j);
    end
    x(row)=x(row)/A(row,row);
end

function [x,A,b] = Gaussian_elimination(A,b)

N = length(b);
for column = 1:N-1
    for row = column+1:N
        d = A(row,column)/A(column,column);
        A(row,:) = A(row,:) - d*A(column,:);
        b(row) = b(row) - d*b(column);
    end
end

x = b;

for row = N:-1:1
    x(row) = b(row);
    for i = (row+1):N
        x(row) = x(row) - A(row,i)*x(i);
    end
    x(row) = x(row)/A(row,row);
end

end
function [x] = backwardSub(A,b)

[N,M] = size(A);
if (N ~= M)
    error('Matrix A in backwardSub should be square');
end

x=b;
for row=1:N
	for j =1:row-1
		x(row)=x(row)-A(row,j)*x(j);
	end
	x(row)=x(row)/A(row,row);
end
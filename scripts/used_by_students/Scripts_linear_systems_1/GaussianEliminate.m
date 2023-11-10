function [x,A,b] = GaussianEliminate(A,b)
% Solves Ax=b using Gaussian Elimination. 
% Syntax: [x] = GaussianEliminate(A,b)
% A: Matrix A
% b: Start vector
% x: Solution vector

% Perform elimination to obtain an upper triangular matrix
N = length(b);
for column=1:(N-1) % Select pivot 
	for row=(column+1):N % Loop over subsequent rows (below pivot)
		d=A(row,column)/A(column,column);
	 	A(row,:)=A(row,:)-d*A(column,:);
	 	b(row)= b(row)-d*b(column);
	end
end	

% Perform backsubstitution
for row=N:-1:1
	x(row) = b(row);
	for i =(row+1):N
		x(row)=x(row)-A(row,i)*x(i);
	end
	x(row)=x(row)/A(row,row);
end

% Transpose the solution to vertical
x=x';
return

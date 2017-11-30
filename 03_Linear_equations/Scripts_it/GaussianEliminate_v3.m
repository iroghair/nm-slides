function [x,A,b] = GaussianEliminate_v3(A,b)
% Solves Ax=b using Gaussian Elimination. 
% Syntax: [x] = GaussianEliminate(A,b)
% A: Matrix A
% b: Start vector
% x: Solution vector

N = length(b);
for column=1:(N-1)
    % Find maximum element below pivot row in this column 
    [dummy,index]= max(abs(A(column:end,column)));
    index=index+column-1; % Get actual column in A (max gets only below pivot)
    % Store current row in temp
    A = SWAP(A,column,index);
    % Swap values in b
    b = SWAP(b,column,index);
	for row=(column+1):N
		d=A(row,column)/A(column,column);
	 	A(row,:)=A(row,:)-d*A(column,:);
	 	b(row)= b(row)-d*b(column);
	end
end	

% Backsubstitution
x = backwardSub(A,b);
return

function x = SWAP(x, r1, r2)
% This function swaps two rows in vector x, returns vector v
% Syntax: v = SWAP(x, r1, r2)
% x: input vector, replaced by output vector
% r1, r2: rows to be swapped

 % Store current row in temp
temp = x(r1,:);
% Swap pivot row and desired row
x(r1,:)=x(r2,:);
x(r2,:)=temp;

return

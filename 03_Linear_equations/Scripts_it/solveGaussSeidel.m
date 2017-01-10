function [x,k] = solveGaussSeidel(A,b,err)
% Solves a linear system using the Jacobi method

% Set default error
if nargin < 3
    err = 1e-1;
end

x = b;              % Set initial guess to b
N = length(A);      % Number of equations
k = 0;              % Init number of iterations
L = tril(A);
U = triu(A,1);

% While not converged or max_it not reached
while ( norm(A*x-b)>err && k < 1000 )
    x_old = x;
    for i=1:N
        s = 0;
        for j = 1:N
            if (j < i)
                % Sum off-diagonal*x
                s = s+A(i,j)*x(j);
            end
            if (j > i)
                % Sum off-diagonal*x_old
                s = s+A(i,j)*x_old(j);
            end
        end
        % Compute new x value
        x(i) = (b(i)-s)/A(i,i);
    end
    % Increate number of iterations
    k = k+1;
end


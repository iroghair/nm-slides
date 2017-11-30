function [x,it_GS] = solveGaussSeidel(A,b,tol)
% Solves a linear system using the Jacobi method

% Set default error
if nargin < 3
    tol = 1e-2;
end

x = b + 1e-16;          % Set initial guess to b
xDiff = 1;              % Norm of the difference between x_old and x_new
N = length(A);          % Number of equations
it_GS = 0;              % Init number of iterations
L = tril(A);
U = triu(A,1);

% While not converged or max_it not reached
while ( xDiff > tol && it_GS < 1000 )
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
    it_GS = it_GS+1;
    xDiff = norm((x-x_old)./x,2);
end

it_GS

end

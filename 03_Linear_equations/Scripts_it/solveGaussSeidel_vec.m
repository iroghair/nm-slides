function [x,it_GS] = solveGaussSeidel_vec(A,b,tol)
% Solves a linear system using the Jacobi method

% Set default error
if nargin < 3
    tol = 1e-2;
end

x = b + 1e-16;      % Set initial guess to b
xDiff = 1;          % Norm of the difference between x_old and x_new
N = length(A);      % Number of equations
it_GS = 0;          % Init number of iterations

% While not converged or max_it not reached
while ( xDiff > tol && it_GS < 1000 )
    x_old = x;
    for i=1:N
        s = 0;
        jrangemin = 1:(i-1);
        jrangemax = (i+1):N;
        % Sum off-diagonal*x
        s = s+A(i,jrangemin)*x(jrangemin);
        % Sum off-diagonal*x_old
        s = s+A(i,jrangemax)*x_old(jrangemax);

        % Compute new x value
        x(i) = (b(i)-s)/A(i,i);
    end
    % Increate number of iterations
    it_GS = it_GS+1;
    xDiff = norm((x-x_old)./x,2);
end

it_GS

end



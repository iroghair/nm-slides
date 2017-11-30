function [x,it_jac] = solveJacobi_vec(A,b,tol)
% Solves a linear system using the Jacobi method

% Set default error
if nargin < 3
    tol = 1e-2;
end

x = b + 1e-16;          % Set initial guess to b
xDiff = 1;              % Norm of the difference between x_old and x_new
N = length(A);          % Number of equations
it_jac = 1;             % Init number of iterations

% While not converged or max_it not reached
while ( xDiff > tol && it_jac < 1000 )
    x_old = x;
    for i=1:N
       % Sum off-diagonal*x_old
        offDiagonalIndex = [1:(i-1) (i+1):N];
        Aij_Xj = A(i,offDiagonalIndex)*x_old(offDiagonalIndex);

        % Compute new x value
        x(i) = (b(i)-Aij_Xj)/A(i,i);
    end
    it_jac = it_jac+1;
    xDiff = norm((x-x_old)./x,2);
end

it_jac

end

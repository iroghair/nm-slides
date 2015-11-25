function [x0,it_jac] = solveJacobi(A,b,tol)
% Solves a linear system using the Jacobi method

% Set default error
if nargin < 3
    tol = 1e-6;
end

x0 = b;   % Initial guess
x = zeros(size(b));      % Pre-allocate vector x
N = length(A);           % Number of equations
it_jac = 1;              % Init number of iterations

for i = 1:N
    x(i) = (1/A(i,i))*((b(i) - A(i,[1:i-1,i+1:N]) * x0([1:i-1,i+1:N])));
end
    
while ( norm(x-x0, 1) > tol  && it_jac < 1000 )
    x0 = x;
    for i = 1:N
        x(i) = (1/A(i,i))*((b(i) - A(i,[1:i-1,i+1:N]) * x0([1:i-1,i+1:N])));
    end
    it_jac = it_jac + 1;
end

it_jac

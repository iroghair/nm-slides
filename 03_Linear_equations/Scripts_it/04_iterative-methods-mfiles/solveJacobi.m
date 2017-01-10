function [x,it_jac] = solveJacobi(A,b,tol)
% Solves a linear system using the Jacobi method

% Set default error
if nargin < 3
    tol = 1e-1;
end

x = 25*ones(size(b));   % Set initial guess to b
N = length(A);          % Number of equations
it_jac = 1;             % Init number of iterations

% While not converged or max_it not reached
while ( norm(A*x-b, 2) > tol && it_jac < 1000 )
    x_old = x;
    for i=1:N
        s = 0;
        for j = 1:N
            if (j ~= i)
                % Sum off-diagonal*x_old
                s = s+A(i,j)*x_old(j);
            end
        end
        % Compute new x value
        x(i) = (b(i)-s)/A(i,i);
    end
    % Increate number of iterations
    it_jac = it_jac+1;
end


% Uncomment this part to use array-indices. Remember to comment the part
% above!
% 
% while ( norm(A*x-b, 2) > tol && it_jac < 1000 )
%     x_old = x;
%     for i = 1:N
%         x(i) = (1/A(i,i))*((b(i) - A(i,[1:i-1,i+1:N]) * x_old([1:i-1,i+1:N])));
%     end
%     it_jac = it_jac + 1;
% end

it_jac

function [xc,yc,Tc,A,b] = solveLaplaceEq(Nx,Ny)
% Solves the Laplace equation for steady-state heat conduction

if (nargin < 2)
    Nx = 10;
    Ny = 10;
end

d = 1/Nx;                           % Grid spacing
alpha = 1;                          % Heat conduction
Tb = [10 20 30 40];                 % Fixed boundary temperatures

% Fill sparse matrix with [1 1 -4 1 1]
e = ones(Nx*Ny,1);
A = spdiags([e,e,-4*e,e,e],[-Nx,-1,0,1,Nx],Nx*Ny,Nx*Ny);
A = A*alpha/d^2;                    % This doesnt matter, steady state...
b = zeros(Nx*Ny,1);                 % Right hand side vector

[A,b] = setBoundaryConditions(A,b,Tb,Nx,Ny);% Set boundary conditions

tic; T = A\b; toc                                    % Solve matrix
% tic; [T,A,b] = GaussianEliminate_v3(A,b); toc
% tic; [T,L,U] = LUdecomp(A,b); toc
% % 
% tic; [T,it_j] = solveJacobi(A,b); toc
% tic; [T,it_j] = solveJacobi_vec(A,b); toc
% % % 
% tic; [T,it_gs] = solveGaussSeidel(A,b); toc
% tic; [T,it_gs] = solveGaussSeidel_vec(A,b); toc

Tc = reshape(T,[Nx,Ny]);                     % Reshape x-vec to mat Nx,Ny
[xc yc] = meshgrid(1:Nx,1:Ny);               % Get position arrays
surf(xc,yc,Tc)                               % Surface plot












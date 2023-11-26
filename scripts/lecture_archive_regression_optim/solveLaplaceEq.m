function T = solveLaplaceEq(Nx,Ny,Tb,Tint)
% Solves the Laplace equation for steady-state heat conduction
% Fill sparse matrix with [1 1 -4 1 1]
e = ones(Nx*Ny,1);
A = spdiags([e,e,-4*e,e,e],[-Nx,-1,0,1,Nx],Nx*Ny,Nx*Ny);
b = zeros(Nx*Ny,1);                 % Right hand side vector

[A,b] = setBoundaryConditions(A,b,Tb,Nx,Ny);% Set boundary conditions

% Set a central node to Tint
ind = round(Nx * (Ny/2));
A(ind,:) = 0; % Reset matrix for boudary cells
A(ind,ind) = 1; % Add a 1 on the diagonal
b(ind) = Tint;

T = A\b;                                    % Solve matrix


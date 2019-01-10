Nx = 20;
Ny = 20; 

Nc = Nx * Ny;

e = ones(Nc,1);
A = spdiags([e, e, -4*e, e, e], [-Nx, -1, 0, 1, Nx], Nc, Nc);
b = zeros(Nc,1);

[A2,b2] = setBoundaryConditions(A,b,[10 20 30 40], Nx, Ny);
% T_sol = A2\b2;
T_sol = GaussianEliminate_v3(A2,b2);

[x y] = meshgrid(1:Nx, 1:Ny);
T_sol = reshape(T_sol, Nx,Ny);
surf(x,y,T_sol);
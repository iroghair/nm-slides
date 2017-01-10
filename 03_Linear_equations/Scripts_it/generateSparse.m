% Grid size
Nx=5;  %number of points along x direction
Ny=5;  %number of points in the y direction
Nc=Nx*Ny; % Total number of points

e = ones(Nc,1);
A = spdiags([e,e,-4*e,e,e],[-Nx,-1,0,1,Nx],Nc,Nc);

figure;
spy(A);

[L,U,P] = lu(A);
figure;
subplot(1,2,1)
spy(L);
subplot(1,2,2)
spy(U)
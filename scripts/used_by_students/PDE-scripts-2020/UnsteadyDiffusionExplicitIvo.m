Nx = 2000;
Nt = 200000;
Dax = 1e-8;
cL = 1;
cR = 0;
tend = 50;
length = 5e-3;

dt = tend/Nt;
dx = length/Nx;

Fo = Dax*dt/(dx*dx);

x = linspace(0, length, Nx+1);

c = zeros(Nt+1,Nx+1);
c(:,1) = cL;
c(:,Nx+1) = cR;
tic
for n=1:Nt
    for i=2:Nx
        c(n+1,i) = Fo*c(n,i-1) + (1 - 2*Fo)*c(n,i) + Fo*c(n,i+1);
    end
end
toc

% out = [12.6 62.5 125 625 5000];
outdt = fix(linspace(1,Nt,min(Nt,10)));
% outdt = fix(out/dt);
plot(x,c(outdt,:))
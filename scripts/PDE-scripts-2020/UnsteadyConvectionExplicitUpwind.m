Nx = 1000;
Nt = 100000;
u = 0.001;
%u = -0.001;
cin = 1;
tend = 100;
length = 0.1;

dt = tend/Nt;
dx = length/Nx;

Co = u*dt/dx;

x = linspace(0, length, Nx+1);

c = zeros(Nt+1,Nx+1);
c(:,1) = cin;
%c(:,Nx+1) = cin;

for n=1:Nt
    for i=2:Nx
        c(n+1,i) = c(n,i) - Co*((u>=0)*(c(n,i) - c(n,i-1)) + (u<0)*(c(n,i+1) - c(n,i)));
    end
    c(n+1,Nx+1) = c(n+1,Nx);
    %c(n+1,1) = c(n+1,2);
end

out = [10 20 30 60 100];
outdt = fix(out/dt);
plot(x,c(outdt,:))
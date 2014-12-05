function [dxdz] = BVPODE(t,x,N)
c_tot = 101325/(8.314*873);
D12 = 1.6e-3;
dxdz = -(1+x)/(c_tot * D12) * N;
return
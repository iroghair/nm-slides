N = 100;
xa(1) = 0;
xb = xa;

for i = 1:N
    xa(i+1) = (3*xa(i)^2 + 3*xa(i) + 4)^(1/3);
    xb(i+1) = (xb(i)^3 - 3*xb(i) - 4)/3;
end

diffxa = abs(diff(xa))
figure;
semilogy(1:N,diffxa)
hold on
semilogy([10 11],[diffxa(10) diffxa(11)], 'o')

log(abs(diffxa(13)/diffxa(12)))/log(abs(diffxa(12)/diffxa(11)))


    
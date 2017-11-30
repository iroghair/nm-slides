n = 1;
fn(1) = 1/(pi^2*n^2);
for n = 2:1000
    fn(n) = fn(n-1) + 1/(pi^2*n^2);
end

array_n = 1:1000;
subplot(2,1,1)
plot(array_n, fn);
subplot(2,1,2)
semilogy(array_n, fn-(1/6))
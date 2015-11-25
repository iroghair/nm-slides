s = [10:10:90 100:100:1000 2000:1000:5000 10000]
for n = 1:length(s)
    s(n)
    A = rand(s(n));
    tic;
    Ainv = inv(A);
    t_inv(n) = toc;
end
loglog(s,t_inv)
xlabel('N')
ylabel('Time [s]')
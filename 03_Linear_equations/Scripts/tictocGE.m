s = [10:10:90 100:100:1000 2000]
for n = 1:length(s)
    s(n)
    A = rand(s(n));
    b = rand(s(n),1);
    tic;
    x = GaussianEliminate_v3(A,b);
    t_GE(n) = toc;
end
loglog(s,t_GE);
xlabel('N');
ylabel('Time [s]');

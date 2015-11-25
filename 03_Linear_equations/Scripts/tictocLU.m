s = [10:10:90 100:100:1000 2000]
for n = 1:length(s)
    s(n)
    A = rand(s(n));
    b = rand(s(n),1);
    tic;
    LUdecomp(A,b);    
    t_LU(n) = toc;
end
loglog(s,t_LU);
xlabel('N');
ylabel('Time [s]');

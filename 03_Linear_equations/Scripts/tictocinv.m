% Generate random matrices of various sizes 's'. Invert the 
% matrices and store the time required for the inversion. 
% Finally, plot the time vs the matrix size
s = [10:10:90 100:100:1000 2000:1000:5000 10000];
for n = 1:length(s);
    s(n)
    A = rand(s(n));
    tic;
    Ainv = inv(A);
    t_inv(n) = toc;
end
loglog(s,t_inv)
xlabel('N')
ylabel('Time [s]')
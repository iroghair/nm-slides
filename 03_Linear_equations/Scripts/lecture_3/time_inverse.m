N=[10:10:100 200:100:1000 2000:1000:5000];

for i = 1:length(N)
    N(i)
    A = rand(N(i));
    
    tic
    Ainv = inv(A);
    t(i) = toc;
end



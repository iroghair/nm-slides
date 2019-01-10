N = 1e8;
a = rand(N,1);
b = rand(N,1);

tic
% for i = 1:N
%     c(i) = a(i)*b(i);
% end
c = a .* b;
toc

function [avg,ssm] = myAverage(a,b,c)

myvector = [a;b;c];
% out = mean(myvector);
ssm = (a + b + c);
avg = ssm/3;
end

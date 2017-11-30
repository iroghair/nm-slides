function nroot = brak(func, x1, x2, n);
nroot = 0;
dx = (x2 - x1)/n;
x = x1;
fp = func(x1);
for i = 0:n
  x = x + dx;
  fc = func(x);
  if (fc*fp<=0)
    nroot = nroot + 1;      
    xb1(nroot) = x - dx;
    xb2(nroot) = x;
  end;
  fp = fc;
end;
if n>0
  for i = 1:nroot 
    disp(sprintf('Root %d in bracketing interval [%f, %f]', [i,xb1(i),xb2(i)]));
  end
else
  disp('No roots found!');
end;

return;
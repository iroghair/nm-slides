function found = brac(func, x1, x2)
ntry = 50;
factor = 1.6;

found = false;
if (x1~=x2)
  f1 = func(x1);
  f2 = func(x2);
  for i = 1:ntry
    if (f1*f2<0)
      found = true
      break;
    end;
    if (abs(f1)<abs(f2))
      x1 = x1 + factor*(x1-x2);
      f1 = func(x1);
    else
      x2 = x2 + factor*(x2-x1);
      f2 = func(x2);
    end; 
  end;
else
  disp('Bad initial range!');    
end;

if found
  disp(sprintf('The bracketing interval = [%f, %f]\n', [x1,x2]));
else
  disp('No bracketing interval found!');
end;
return
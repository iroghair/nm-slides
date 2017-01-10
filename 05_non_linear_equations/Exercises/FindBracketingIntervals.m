function n = FindBracketingIntervals(func, x1, x2, nint);
  nroot = brak(func,x1,x2,nint);
  if (nroot<1) 
    brac(func,x1,x2);  
  end;
return
[ dnum , dnam ] = weekday ( now ) ;
switch dnum
case {1 ,7}
disp ('Yay ! It is weekend !') ;
case 6
disp ('Hooray ! It is Friday !') ;
case {2 ,3 ,4 ,5}
disp (['Today is ' dnam ]) ;
otherwise
disp ('Today is not a good day ... ') ;
end
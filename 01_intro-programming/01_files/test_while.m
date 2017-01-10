num = floor (10* rand +1) ;
guess = input ('Your guess please : ') ;

while ( guess ~= num )
    guess = input ('That is wrong . Try again ... ') ;
end

if (isempty(guess))
    disp('No number supplied - exit');
else
    disp ('Correct !') ;
end
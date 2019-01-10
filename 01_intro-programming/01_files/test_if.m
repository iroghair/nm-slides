num = floor (10* rand +1);
guess = input ('Your guess please : ');

if ( guess ~= num )
    disp (['Wrong, it was ', num2str(num), '. Kbye. ']);
else
    disp ('Correct !');
end
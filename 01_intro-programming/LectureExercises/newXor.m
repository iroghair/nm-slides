function [value] = newXor(val1, val2)
if ~islogical(val1) || ~islogical(val2)
    disp('Input should be logical values only');
    return
end
if (val1 && val2) || (~val1 && ~val2)
    value = true;
else
    value = false;
end


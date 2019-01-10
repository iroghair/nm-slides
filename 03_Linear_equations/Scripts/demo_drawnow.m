pos = [0 0];

vel = rand(1,2);

for t = 2:1000
    pos(t,:) = pos(t-1,:) + vel;
    vel = 1-2*rand(1,2);
    plot(pos(:,1),pos(:,2))
    drawnow
    plot(pos(:,1),pos(:,2))
end




    
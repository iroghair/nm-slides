x_cont = linspace ( -1 ,1 ,1001) ;
p2 = polyfit ( x2 , y2 ,2) ;
p3 = polyfit ( x2 , y2 ,3) ;
p4 = polyfit ( x2 , y2 ,4) ;
y_cont2 = polyval ( p2 , x_cont ) ;
y_cont3 = polyval ( p3 , x_cont ) ;
y_cont4 = polyval ( p4 , x_cont ) ;
plot(x2,y2,'o',x_cont,y_cont2,x_cont,y_cont3,x_cont , y_cont4 )
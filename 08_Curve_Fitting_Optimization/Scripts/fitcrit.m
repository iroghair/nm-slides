function err = fitcrit ( ke ,T ,U , U0 )
[t , ue ] = ode45 ( @simpleode ,T , U0 ,[] , ke ) ;
err = ( ue - U ) ;
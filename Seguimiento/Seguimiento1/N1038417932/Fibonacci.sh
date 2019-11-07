
#Este es un script en bash que calcula los primeros 1000 digitos de la serie de fibonacci  e imprime los pares 

  Fib_2=0;
  Fib_1=1;
  echo -n  "${Fib_2} "

  for i in {2..1000}
do

    Fib=$((Fib_2+Fib_1 ))
    val=$(( Fib%2 ))
    if [ $val = 0 ];
    then
	echo -n "${Fib} "
    fi

    Fib_2=$Fib_1
    Fib_1=$Fib
  
  

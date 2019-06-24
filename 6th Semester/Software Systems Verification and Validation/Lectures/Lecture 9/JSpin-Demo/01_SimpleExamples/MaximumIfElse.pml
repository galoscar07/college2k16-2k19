active proctype P(){
  int a=5, b=7;
  int max1, max2;
  if
    :: a > b -> max1 =a;  /* not atomic statement*/
    :: else -> max1 =b;  /* an interleaving is possible between */
  fi;     /* the guard and the following assignment statement */

  printf("The maximum of %d and %d = %d by max1 \n", a,b,max1);

  max2 = (a>b -> a:b);
  printf("The maximum of %d and %d = %d by max2 \n", a,b,max2)

}
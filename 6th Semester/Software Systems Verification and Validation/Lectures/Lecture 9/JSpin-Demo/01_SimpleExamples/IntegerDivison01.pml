active proctype P(){
/*  Example 1 - run
  int dividend =15;
  int divisor =4; */

/*  Example 2 - run*/
  int dividend =16;
  int divisor =4; 


  int quotient, remainder;
  /* precondition */
  assert (dividend >=0 && divisor >0);

  quotient =0;
  remainder = dividend;
  do
/*  Example 1 - run
  :: remainder >= divisor -> */
/*  Example 2 - run*/
  :: remainder > divisor ->
       quotient++;
       remainder = remainder -divisor
  :: else ->
       break        
  od;
  printf("%d divided by %d = %d, remainder=%d \n",
     dividend, divisor, quotient, remainder);
   /* postcondition */
  assert(0<=remainder && remainder <divisor);
  assert(dividend == quotient * divisor +remainder) 

}
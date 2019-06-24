active proctype P(){
  byte days;
 byte month =8;
  int year = 2000; 

/*  byte month =6;
  int year = 2000; */

/* byte month =2;
  int year = 2000; */

/*  byte month =2;
  int year = 2004; */

/*  byte month =2;
  int year = 2000;*/

  if
  :: month ==1 || month ==3 || month ==5 ||
     month ==7 || month ==8 || month ==10 ||
     month ==12 ->
        days = 31
  :: month ==4 || month ==6 || month ==9 ||
     month ==11 ->
        days = 30
  :: month ==2 && year % 4==0 && /*leap year */
     (year %100 !=0 || year % 400 ==0) ->
        days = 29
  :: else ->    /* the else guard is only selected if */
        days =28   /* all other guards evaluate to false  */
  fi;
  printf("month = %d, year=%d, days=%d \n", month, year, days)

}
#define mutex (critical<=1)
/*   
 mutex= mutual exclusion
 []always
 In the LTL formula
 []mutex
*/
bool wantP =false, wantQ=false;
byte critical =0;

active proctype P(){
  do
  :: printf("Noncritical section P \n");
     wantP =true;
     !wantQ;
     critical++;
     printf("Critical section P \n");
  /*   assert(critical<=1);*/
     critical--;
     wantP =false
  od
}

active proctype Q(){
  do
  :: printf("Noncritical section Q \n");
     wantQ =true;
     !wantP;
     critical++;
     printf("Critical section P \n");
/*     assert(critical<=1);*/
     critical--;
     wantQ =false
  od
}




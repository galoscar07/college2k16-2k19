bool wantP =false, wantQ=false;

active proctype P(){
  do
  :: printf("Noncritical section P \n");
     wantP =true;  
     printf("Critical section P \n");
     wantP =false
  od
}

active proctype Q(){
  do
  :: printf("Noncritical section Q \n");
     wantQ =true;
     printf("Critical section P \n");
     wantQ =false
  od
}
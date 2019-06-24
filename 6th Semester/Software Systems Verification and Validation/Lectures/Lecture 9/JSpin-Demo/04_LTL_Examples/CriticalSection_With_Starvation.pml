/*   
 Step 1) Translate button
 Step 2) absence of starvation by <>csp
    Weak fairness - checked 
    Acceptance - combobox
    Verify button


*/

bool wantP =false, wantQ=false;

active proctype P(){
  do
  :: wantP =true;
     do
     :: wantQ->
         wantP=false;
         wantP=true
     :: else -> break
    od;
    csp=true;
    csp=false;
    wantP=false
  od
}

active proctype Q(){
  do
  :: wantQ =true;
     do
     :: wantP->
         wantQ=false;
         wantQ=true
     :: else -> break
    od;
    wantQ=false
  od
}




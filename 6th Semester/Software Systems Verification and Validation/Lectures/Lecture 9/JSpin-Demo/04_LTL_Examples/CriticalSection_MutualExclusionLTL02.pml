
/*   
 In the LTL formula
 []!(csp && csq)

*/
bool wantP =false, wantQ=false;
byte critical =0;

active proctype P(){
  do
  :: 
     wantP =true;
     !wantQ;
     csp=true;
     csp=false;
     wantP =false
  od
}

active proctype Q(){
  do
  :: 
     wantQ =true;
     !wantP;
     csq=true;
     csq=false;
     wantQ =false
  od
}




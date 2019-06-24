/*
 * First KLEE testing a small function
 * http://klee.github.io/tutorials/testing-function/
 */


int get_gF(int gL, int gS, int gE) {
	int l=0, s=0,e=0;
	if (gL >=5 )
		l=1;
	if (gS>=5)
		s=1;;
	if (gE>=5){
		if (gL<5 && gS<5){
			l=-1; s=-1;
		}
		e=2;
	}
	gF=l+s+e;
 	//  assert(gF>=3);
	return gF;}

int main() {
	int a,b,c;
	klee_make_symbolic(&a, sizeof(a), "a");
	klee_make_symbolic(&b, sizeof(a), "b");
	klee_make_symbolic(&c, sizeof(a), "c");
	return get_gF(a,b,c);
}
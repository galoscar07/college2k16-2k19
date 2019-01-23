package models;

public class ArithmeticExpression implements Expression {
	private char op;
	private Expression l,r;
	public ArithmeticExpression(char o1,Expression l1,Expression r1) {
		op = o1;
		l=l1;
		r=r1;
	}
	public int eval(IDictionary<String,Integer> st) {
		int a,b;
		a = l.eval(st);
		b = r.eval(st);
		switch (op) {
		case '+':
			return a+b;
		case '-':
			return a-b;
		case '/':
			if (b==0)
				throw new DivisionByZeroException("Division by 0.");
			return a/b;
		case '*':
			return a*b;
		default:
			throw new UnknownOperatorException("Unknown operator.");
		}
	}
	@Override
	public String toString() {
		return l.toString() + op + r.toString();
	}
}

package models;

public class PrintStatement implements Statement{
	private Expression expr;
	public PrintStatement(Expression e) {
		expr = e;
	}
	@Override
	public ProgramState execute(ProgramState ps) {
		IDictionary<String,Integer> st = ps.getSymbolTable();
		int e = expr.eval(st);
		ps.getList().add(e);
		return ps;
	}
	@Override
	public String toString() {
		return "Print(" + expr + ")";
	}
}

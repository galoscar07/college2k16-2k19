package models;

public class IfStatement implements Statement{
	private Expression cond;
	private Statement thenS,elseS;
	
	public IfStatement(Expression c,Statement t,Statement e) {
		cond = c;
		thenS = t;
		elseS = e;
	}
	
	@Override
	public ProgramState execute(ProgramState ps) {
		int res = cond.eval(ps.getSymbolTable());
		if(res!=0) {
			ps.getExecStack().push(thenS);
		}
		else {
			ps.getExecStack().push(elseS);
		}
		return ps;
	}
	
	@Override
	public String toString() {
		return "If" + cond + "then" + thenS + "else" + elseS;
	}
}

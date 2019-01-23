package models;

public class CompoundStatement implements Statement{
	private Statement first,second;
	public CompoundStatement(Statement f,Statement s) {
		first = f;
		second = s;
	}
	@Override
	public ProgramState execute(ProgramState ps) {
		ps.getExecStack().push(second);
		ps.getExecStack().push(first);
		return ps;
	}
	@Override
	public String toString() {
		return "(" + first + "," +second + ")";
	}
}

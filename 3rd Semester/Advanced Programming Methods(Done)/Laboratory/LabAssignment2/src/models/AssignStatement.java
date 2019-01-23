package models;

public class AssignStatement implements Statement {
	private String varName;
	private Expression value;
	public AssignStatement(String n,Expression v) {
		varName = n;
		value = v;
	}
	@Override
	public ProgramState execute(ProgramState ps) {
		IDictionary<String,Integer> st=ps.getSymbolTable();
		int e = value.eval(st);
		if(st.contains(varName)) {
			st.update(varName,e);
		}
		else {
			st.add(varName,e);
		}
		return ps;
	}
	@Override
	public String toString() {
		return varName + "=" + value;
	}
}

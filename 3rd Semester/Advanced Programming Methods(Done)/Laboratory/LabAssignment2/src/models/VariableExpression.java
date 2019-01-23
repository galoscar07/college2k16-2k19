package models;

public class VariableExpression implements Expression{
	private String varName;
	public VariableExpression(String n) {
		varName = n;
	}
	public int eval(IDictionary<String,Integer> st) {
		if(st.contains(varName))
			return st.get(varName);
		else {
			throw new NotFoundException("Not found.");
		}
	}
	@Override
	public String toString() {
		return varName;
	}
}

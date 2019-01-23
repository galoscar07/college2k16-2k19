package models;

public class ConstExpression implements Expression{
	private int val;
	public ConstExpression(int a) {
		val = a;
	}
	public int eval(IDictionary<String,Integer> st) {
		return val;
	}
	@Override
	public String toString() {
		return " " + val;
	}
}
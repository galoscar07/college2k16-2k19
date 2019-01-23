package model;

import exception.DivideByZeroException;
import exception.UnknownComparisonExpression;
import exception.UnknownVariableException;

public class BoolExp extends Exp
{
	private String sign;
	private Exp l;
	private Exp r;
	
	public BoolExp(String si, Exp le, Exp ri)
	{
		sign = si;
		l = le;
		r = ri;
	}
	
	public int	eval(MyIDictionary <String, Integer> st, MyIHeap<Integer> heap) throws UnknownComparisonExpression, DivideByZeroException, UnknownVariableException
	{
		int left;
		int right;
		
		left = l.eval(st, heap);
		right = r.eval(st, heap);
		
		switch(sign)
		{
			case "<=":
				if (left <= right)
					return (1);
				else
					return (0);
			case "<":
				if (left < right)
					return (1);
				else
					return (0);
			case ">=":
				if (left >= right)
					return (1);
				else
					return (0);
			case ">":
				if (left > right)
					return (1);
				else
					return (0);
			case "==":
				if (left == right)
					return (1);
				else
					return (0);
			case "!=":
				if (left != right)
					return (1);
				else
					return (0);
			default:
				throw new UnknownComparisonExpression("Comparator not found!");
		}
	}
	@Override
	public String toString()
	{
		return ("" + l.toString() + " " + sign + " " + r.toString());
	}
}

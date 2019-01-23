package models;

import java.util.ArrayDeque;
import java.util.Deque;

public class ExecStack<T> implements IExecStack<T> {

	private Deque<T> stack;
	public ExecStack() {
		stack=new ArrayDeque<T>();
	}
	@Override
	public void push(T e) {
		stack.push(e);
	}

	@Override
	public T pop() {
		return stack.pop();
	}

	@Override
	public boolean isEmpty() {
		return stack.size()== 0;
	}
	
	@Override
	public String toString() {
		StringBuffer sb = new StringBuffer();
		for(T a:stack) {
			sb.append(a);
			sb.append('\n');
		}
		return sb.toString();
	}
}

package models;

public interface IExecStack<T> {
	void push(T e);
	T pop();
	boolean isEmpty();
}

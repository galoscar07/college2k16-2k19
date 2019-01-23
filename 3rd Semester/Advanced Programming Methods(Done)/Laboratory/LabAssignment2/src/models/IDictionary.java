package models;

public interface IDictionary<T,E> {
	boolean contains(T k);
	E get(T k);
	void add(T k,E e);
	void update(T k,E e);
}

package models;

import java.util.ArrayList;
import java.util.List;

public class MyList<T> implements IList<T>{
	private List<T> list = new ArrayList<>();

	@Override
	public void add(T el) {
		list.add(el);
	}
	
	@Override
	public String toString() {
		StringBuffer s = new StringBuffer();
		for(T e:list) {
			s.append(e);
			s.append('\n');
		}
		return s.toString();
	}
}

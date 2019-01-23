package models;

import java.util.HashMap;
import java.util.Map;

public class Dictionary<T,E> implements IDictionary<T,E>{

	private Map<T,E> dict = new HashMap<T,E>();
	
	@Override
	public boolean contains(T k) {
		return dict.containsKey(k);
	}

	@Override
	public E get(T k) {
		return dict.get(k);
	}

	@Override
	public void add(T k, E e) {
		dict.put(k, e);
		
	}

	@Override
	public void update(T k, E e) {
		dict.put(k, e);
	}
	
	@Override
	public String toString() {
		StringBuffer sb = new StringBuffer();
		for(Map.Entry<T, E> e:dict.entrySet()) {
			sb.append(e.getKey()+" "+e.getValue()+'\n');
		}
		return sb.toString();
	}
}

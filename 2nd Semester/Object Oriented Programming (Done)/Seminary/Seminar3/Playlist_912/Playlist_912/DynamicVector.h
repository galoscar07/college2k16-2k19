#pragma once

#include <iostream>
#include <string>

template <typename T>

class DynamicVector
{
private:
	int len,  capacity;
	T *arr;
	void Resize()
	{
		this->capacity *= 2;
		T *arrn = new T[this->capacity];
		int i;
		for (i = 0; i < this->len; i++)
			arrn[i] = this->arr[i];
		delete[] this->arr;
		this->arr = arrn;		
	}
public:
	DynamicVector(int capacity = 10)
	{
		this->len = 0;
		this->capacity = capacity;
		this->arr = new T[capacity];
	}
	
	DynamicVector(const DynamicVector<T>& v)
	{
		this->len = v.len;
		this->capacity = v.capacity;
		this->arr = new T[this->capacity];
		for (int i = 0; i < this->len; i++)
			this->arr[i] = v.arr[i];
	}

	DynamicVector<T>& operator=(const DynamicVector<T>& v)
	{
		if (this == &v)
			return *this;
		delete[] this->arr;
		this->len = v.len;
		this->capacity = v.capacity;
		this->arr = new T[this->capacity];
		for (int i = 0; i < this->len; i++)
			this->arr[i] = v.arr[i];
		return *this;
	}

	~DynamicVector()
	{
		this->len = 0;
		this->capacity = 0;
		delete[] this->arr;
	}

	void Add(T element)
	{
		int i;
		if (len == capacity)
			Resize();
		else
		{
			this->arr[len] = element;
			this->len++;
		}
	}

	int Get_Len()
	{
		return this->len;
	}

public:
	class iterator: public std::iterator<std::forward_iterator_tag, T, ptrdiff_t, T*, T&>
	{
	private:
		T* current;

	public:
		iterator(T* p) { this->current = p; }
		iterator operator++() { return iterator{ ++this->current }; }
		iterator operator++(int) { return iterator{ this->current++ }; }
		bool operator!=(iterator it) { return this->current != it.current; }
		T operator*() { return *this->current; }
		T* operator->() { return this->current; }
	};

	iterator begin() { return iterator{this->arr}; }
	iterator end() { return iterator{ this->arr + this->len }; }
};

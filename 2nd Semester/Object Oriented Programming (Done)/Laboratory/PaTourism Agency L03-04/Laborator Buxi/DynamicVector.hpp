#pragma once
#include <iterator>

template <typename T>

class DynamicVector{
private:
	T* elems;
	int size;
	int capacity;

public:
	//default constructor
	DynamicVector(int capacity = 10);

	//copy constructor
	DynamicVector(const DynamicVector& v);
	~DynamicVector();

	//assignment operator
	DynamicVector& operator=(const DynamicVector<T>& v);


	T& operator[](int pos);

	//adds an element to the vector
	void add(const T& e);

	//removes an element from the vector
	void remove(int pos);

	void update(const T& e, int pos);

	int getSize() const;
	T* getAllElems() const;

	DynamicVector operator-(T& e);

private:
	//resizes the current dynamicVector
	void resize(double factor = 2);

public:
	class iterator : public std::iterator<std::forward_iterator_tag, T, std::ptrdiff_t, T*, T&>
	{
	private:
		T* ptr;
	public:
		iterator(T* p) : ptr{ p } { }
		iterator operator++() { this->ptr++; return *this; }
		iterator operator++(int dummy) { iterator i = *this; this->ptr++; return i; }
		T& operator*() { return *this->ptr; }
		T* operator->() { return this->ptr; }
		bool operator!=(const iterator& it) { return this->ptr != it.ptr; }
	};

	iterator begin()
	{
		return iterator{ this->elems };
	}

	iterator end()
	{
		return iterator{ this->elems + this->size };
	}
};

template <typename T>
DynamicVector<T>::DynamicVector(int capacity){
	this->size = 0;
	this->capacity = capacity;
	this->elems = new T[capacity];
}

template <typename T>
DynamicVector<T>::DynamicVector(const DynamicVector<T>& v)
{
	this->size = v.size;
	this->capacity = v.capacity;
	this->elems = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = v.elems[i];
}

template <typename T>
DynamicVector<T>::~DynamicVector()
{
	delete[] this->elems;
}

template <typename T>
DynamicVector<T>& DynamicVector<T>::operator=(const DynamicVector<T>& v)
{
	if (this == &v)
		return *this;
	this->size = v.size;
	this->capacity = v.capacity;
	delete[] this->elems;
	this->elems = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = v.elems[i];

	return *this;
}

template <typename T>
T& DynamicVector<T>::operator[](int pos)
{
	return this->elems[pos];
}

template <typename T>
void DynamicVector<T>::add(const T& e)
{
	if (this->size == this->capacity)
		this->resize();
	this->elems[this->size] = e;
	this->size++;
}

template <typename T>
void DynamicVector<T>::remove(int pos)
{
	if (this->size == 0)
		return;
	if (this->elems == NULL)
		return;

	for (int i = pos; i < this->size - 1; i++)
		this->elems[i] = this->elems[i + 1];

	this->size--;
}

template <typename T>
void DynamicVector<T>::update(const T& e, int pos)
{
	this->elems[pos] = e;
}

template <typename T>
void DynamicVector<T>::resize(double factor)
{
	this->capacity *= static_cast<int>(factor);

	T* els = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = els[i];

	delete[] this->elems;
	elems = els;
}

template <typename T>
T* DynamicVector<T>::getAllElems() const
{
	return this->elems;
}

template <typename T>
int DynamicVector<T>::getSize() const
{
	return this->size;
}

template <typename T>
DynamicVector<T> DynamicVector<T>::operator-(T& e)
{
	for (int i = 0; i < this->size; i++)
	{
		if (this->elems[i].getTitle() == e.getTitle())
			for (int j = i; j < this->size - 1; j++)
				this->elems[j] = this->elems[j + 1];
		break;
	}
	return *this;
}

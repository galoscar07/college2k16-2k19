#pragma once

template <typename T>
class DynamicVector {
private:
	T *container;
	unsigned int size, capacity;
	void increaseSize();
public:
	DynamicVector(unsigned int capacity = 10);
	DynamicVector(DynamicVector &v);
	DynamicVector &operator=(const DynamicVector &v);
	~DynamicVector();
	void add(const T &e);
	unsigned int length() const;
};

template <typename T>
DynamicVector<T>::DynamicVector(unsigned int capacity) {
	container = new T[capacity];
	size = 0;
	this->capacity = capacity;
}

template <typename T>
DynamicVector<T>::~DynamicVector() {
	delete[] container;
	container = nullptr;
	size = 0;
	capacity = 0;
}

template <typename T>
void DynamicVector<T>::add(const T &e) {
	if (size == capacity)
		increaseSize();

	container[size++] = e;
}

template <typename T>
void DynamicVector<T>::increaseSize() {
	T *copy;

	capacity *= 2;
	copy = new T[capacity];
	for (unsigned int i = 0; i < size; i++)
		copy[i] = container[i];
	delete[] container;

	container = copy;
	copy = nullptr;
}

template <typename T>
unsigned int DynamicVector<T>::length() const {
	return size;
}

template <typename T>
DynamicVector<T>::DynamicVector(DynamicVector& v)
{
	this->capacity = v.capacity;
	this->size = v.size;
	this->container = new T[this->capacity];
	for (unsigned int i = 0; i < this->size; i++)
		this->container[i] = v.container[i];
}


template <typename T>
DynamicVector<T> & DynamicVector<T>::operator=(const DynamicVector &v)
{
	if (this == &v)
		return *this;
	this->capacity = v.capacity;
	this->size = v.size;

	T *aux = new T[this->capacity];
	for (unsigned int i = 0; i < this->size; i++)
		aux[i] = v.container[i];
	
	delete[] this->container;
	this->container = aux;
	return *this;
}

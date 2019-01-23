#include "DynamicVector.hpp"

DynamicVector::DynamicVector(int capacity){
	this->size = 0;
	this->capacity = capacity;
	this->elems = new TElement[capacity];
}

DynamicVector::DynamicVector(const DynamicVector& v)
{
	this->size = v.size;
	this->capacity = v.capacity;
	this->elems = new TElement[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = v.elems[i];
}

DynamicVector::~DynamicVector()
{
	delete[] this->elems;
}

DynamicVector& DynamicVector::operator=(const DynamicVector& v)
{
	if (this == &v)
		return *this;
	this->size = v.size;
	this->capacity = v.capacity;
	delete[] this->elems;
	this->elems = new TElement[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = v.elems[i];

	return *this;
}

void DynamicVector::add(TElement& e)
{
	if (this->size == this->capacity)
		this->resize();
	this->elems[this->size] = e;
	this->size++;
}

void DynamicVector::remove(int pos)
{
	if (this->size == 0)
		return;
	if (this->elems == NULL)
		return;

	for (int i = pos; i < this->size - 1; i++)
		this->elems[i] = this->elems[i + 1];

	this->size--;
}

void DynamicVector::update(const TElement& e, int pos)
{
	this->elems[pos] = e;
}

void DynamicVector::resize(double factor)
{
	this->capacity *= static_cast<int>(factor);

	TElement* els = new TElement[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = els[i];

	delete[] this->elems;
	elems = els;
}

TElement* DynamicVector::getAllElems() const
{
	return this->elems;
}

int DynamicVector::getSize() const
{
	return this->size;
}

DynamicVector DynamicVector::operator-(TElement& e)
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

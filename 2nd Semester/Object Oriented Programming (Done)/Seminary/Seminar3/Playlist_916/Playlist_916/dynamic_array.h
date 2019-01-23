template <typename T>
class DynamicVector
{
private:
	int capacity;
	int size;
	T *elems;
	void resize();

public:
	DynamicVector(int capacity=10);
	DynamicVector(const DynamicVector& v);
	DynamicVector& operator=(const DynamicVector& v);
	~DynamicVector();
	void add_to_array(T element);
	//T& get_element_on_position(int position); // returns a reference so we can change the element later
	int get_size();
};

template <typename T>
DynamicVector<T>& DynamicVector<T>::operator=(const DynamicVector& v)
{

}

template <typename T>
DynamicVector<T>::DynamicVector(const DynamicVector& v)
{
	this->size = v.size;
	this->capacity = v.capacity;
	this->elems = new T[v.capacity];
	int i = 0;
	for (; i < v.size; i++)
	{
		this->elems[i] = v.elems[i];
	}
}

template <typename T>
DynamicVector<T>::DynamicVector(int capacity = 10)
{
	// funcion definitions MUST be done within the header !!
	this->size = 0;
	this->capacity = capacity;
	this->elems = new T[this->capacity]; // C++ style memory allocation
}

template <typename T>
DynamicVector<T>::~DynamicVector()
{
	delete[]this->elems; // C++ style memory de-allocation
}

template <typename T>
void DynamicVector<T>::resize()
{
	this->capacity = this->capacity * 2;
	T* el = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		el[i] = this->elems[i];
	delete[] this->elems;
	this->elems = el;
}

template <typename T>
void DynamicVector<T>::add_to_array(T element)
{
	if (this->size == this->capacity)
		this->resize();
	this->elems[this->size] = element; // if T is a pointer, make sure T has an assigment operator override
	this->size++;
}

template<typename T>
inline int DynamicVector<T>::get_size()
{
	return this->size;
}

#ifndef SORTEDSLLIST_H
#define SORTEDSLLIST_H

#include <abstractsortedlist.h>
#include <cassert>

template <typename Object>
class SortedSLList : public AbstractSortedList<Object> {
public:
    /** Constructors */
    SortedSLList();
    SortedSLList(const Object& Data);
    /** Destructor */
    ~SortedSLList();
    /** Get the 'data' at Index in list */
    Object getAtIndex(const int& Index);
    /** Get the 'data' at front in list */
    Object getFront();
    /** Get the 'data' at back in list */
    Object getBack();
    /** Add into the list sorted ascending */
    void add(const Object& Data);
    /** Remove the 'data' at Index in list */
    void removeAtIndex(const int& Index);
    /** Remove the 'data' at front in list */
    void removeFront();
    /** Remove the 'data' at back in list */
    void removeBack();
    /** Check if list contains 'Data' */
    bool contains(const Object& Data);
    /** Clear list */
    void clear();
    /** Return list node count */
    int size();
private:
    class SLNode {
    private:
        friend class SortedSLList;
        Object _data;
        SLNode *_next;
    public:
        /** Constructor */
        SLNode(const Object& data = NULL, const SLNode* next = NULL): _data(data), _next(next) {}
        /** Destructor */
        ~SLNode() {}
        /** Assignment oprator */
        SLNode& operator=(const SLNode& other);
        /** Getter for the data - useless */
        Object& getData();
    };
    /** Begin and end of the Linked List*/
    SLNode *_begin, *_end;
};

/**
    Default constructor
    @PRECOND: None
    @POSTCOND:
        begin = NULL
        end = NULL
        count = 0
    @COMPLEXITY:
        O(1) - it takes constant time to initialize a singly-liked list
*/
template <typename Object>
SortedSLList<Object>::SortedSLList() {
    this->_begin = NULL;
    this->_end = NULL;
    this->_count = 0;
}

/**
    Constructor when one Objects is given
    Create a single-element linked list
    @PRECOND: Node
    @POSTCOND:
        begin = end = node containing the given argument
        count = 1
    @COMPLEXITY:
        O(1) - it takes constant time to initialize a singly-liked list
*/
template <typename Object>
SortedSLList<Object>::SortedSLList(const Object& Data) {
    this->_begin = new SLNode(Data);
    this->_end = this->_begin;
    this->_count = 1;
}

/**
    Destructor: release the memory (works exactly like the clear() method)
    @PRECOND: None
    @POSTCOND:
        List is destroyed
        front = NULL
        back = NULL
        count = 0
    @COMPLEXITY:
        O(N) - where N is the number of nodes in the Singly-Liked List
*/
template <typename Object>
SortedSLList<Object>::~SortedSLList() {
    SLNode *prevNode = NULL, *node = this->_begin;
    while(node != NULL) {
        prevNode = node;
        node = node->_next;
        delete prevNode;
    }
    this->_count = 0;
    this->_begin = this->_end = NULL;
}

/**
    getAtIndex(const int& Index): Method to get the element from a given Index
    Index - the required element position
    @PRECOND: Index between 0 and count - 1
    @POSTCOND:
        Return: Object contained at Index
    @COMPLEXITY:
        We are always making exactly 'Index' steps ahead in the Liked List, so in the
        worst scenario we will execute exactly N steps.
        O(N) where N is the number of nodes in the Singly-Liked List
*/
template <typename Object>
Object SortedSLList<Object>::getAtIndex(const int& Index) {
    /// todo, give up on assertion
    assert(0 <= Index && Index < this->_count);
    SLNode *act = this->_begin;
    int i = 0;
    while(i < Index) {
        act = act->_next;
        ++ i;
    }
    return act->_data;
}

/**
    getFront(): Method to get the first element in the list (aka the smallest one since the ADT is sorted by the Object's < operator)
    @PRECOND: List is valid (not empty)
    @POSTCOND:
        Return: Object contained in front
    @COMPLEXITY:
        O(1) since we store the front node of the Singly-Liked List
*/
template <typename Object>
Object SortedSLList<Object>::getFront() {
    if(this->_begin == NULL)
        return NULL;
    return this->_begin->_data;
}

/**
    getBack(): Method to get the last element in the list (aka the biggest one since the ADT is sorted by the Object's < operator)
    @PRECOND: List is valid (not empty)
    @POSTCOND:
        Return: Object contained at the end of the list
*/
template <typename Object>
Object SortedSLList<Object>::getBack() {
    if(this->_end == NULL)
        return NULL;
    return this->_end->_data;
}

/**
    add(const Object& Data): Method to add an object to the last, while maintaining the sorted property
    Data - Element to be added to the list
    @PRECOND: Data is an object of type 'Object' (defined at the declaration of the SortedSLList)
    @POSTCOND:
        Return: The list now contains Data (and still sorted)
    @COMPLEXITY:
        We first, see where we need to insert the new node, then we do the insert.
        The first part requires O(N) time since in the worst case we look at all the nodes (here N - number
        of nodes of SLList).
        The second part required O(1) time since we only change some pointers.
*/
template <typename Object>
void SortedSLList<Object>::add(const Object& Data) {
    if(this->_begin == NULL)
        this->_begin = this->_end = new SLNode(Data);
    else {
        if(this->_begin->_data >= Data) {
            SLNode *newNode = new SLNode(Data);
            newNode->_next = this->_begin;
            this->_begin = newNode;
        } else {
            SLNode *node = this->_begin, *prevNode = NULL;
            while(node != NULL && node->_data < Data) {
                prevNode = node;
                node = node->_next;
            }
            prevNode->_next = new SLNode(Data);
            prevNode->_next->_next = node;
            if(node == NULL)
                this->_end = prevNode->_next;
        }
    }
    this->_count ++;
}


/**
    removeAtIndex(const int& Index): Method to remove the element from a given Index
    Index - the required element position
    @PRECOND: Index between 0 and count - 1
    @POSTCOND:
        Object at index Index is not removed
    @COMPLEXITY:
        We are always making exactly 'Index' steps ahead in the Liked List, so in the
        worst scenario we will execute exactly N steps.
        O(N) where N is the number of nodes in the Singly-Liked List
*/
template <typename Object>
void SortedSLList<Object>::removeAtIndex(const int& Index) {
    assert(0 <= Index && Index < this->_count);
    if(Index == 0) {
        SLNode *aux = this->_begin;
        this->_begin = this->_begin->_next;
        delete aux;
        this->_count --;
        return ;
    }
    SLNode *prevNode = NULL, *node = this->_begin;
    int i = 0;
    while(i < Index) {
        prevNode = node;
        node = node->_next;
        ++ i;
    }
    prevNode->_next = node->_next;
    this->_count --;
    delete node;
}

/**
    removeFront(): Method to remove front element
    @PRECOND: List is valid (nonempty)
    @POSTCOND:
        Object at index 0 is now removed
    @COMPLEXITY:
        O(1)
*/
template <typename Object>
void SortedSLList<Object>::removeFront() {
    if(this->_begin == NULL)
        return ;
    SLNode *lastFront = this->_begin;
    this->_begin = this->_begin->_next;
    this->_count --;
    delete lastFront;
}

/**
    removeBack(): Method to remove back element
    @PRECOND: List is valid (nonempty)
    @POSTCOND:
        Object at index 'count - 1' is now removed
    @COMPLEXITY:
        O(N) since we first have to get the node ahead of the last element, then to remove the second one.
        Here N - number of elements in the SLList.
*/
template <typename Object>
void SortedSLList<Object>::removeBack() {
    if(this->_begin == NULL)
        return ;
    SLNode *prevNode = NULL, *node = this->_begin;
    while(node->_next != NULL) {
        prevNode = node;
        node = node->_next;
    }
    if(prevNode != NULL) {
        delete prevNode->_next;
        prevNode->_next = NULL;
        this->_end = prevNode;
    } else {
        delete this->_begin;
        this->_begin = this->_end = NULL;
    }
    this->_count --;
}
/**
    contains(const Object& Data): Method to check if the list contains 'Data'
    Data - Data to be checked if it exists
    @PRECOND: Data is an object of 'Object' type (defined at declaration)
    @POSTCOND
        Return: True - if it exists, False - otherwise
    @COMPLEXITY:
        O(N) where N - the number of nodes in the SLList
*/
template <typename Object>
bool SortedSLList<Object>::contains(const Object& Data) {
    SLNode *node = this->_begin;
    while(node != NULL) {
        if(node->_data == Data)
            return true;
        node = node->_next;
    }
    return false;
}

/**
    clear*(): Method to clear the list
    @PRECOND: None
    @POSTCOND: count = 0
    @COMPLEXITY:
        O(N) where N is the number of nodes in the SLList
*/
template <typename Object>
void SortedSLList<Object>::clear() {
    SLNode *prevNode = NULL, *node = this->_begin;
    while(node != NULL) {
        prevNode = node;
        node = node->_next;
        delete prevNode;
    }
    this->_count = 0;
    this->_begin = this->_end = NULL;
}

/**
    size(): Method to return the node count
    @PRECOND: None
    @POSTCOND:
        Return: count (number of nodes in the Linked List)
    @COMPLEXITY:
        O(1)
*/
template <typename Object>
int SortedSLList<Object>::size() {
    return this->_count;
}

/**
    '=' operator for the SLNode class
*/
template <typename Object>
typename SortedSLList<Object>::SLNode& SortedSLList<Object>::SLNode::operator=(const SLNode& other) {
    this->_data = other._data;
    this->_next = other._next;
}

/**
    getData(): Getter for the data of a SLNode
    @POSTCOND: None
    @PRECOND:
        Return: the data stored in the current node
    @COMPLEXITY:
        O(1)
*/
template <typename Object>
Object& SortedSLList<Object>::SLNode::getData() {
    return this->_data;
}

#endif // SORTEDSLLIST_H

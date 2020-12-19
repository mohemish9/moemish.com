/*
 * \file intlist.cpp
 * \authors YOUR ALIASES HERE
 * \brief Implemenation of IntList and its private classes.
*/

#include "intlist.hpp"
#include "testing-logger.hpp"

using namespace std;

IntList::IntList() 
    : back_(nullptr),
      front_(nullptr),
      size_(0)
{
    affirm(consistent() && empty());
}

IntList::~IntList()
{
 while(size_>0)
 {
     pop_front();
 }

 
}


IntList::IntList(const IntList& orig) 
    :back_(nullptr),
    front_(nullptr),
    size_(0)

{
    iterator iter = orig.begin();
    iterator endIter = orig.end();
    while(iter != endIter)
    {
        this->push_back(*iter);
        ++iter;
    }
    affirm(consistent());
    
}

void IntList::swap(IntList& rhs)
{
    // This is the canonical way to swap arbitrary types; this incantation
    // will call std::swap unless we're swapping a class that provides its
    // own swap function (like we do), in which case that swap is called.
    // Here we end up calling std::swap since the swapped parts are primitives.

    using std::swap;

    swap(back_, rhs.back_);
    swap(front_, rhs.front_);
    swap(size_, rhs.size_);
    affirm(consistent());
}

void swap(IntList& lhs, IntList& rhs) { lhs.swap(rhs); }

IntList& IntList::operator=(const IntList& rhs)
{
    // Assignment is implemented idiomatically for C++, using "the swap trick"
    IntList copy = rhs;
    swap(copy);

    affirm(consistent());
    return *this;
}


size_t IntList::size() const
{ 
    return size_;
}


bool IntList::empty() const
{
    if (size_ == 0)
    {
      return true;
    }
    else{
        return false;
    }
}



bool IntList::operator==(const IntList& rhs) const
{
  
    iterator iter = begin();
    iterator rhsIter = rhs.begin();
    iterator enditer = end();
    
    while(iter != enditer){
       if (*iter == *rhsIter){
           ++iter;
           ++rhsIter;
       }
       else{
           return false;
       }
    }
    return true;
}
bool IntList::operator!=(const IntList& rhs) const
{
    // Idiomatic code: leverage == to implement !=
    return !operator==(rhs);
}



void IntList::push_front(int pushee)
{
    
    
    Element* newFront = new Element(pushee, front_);
    front_ = newFront;
    ++size_;
    if (size_ == 1){
        back_ = front_;
    }
    affirm(consistent() && !empty());

}



int IntList::pop_front()
{
    
    
    int value = front_->value_;
    Element* temp = front_;
    front_ = front_->next_;
    delete temp;
    -- size_;
    if (size_ == 0){
        back_ = nullptr;
        front_ = nullptr;
    }
    affirm(consistent());
    return value;
}



void IntList::push_back(int pushee)
{
    Element* newBack = new Element(pushee, nullptr);
    if (size_ == 0){
        back_ = newBack;
        front_ = back_;
    }
    else{
        
        back_->next_ = newBack;
        back_ = newBack;
        
    }
    ++size_;
    affirm(consistent());
}



void IntList::insert_after(iterator where, int value)
{
    affirm(where != end());
    
    Element* newElement = new Element(value, where.current_->next_);
    where.current_->next_ = newElement;
    ++size_;
    
    if (++(++where) == end())
    {
        back_ = newElement;
    }
    affirm(consistent() && !empty());
    
}



IntList::iterator IntList::begin() const
{
    return Iterator(front_);
}



IntList::iterator IntList::end() const
{
    return Iterator(nullptr);
}


bool IntList::consistent() const
{
    return ((front_ == nullptr) && (back_ == nullptr) && (size_ == 0))
           || ((front_ == back_) && (size_ == 1))
           || ((front_ != back_) && (size_ > 1));
}

// --------------------------------------
// Implementation of IntList::Element
// --------------------------------------

IntList::Element::Element(int value, Element* next) : value_(value), next_(next)
{
    // Nothing else to do.
}

// --------------------------------------
// Implementation of IntList::Iterator
// --------------------------------------

IntList::Iterator::Iterator(Element* current) : current_(current)
{
    // Nothing else to do.
}


IntList::Iterator& IntList::Iterator::operator++()
{
   current_ = current_->next_;
   return *this;
}



int& IntList::Iterator::operator*() const
{
    return current_->value_;
}



bool IntList::Iterator::operator==(const Iterator& rhs) const
{
    return current_ == rhs.current_;
}


bool IntList::Iterator::operator!=(const Iterator& rhs) const
{
    // Idiomatic code: leverage == to implement !=
    return !(*this == rhs);
}


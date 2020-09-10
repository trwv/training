#include <iostream>
using namespace std;

class num_sequence {
public:
    virtual ~num_sequence(){};

    virtual int elem(int pos) const = 0;
    virtual const char* what_am_i() const = 0;
    static int max_elems(){return _max_elems};
    virtual ostream& print(ostream &os = cout) const = 0;

protected:
    virtual void gen_elems(int pos) const = 0;
    bool check_integrity(int pos) const;

    const static int _max_elems = 1024;
};

bool num_sequence::
check_integrity(int pos) const
{
    if (pos < 0 || pos >= _max_elems)
    {
        ceer << "!! invalid position: " << pos
             << " Cannot honor request\n";
        return false;
    }
    return true;
}

ostream& operator<<(ostream &os, const num_sequence &ns)
    {return ns.print(os);}

class Fibonacci : public num_sequence {
public:
    Fibonacci(int len = 1, int beg_pos = 1)
        : _length(len), _beg_pos(beg_pos) {}
    virtual int elem(int pos) const;
    virtual const char* what_am_i() const {return "Fibonacci";}
    
}
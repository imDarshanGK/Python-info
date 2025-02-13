import weakref

class MyClass:
    pass

my_obj = MyClass()
weak_ref_to_obj = weakref.ref(my_obj)
retrieved_obj = weak_ref_to_obj()

if retrieved_obj is None:
    print("The object has been garbage collected.")
else:
    print("The object is still alive.")
  

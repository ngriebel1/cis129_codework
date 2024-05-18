Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 55, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 53, in main
    animal = Pet.Pet()
TypeError: Pet.Pet() missing 4 required positional arguments: 'self', 'n', 't', and 'a'

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 56, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 54, in main
    animal.Animal()
AttributeError: type object 'Pet' has no attribute 'Animal'

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 56, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 54, in main
    animal.Pet()
TypeError: Pet.Pet() missing 4 required positional arguments: 'self', 'n', 't', and 'a'

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 81, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 54, in main
    animal.setName(getAsciiString("Enter a pet name: ", "That is not a valid name. "))
TypeError: Pet.setName() takes 1 positional argument but 2 were given

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: -Nick

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: 66

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: 55

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: -Nick

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: 44

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: 44
That is not a valid name. 
Enter a pet name: -Nick
That is not a valid name. 
Enter a pet name: blasphemy66
That is not a valid name. 
Enter a pet name: Rigby

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nicky
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 81, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 55, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 37, in getName
    return _name
NameError: name '_name' is not defined. Did you mean: 'self._name'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 44

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 81, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 53, in main
    animal.Pet(getAsciiString("Enter a pet name: ", "That is not a valid name. "),
NameError: name 'animal' is not defined

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 15

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 86, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 58, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 37, in getName
    return _name
NameError: name '_name' is not defined. Did you mean: 'self._name'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 86, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 54, in main
    animal = Pet(getAsciiString("Enter a pet name: ", "That is not a valid name. "),
TypeError: Pet() takes no arguments

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 86, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 54, in main
    animal = Pet(getAsciiString("Enter a pet name: ", "That is not a valid name. "),
TypeError: Pet() takes no arguments

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 86, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 54, in main
    animal = Pet.Pet(getAsciiString("Enter a pet name: ", "That is not a valid name. "),
TypeError: Pet.Pet() missing 1 required positional argument: 'a'

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 86, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 54, in main
    animal = Pet.Pet(animal, getAsciiString("Enter a pet name: ", "That is not a valid name. "),
UnboundLocalError: cannot access local variable 'animal' where it is not associated with a value

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 86, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 54, in main
    animal = Pet(getAsciiString("Enter a pet name: ", "That is not a valid name. "),
TypeError: Pet() takes no arguments

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 87, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 59, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 37, in getName
    return _name
NameError: name '_name' is not defined. Did you mean: 'self._name'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 87, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 59, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 37, in getName
    return _name
NameError: name '_name' is not defined. Did you mean: 'self._name'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 87, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 59, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 37, in getName
    return _name
NameError: name '_name' is not defined. Did you mean: 'self._name'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: dog
Enter a pet age: 10

Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 87, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 60, in main
    print(animal.getType())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 41, in getType
    return _type
NameError: name '_type' is not defined. Did you mean: 'self._type'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10


0

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: dog
Enter a pet age: 120


0

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 87, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 59, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 37, in getName
    return _petName
NameError: name '_petName' is not defined

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 87, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 59, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 37, in getName
    return _petName
NameError: name '_petName' is not defined. Did you mean: 'self._petName'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 87, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 59, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 37, in getName
    return _petName
NameError: name '_petName' is not defined. Did you mean: 'self._petName'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
<class 'str'>
<class 'str'>
<class 'int'>

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
<class 'str'>
<class 'str'>
<class 'int'>

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 87, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 59, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 37, in getName
    return _petName
NameError: name '_petName' is not defined. Did you mean: 'self._petName'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 87, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 59, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 37, in getName
    return petName
NameError: name 'petName' is not defined. Did you mean: 'self.petName'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 87, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 59, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 37, in getName
    return petName
NameError: name 'petName' is not defined. Did you mean: 'self.petName'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 87, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 59, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 37, in getName
    return petName
NameError: name 'petName' is not defined. Did you mean: 'self.petName'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
<class 'str'>
<class 'str'>
<class 'int'>

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 79, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 51, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 32, in getName
    return _petName
NameError: name '_petName' is not defined. Did you mean: 'self._petName'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 80, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 50, in main
    animal.Pet(inputName, inputType, inputAge)
TypeError: Pet.Pet() takes 3 positional arguments but 4 were given

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 80, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 52, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 32, in getName
    return _petName
NameError: name '_petName' is not defined. Did you mean: 'self._petName'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 80, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 52, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 32, in getName
    return _petName
NameError: name '_petName' is not defined. Did you mean: 'self._petName'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
<class 'str'>
<class 'str'>
<class 'int'>

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
<class 'str'>
<class 'str'>
<class 'int'>

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
<class 'str'>
<class 'str'>
<class 'int'>

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10


0

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 120
<class 'str'>
<class 'str'>
<class 'int'>

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
<class 'str'>
<class 'str'>
<class 'int'>

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Nick
<class 'str'>
<class 'int'>

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Nick
<class 'str'>
10

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
<class 'str'>
<class 'str'>
10

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
<class 'str'>
<class 'str'>
10

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
DEbug:  <class 'str'>
<class 'str'>
<class 'str'>
10

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
<class 'str'>
<class 'str'>
10

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10\
That is not a valid age. 
Enter a pet age: 10
<class 'str'>
<class 'str'>
10

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 77, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 45, in main
    animal = Pet()
TypeError: Pet.__init__() missing 3 required positional arguments: 'n', 't', and 'a'

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
<class 'str'>
<class 'str'>
10

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 109
<class 'str'>
<class 'str'>
109
<class 'str'>
<class 'str'>
109

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
<class 'str'>
<class 'str'>
10
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 80, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 51, in main
    print(animal.getName())
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 32, in getName
    return petName
NameError: name 'petName' is not defined. Did you mean: 'self.petName'?

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
<class 'str'>
<class 'str'>
10
<class 'str'>
<class 'str'>
10

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
Nick
Dog
10

===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: -10
That is not a valid name. 
Enter a pet name: FUCKYOU
Enter a pet type: STUPIDPROGRAM
Enter a pet age: 10
FUCKYOU
STUPIDPROGRAM
10
>>> 
===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Traceback (most recent call last):
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 80, in <module>
    main()
  File "C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py", line 41, in main
    animal = Pet()
TypeError: Pet.__init__() missing 3 required positional arguments: 'n', 't', and 'a'
>>> 
===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 10
The pet name is Nick
The pet type is Dog
The pet age is 10
>>> 
===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: -120
That is not a valid name. 
Enter a pet name: D!ng0
That is not a valid name. 
Enter a pet name: N!ck
That is not a valid name. 
Enter a pet name: N00
That is not a valid name. 
Enter a pet name: Nick
Enter a pet type: D0g
That is not a valid type. 
Enter a pet type: dog
Enter a pet age: -99
That is not a valid age. 
Enter a pet age: 1E-10
That is not a valid age. 
Enter a pet age: 1E+4
That is not a valid age. 
Enter a pet age: E+6
That is not a valid age. 
Enter a pet age: 00000000000
The pet name is Nick
The pet type is dog
The pet age is 0
>>> 
===================== RESTART: C:/Users/zeroa/OneDrive/Desktop/CIS129_NickGriebel_Lab12.py =====================
Enter a pet name: Nick
Enter a pet type: Dog
Enter a pet age: 5.34
That is not a valid age. 
Enter a pet age: 6 1/2
That is not a valid age. 
Enter a pet age: 6.5
That is not a valid age. 
Enter a pet age: 6
The pet name is Nick
The pet type is Dog
The pet age is 6

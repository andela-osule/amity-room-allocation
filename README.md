OFFICE SPACE ALLOCATION ![Travis Build Badge](https://travis-ci.org/andela-osule/amity-room-allocation.svg?branch=master)
=======================

This exercise models a room allocator for Andela's Amity Residence.

Rooms can be offices or living spaces.

CONDITIONS
==========

Office can occupy max. of 6 people.
Living space can occupy max. of 4 people.

Person can be fellow or staff.
Staff cannot be allocated living spaces.

TESTING THE PROGRAM
===================
```
python amity/test_amity.py
```

USING THE PACKAGE
=================

*Examples:*

* If you want data output in a file, output is stored in the output directory of the package

```
from tools import PeopleFileParser, AllocationWriter
persons = PeopleFileParser.line_to_person('filepath')
AllocationWriter.write_allocation(print_file=True)

```

* If you want data output to standard IO
```
from tools import PeopleFileParser, AllocationWriter
persons = PeopleFileParser.line_to_person('filepath')
AllocationWriter.write_allocation(print_stdio=True)
```

* Usually the case is that you want to create persons on the fly
```
from people import Person
from building import Amity
jane = Person('Jane', 'F').make_person('fellow', has_expr_interest=True)
# If the has_expr_interest isn't specified, it's set to False by default
jake = Person('Jake', 'M').make_person('staff')
Amity.add_persons(jake, jane)
```

* There is a Manager to assign persons to rooms
```
from people import Manager
Manager.assign_to_room('Person name', 'Room name')
# Both arguments passed in to the assign_to_room methods 
# must be existent objects in Amity.people_collection
```
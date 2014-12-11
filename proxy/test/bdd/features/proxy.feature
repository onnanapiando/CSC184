Feature: application that creates a proxy to interface an object
         that contains 10 million digits

         As a user I wish to know the number of references
         created out of the said object
         
         Scenario Outline: Get number of references connected to the main object
         Given I run the proxy application
         When there are already 3 created references
	 |message|
         |Created new object |
         |Count of references =  1 |
         |Using cached object  |
         |Count of references =  2 |
         |Using cached object |
         |Count of references =  3 |

	Then all references should be deleted afterwards for confirmation
	|message           |
	|Created new object|
	|Count of references =  1|
	|Using cached object|
	|Count of references =  2|
	|Using cached object|
	|Count of references =  3|
	|Called sort method with args:|
	|[('self', <__main__.Proxy object at 0x7f019632c910>), ('reverse', True)]|
	|Deleting proxy2|
	|Deleted object. Count of objects =  2|
	|The other objects are deleted upon program termination|
	|Deleted object. Count of objects =  1|
	|Number of reference_count is 0. Deleting cached object...|
	|Deleted object. Count of objects =  0|

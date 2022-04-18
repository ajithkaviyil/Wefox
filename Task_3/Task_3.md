# Task 3

- In terms of the different testing categories that describe the scope of the test, how would you describe the type of test you have just written?

	- The api task which has been automated comes under functional testing, Under functional testing its part of integration testing. In this scenarios our scope of testing are create,update and delete functionalities.
		- Create API: Different combination of creation (create functionality) of new resource can be tested.
		- Update API: Different combination of updation (update functionality) of existing resource can be tested.
		- Delete API: Delete functionality of existing resource can be tested.
	
- Outline the possibilities of automating these specific test cases in different scopes,together with a short summary of the pros and cons of each of them.

	- The existing piece of code can be modified for other scopes such as fetching details (Get Functionality) and Patch Functionality.
	- These test cases can be modified for doing Traffic/Stress testing, creating/updating n number of resources, deletion of n number of resources and the system behaviour to it.
	- These test cases can be used for testing different scenarios (Positive Testing, Negative Testing , Corner case validation , etc)
	- These test cases can be modified for creating a particular DB of requirement.

	- Pros:
		- Easy to modify and test different type of testing.
		- Quick response and less execution time reduces testing time.
		- Can be used for different use cases.
		- All the main functionalities can be tested.

	- Cons:
		- Choosing the wrong API parameter combinations can trigger faulty program states.
		- If requests are handled not in correct order, response or execution can have errors.


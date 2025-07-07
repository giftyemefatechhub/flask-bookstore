# Coding Assignment
Same problem in either go or python, pick the language you feel most conformable with.

## Go

- Install Go: https://go.dev/doc/install
- Getting started: https://go.dev/doc/tutorial/getting-started
- to run the code: go run .
- to run the tests: go test

### Good Go syntax reference
https://gobyexample.com/


## Python

- Install python 3: https://www.python.org/about/gettingstarted/
- Install required packages: pip install -r requirements.txt
- to run the code: python bookstore_assignment.py
- to run the tests: python -m unittest bookstore_assignment_test.py

### Python reference
https://docs.python.org/3/reference/index.html

## Tasks
* A unit test is failing, fix the issue in the code and make all tests pass
* Add a new endpoint to list one book by title
* Include a price field to the books struct

## Solution

I chose to complete the assignment in Python using the Flask web framework. Here's a summary of the work I did:

### Fixed a Failing Test

- One of the original tests was trying to check for a dictionary inside another dictionary using `assertIn()`, which caused an error.
- I fixed this by using `assertDictEqual()` to properly compare two dictionaries.

### Added a Price Field

- I updated the `Book` class to include a new field called `price`.
- I made sure all example data and related tests included a price value.

### Created a New Endpoint

- I added a new route: `/books/:title`, which lets users get a single book by its title.
- If the book exists, it returns the book details in JSON format. If not, it returns a 404 error.

### Added a Home Route

- I created a `/` route that returns a welcome message and a list of all available API endpoints.
- This makes it easier to understand how to use the API.

### Added a New Test

- I wrote a fourth test to make sure the new `/books/:title` endpoint works as expected.
- It checks the status code and that the data returned is correct.

### How to Run the Application

To start the Flask server:
python bookstore_assignment.py

To run the unit tests:
python -m unittest bookstore_assignment_test.py

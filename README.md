![Alt Text](https://camo.githubusercontent.com/59589bd21e8ec09ef94f2d9bb80d36d144bc487fe4737f8b213d005f3273921b/68747470733a2f2f696d6775722e636f6d2f4f696c457358562e706e67)

# 0x00. AirBnB clone - The console

This project contains the inner workings of our AirBnB clone project. This is the roots of the backend; a console that instantiate and manipulate instances of our classes, and serialize/deserialize them to/from a JSON file.

# Usage

```
To run the console, launch `./console.py` in your favorite shell.
```

## Commands

| Command | Description                                                                                                                              | Example                                                      |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| create  | Creates a new instance of a class, serializes it to the JSON file and prints its id                                                      | `(hbnb) create <class>`                                      |
| show    | Prints the string representation of an instance based on the class name and id                                                           | `(hbnb) show <class> <id>`                                   |
| destroy | Permanently deletes an instance based on the class name and id (from working memory + from JSON)                                         | `(hbnb) destroy <class> <id>`                                |
| update  | Updates an instance based on the class name and id by adding or updating attribute                                                       | `(hbnb) update <class> <id> <attribute> "<attribute value>"` |
| all     | Prints all string representation of all current instances. If a class is specified, print all instances from that specific class instead | `(hbnb) all <class>`                                         |
| help    | display help information                                                                                                                 | `(hbnb) help <command>`                                      |
| quit    | exit the program                                                                                                                         | `(hbnb) quit`                                                |
| EOF     | exit the program                                                                                                                         | `(hbnb) ctrl+D`                                              |

All previous commands are also available under the format `<class>.cmd(params)`:

| Command | Description                                                                                                                              | Example                                                      |
| create() | Creates a new instance of a class, serializes it to the JSON file and prints its id | `(hbnb) <class>.create()` |
| show() | Prints the string representation of an instance based on the class name and id | `(hbnb) <class>.show("<id>")` |
| destroy() | Permanently deletes an instance based on the class name and id (from working memory + from JSON) | `(hbnb) <class>.destroy("<id>")` |
| update() | Updates an instance based on the class name and id by adding or updating attribute | `(hbnb) <class>.update("<id>", "<attribute>", "<value>")` |
| update(dict) | Update can also take a dictionary of key-value attributes | `(hbnb) <class>.update("<id>", {"<attribute1>": "<value2>", "<attribute2>": "<value2>"}")` |
| all() | Prints string representation of all instances based on the class name | `(hbnb) <class>.all()` |

Additionnally, an exclusive `<class>.count()` function can be called only from its class name:

| Command | Description                                                                                                                              | Example                                                      |
| count() | Show the number of instance created | `(hbnb) <class>.count()` |

## Examples

Create an instance of User class:

```
(hbnb) create User
613293f9-4a00-40a9-a855-6c8eefdf4826
```

Show the instance linked to the id `613293f9-4a00-40a9-a855-6c8eefdf4826`

```
(hbnb) User.show(613293f9-4a00-40a9-a855-6c8eefdf4826)
[User] (613293f9-4a00-40a9-a855-6c8eefdf4826) {'created_at': datetime.datetime(2021, 2, 19, 8, 55, 7, 163635), 'updated_at': datetime.datetime(2021, 2, 19, 8, 55, 7, 163676), 'id': '613293f9-4a00-40a9-a855-6c8eefdf4826'}
```

Update the User `613293f9-4a00-40a9-a855-6c8eefdf4826` with `first_name` Betty and `last_name` Holberton, from a dict:

```
(hbnb) User.update(613293f9-4a00-40a9-a855-6c8eefdf4826, {"first_name": "Betty", "last_name": "Holberton"})
(hbnb) User.show(613293f9-4a00-40a9-a855-6c8eefdf4826)
[User] (613293f9-4a00-40a9-a855-6c8eefdf4826) {'updated_at': datetime.datetime(2021, 2, 19, 8, 57, 32, 813444), 'created_at': datetime.datetime(2021, 2, 19, 8, 55, 7, 163635), 'last_name': 'Holberton', 'id': '613293f9-4a00-40a9-a855-6c8eefdf4826', 'first_name': 'Betty'}
```

Count all instances of User class:
```
(hbnb) User.count()
1
```

Destroy the User `613293f9-4a00-40a9-a855-6c8eefdf4826`
```
(hbnb) destroy User 613293f9-4a00-40a9-a855-6c8eefdf4826
(hbnb) all User
[]
(hbnb)
```

## Author

Thibaud PONCIN

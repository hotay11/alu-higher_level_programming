# JavaScript - Web scraping

This project covers reading and writing files with the `fs` module, making HTTP requests with the `request` module, and manipulating JSON data in Node.js.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Interpreted on Ubuntu using `node`
- All files end with a new line
- The first line of every file is exactly `#!/usr/bin/node`
- Code is `semistandard` compliant
- All files are executable
- No use of `var`

## Setup

Install the `request` module and set the module path:

```
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```

Install the linter:

```
sudo npm install semistandard --global
```

Make the scripts executable:

```
chmod +x *.js
```

## Files

| File | Description |
| --- | --- |
| `0-readme.js` | Reads and prints the content of a file (utf-8). Prints the error object on failure |
| `1-writeme.js` | Writes a string to a file (utf-8). Prints the error object on failure |
| `2-statuscode.js` | Prints the status code of a GET request as `code: <status code>` |
| `3-starwars_title.js` | Prints the title of a Star Wars movie given its ID |
| `4-starwars_count.js` | Prints the number of movies where "Wedge Antilles" (character ID 18) appears |
| `5-request_store.js` | Fetches a webpage and stores the body in a file (utf-8) |
| `6-completed_tasks.js` | Prints the number of completed tasks per user ID |

## Usage

```
./0-readme.js cisfun
./1-writeme.js my_file.txt "Python is cool"
./2-statuscode.js https://alu-intranet.hbtn.io/status
./3-starwars_title.js 1
./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
./5-request_store.js http://loripsum.net/api loripsum
./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
```

## Author
joshua hotay

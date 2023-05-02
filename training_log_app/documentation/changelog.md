# Changelog

## Week 3
- Added UserReposityory and LogEntryRepository classes, which are responsible for connections with database
- Added User and LogEntry classes, which describe the objects
- Added database connection
- Added configuration files for filesystem and database
- User can be created and saved to database, before saving password is hashed
- Log entries can be saved to database and a couple tests for that


## Week 4
- Created user interface for adding new log entries
- User can add a new entry and it is stored in database
- User can create new accounts and save them to the database
- User can then log in to those accounts
- User can use the program with the ui and can go to different windows
- Created appropriate tests and code quality checks

## Week 5
- User can see some simple statistics on the main page
- User can see latest entry on the main page
- Made significant improvements to user interface
- User can now select date with a calendar widget
- User can see more specific statistics of training, not finished

## Week 6
- User can see a graph of weekly training sessions from current year in the statistics tab
- All necessary input validation completed
- User can browse their logs in a separate page
- Changed database structure to have log_ids for each user
- Significantly improved UI with styling
- Improved architecture documentation
- Created user manual
- Code has proper docstring

## Week 7
- Created new classes AppStyle, NightMode and Daymode for controlling UI style
- User can now change between these themes with a button on the main page


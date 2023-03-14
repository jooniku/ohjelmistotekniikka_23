# Requirement specification

## Purpose of the app
With the app, users can keep track and get useful data from their martial arts training. Each user has their unique, private data.

## Users
Currently there are no admin users, though that might be created. The only usertype is normal user.

## User interface draft
![image](https://user-images.githubusercontent.com/101401566/225024165-f36fcf74-07ad-4cdf-b36f-de9dda515306.png)
The app opens up to a login page where user can log in or create a new account. After login they can view their training data.

## Functions of the basic version
### Before login
- User can register a new account
  - Username must be unique and has some specifications like minimum length of 2 and max length of 10
- User can log in with correct username and password
- If log in is not successful, user is notified

### After login
#### Main page
- User can see statistics of their training data
  - The data on the from page might be *total hours trained* etc. and the precentage of goals (explained below) achieved
- User sees last entry on the front page (or a part of it)
  - Perhaps users has a goal for each next training session and can see the goal
- User can add new entries
- User can view more specific data
#### New entry page
- User specifies information about a training session they had such as:
  - Date
  - Duration
  - Type e.g. sparring, boxing, wrestling etc.
  - What techniques did user practice and what are some key concepts to remember about it
  - What went well in the session
  - What did not go well and why
  - A goal for next session e.g. get 3 sweeps from half-guard etc.
  - Did the user achieve the previously set goal

## Further development
After the completion of the basic version, these are some improvements to consider
- User can get some kind of analysis of training data to their email
- User can edit previous entries
- Introduction of admin user
- Training groups that can have the same goals etc.
- Injury tracking

# Requirement specification

## Purpose of the app
With the app, users can keep track and get useful data from their martial arts training. Each user has their unique data.

## Users
The only usertype is normal user.

## User interface draft
![image](https://user-images.githubusercontent.com/101401566/225024165-f36fcf74-07ad-4cdf-b36f-de9dda515306.png)
The app opens up to a login page where user can log in or create a new account. After login they can view their training data.

## Functions of the basic version
### Before login
- User can register a new account, password is hashed before storing it
- User can login with correct username and password
- If login is not successful, user is notified

### After login

#### Main page
- User can see simple statistics of their training data
- User sees their latest entry on the front page
- There are several pages user can go into from the main page
	- User can add new entries
	- User can browse their entries
	- User can view more specific data

#### New entry page
- User specifies information about a training session they had such as:
  - Date
  - Duration
  - Type e.g. sparring, boxing, wrestling etc.
  - What went well in the session
  - What did not go well and why
  - A goal for next session
  - Did the user achieve the previously set goal

#### Browsing log entries
- User can browse their log entries

#### Statistics
- User can view more specific statistics of their training data

#### Other
- User can change the theme of the application
- User can log out

## Further development
#### After the completion of the basic version, these are some improvements to consider:
- User setting tab, where user might change password etc.
- User can edit previous entries
- Introduction of admin user
- Training groups that can have the same goals etc.
- Injury tracking

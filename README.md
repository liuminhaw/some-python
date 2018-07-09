# Some Python Program
Some python programs that may or may not make life easier

## Programs

### password_generator
Randomly generate password for use  
Use `length=LENGTH` to assign password length, default value is 15  
`symbols` argument to include symbol characters in new created password

    password_generator [length=LENGTH] [symbols]


## Classes

### logging_class
#### Version 1.0.0
Logging class for use in other python programs

    PersonalLog(name)
    PersonalLog.debug(message)
    PersonalLog.info(message)
    PersonalLog.warning(message)
    PersonalLog.error(message)
    PersonalLog.critical(message)

### user_agent_class
#### Version 1.0
User-agent header for web scraping

##### UserAgent.random_computer()
Randomly return an user-agent value that is used by computer

    UserAgent.random_computer()

##### UserAgent.random_phone()
Randomly return an user-agent value that is used by phone

    UserAgent.random_phone()

##### UserAgent.write_computer()
Save computer use user-agent headers data to file

    UserAgent.write_computer()

##### UserAgent.write_phone()
Save phone use user-agent headers data to file

    UserAgent.write_phone()

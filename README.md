# Some Python Program
Some python programs that may or may not make life easier

## Program

### image_modify

##### compress
Compress image in **jpeg** format  
`QUALITY` should be value between 1 and 95

    image_modify compress INPUTFILE [QUALITY]

### password_generator
Randomly generate password for use  
Use `length=LENGTH` to assign password length, default value is 15  
`symbols` argument to include symbol characters in new created password

    password_generator [length=LENGTH] [symbols]


## Class

### logging_class
Logging class for use in other python programs

    PersonalLog(name)
    PersonalLog.debug(message)
    PersonalLog.info(message)
    PersonalLog.warning(message)
    PersonalLog.error(message)
    PersonalLog.critical(message)

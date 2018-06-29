# Some Python Program
Some python programs that may or may not make life easier

## Programs

### image_modify

##### compress
Compress image in **jpeg** format.  
`QUALITY` should be value between 1 and 95.  
Default value of `QUALITY` is `75` if not specified.

    image_modify compress INPUTFILE OUTPUTFILE [QUALITY]

##### resize
Resize image's width and height by dividing to `PROPORTION`.  
`PROPORTION` should be a positive integer.  
Default value of `PROPORTION` is `2` if not specified.   

    image_modify resize INPUTFILE OUTPUTFILE [PROPORTION]


### password_generator
Randomly generate password for use  
Use `length=LENGTH` to assign password length, default value is 15  
`symbols` argument to include symbol characters in new created password

    password_generator [length=LENGTH] [symbols]


## Classes

### logging_class
Logging class for use in other python programs

    PersonalLog(name)
    PersonalLog.debug(message)
    PersonalLog.info(message)
    PersonalLog.warning(message)
    PersonalLog.error(message)
    PersonalLog.critical(message)

### user_agent_class
User-agent header for web scraping

##### UserAgent.load_random()
Randomly return an user-agent value

    UserAgent.load_random()

##### UserAgent.write_file()
Save user-agent headers data to file

    UserAgent.write_file()

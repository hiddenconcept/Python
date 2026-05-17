emails = [
    'johndoe@gmail.com',
    'alice7684@icloud.com',
    'micheal_smith@outlook.com',
    'pythonlover@hotmail.com',
    'java_style_87957@icloud.com',
    'dev.user@bell.net',
    'coderhub@fastmail.com',
    'data_sceience_87957@gmail.com',
    'machinelearningglobaly@fastinternet.com',
    'techworld@rogers.com',
    'fastcars@g7.com'
]

usernames = [email.split("@")[0] for email in emails]


print("\nDatabase Of Emails:\n",emails)
print("\nThe Usernames Without The Mail Provider:\n",usernames)
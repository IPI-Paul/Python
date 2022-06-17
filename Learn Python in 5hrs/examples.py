def regex_example():
    import re
    regex = re.compile(r"(\s*)(:)(\s*)").match(" : ")
    print(regex.group(2))


def os_example():
    import os
    print(os.name)


def logging_example():
    import logging
    logger = logging.getLogger("MAIN")
    logger.error("Error happened in the app")


def user_example():
    from user import User
    from post import Post

    app_user_one = User("nn@nn.com", "Nana Janashia", "pwd1", "DevOps Engineer")
    app_user_one.get_user_info()
    """app_user_one.change_job_title("DevOps Trainer")
    app_user_one.get_user_info()"""

    app_user_two = User("aa@aa.com", "James Bond", "supersecret", "Agent")
    app_user_two.get_user_info()

    new_post = Post("On a Secret mission today", app_user_two.name)
    new_post.get_post_info()


user_input = None
while user_input not in ["", "q"]:
    examples = ["regex_example", "os_example", "logging_example", "user_example"]
    msg = "> " if user_input is not None else """
Please enter the exercise number to run!
1) Use Regular Expression to remove spaces before and after colon
2) Print the Operating System Name 
3) Print an Error Message using the Builtin Logging Module
4) User the Classes User and Post to view prepopulated Users and Posts
h) Show Help List
type q or just enter to quit
> """
    user_input = input(msg)
    if user_input in ["", "q"]:
        print("All done, bye ;D")
        continue
    elif user_input == "h":
        user_input = None
        continue
    elif user_input not in ["1", "2", "3", "4"]:
        print(f"Your entry {user_input} is not one of the specified values!{msg}")
        user_input = None
        continue
    eval(f"{examples[int(user_input) - 1]}()")

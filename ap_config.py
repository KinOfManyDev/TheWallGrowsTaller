"""
Config settings for '/u/TheWallGrowsTaller' reddit bot
"""
import random

USERNAME = 'USERNAME_HERE'                  # Bot's username
PASSWORD = 'PASSWORD_HERE'                  # Bot's password
user_agent = "USERAGENT_HERE"               # Bot's agent
sleep_length = 5                            # Sleep /r/subreddit/comments refresh
subreddit = "The_Donald+HillaryForPrison"   # Subreddit(s) to scan

def get_bot_message():
    """ Get the message template. """
    with open("message_template.txt", "r") as f:
        return f.read()

def get_triggers():
    """ Get a list of triggers. """
    with open("triggers.txt", "r") as f:
        return f.read().split('\n')

def get_phrases():
    """ Get a list of phrases. """
    with open("phrases.txt", "r") as f:
        return f.read().split('\n')

def get_replied():
    """ Get a list of replied-to comments. """
    with open("replied.txt", "r") as f:
        return f.read().split('\n')

def set_replied(string):
    """ Add a comment to the list of replied-to comments. """
    with open("replied.txt", "a") as f:
        f.write(string + '\n')

def get_wall_height():
    """ Get the current height of the wall. """
    with open("wall.txt", "r") as f:
        return int(f.read())

def get_target_height():
    """ Get the goal height. """
    with open("target.txt", "r") as f:
        return int(f.read())

def set_wall_height(int):
    """ Set the current height of the wall. """
    with open("wall.txt", "w") as f:
        f.write(str(int))

def comment_content():
    """ Honestly, not sure why this is here.. Mostly for get_bot_message() is pretty good on it's own. """
    return get_bot_message()

def sentences():
    """ Randomly select a sentence from the list returned in get_phrases() """
    sentences_list = get_phrases()
    sentence_index = random.randint(0, len(sentences_list) - 1)
    return sentences_list[sentence_index]
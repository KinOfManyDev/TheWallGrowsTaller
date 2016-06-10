"""
    Run through comments in a subreddit,
    look for triggers, and if a trigger is found,
    increase the height of the wall by 10 & post a new comment.
"""
import praw
import time
import logging

import ap_config

# For logging purposes
logger = logging.getLogger(__name__)

# User agent setup + login
r = praw.Reddit(user_agent=ap_config.user_agent)
r.login(ap_config.USERNAME, ap_config.PASSWORD)

def buid_the_wall():
    """ building starts here """
    subreddit = r.get_subreddit(ap_config.subreddit)
    try:
        sub_comments = subreddit.get_comments()
        for comment in sub_comments:
            ''' for every comment in the fetched comments, look for a trigger in the list of triggers '''
            comment_text = comment.body.lower()
            is_triggered = False
            for trigger in ap_config.get_triggers():
                if trigger in comment_text:
                    ''' if trigger is found in the comments, is_triggered is True '''
                    is_triggered = True
                    break

            if comment.id not in ap_config.get_replied() and is_triggered and (str(comment.author) != ap_config.USERNAME):
                ''' if the comment was not replied to, a trigger is found, and the author of the comment is not me, reply '''
                print("---")
                print("Trigger found. Comment ID: {} by {}".format(comment.id, str(comment.author)))
                try:
                    # THE WALL JUST GOT 10 FEET HIGHER!
                    new_height = ap_config.get_wall_height() + 10
                    target_height = ap_config.get_target_height()
                    comment.reply(ap_config.comment_content().format(ap_config.sentences(),
                                                                     new_height,
                                                                     float("{0:.3f}".format((new_height / target_height) * 100)),
                                                                     target_height - new_height))
                    print("Replied.")
                    ap_config.set_replied(comment.id)
                    ap_config.set_wall_height(new_height)
                    print("ID logged.\n   Searching again...")
                except Exception:
                    logger.warning("Reply failed!", exc_info=True)
    except Exception:
        logger.exception("Couldn't pull comments from subreddit", exc_info=True)

while True:
    buid_the_wall()
    # Sleep between queries to prevent excessive calls to the Reddit servers
    time.sleep(ap_config.sleep_length)
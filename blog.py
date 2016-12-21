#!/usr/bin/python
# blog draft vim_tricks
# if there is a draft file with vim_tricks in the name, edit it
# otherwise, start a new draft file
import re
import argparse
import os
import sys
import datetime
import shutil
import subprocess as sp

website = "www.weaselpipe.com"
script_path = os.path.dirname(os.path.realpath(__file__))

class FileNotFoundError(Exception): pass
class MultipleFilesFoundError(Exception): pass

def find_subdir(tld_path, name):
    """ Find subdirectory name somewhere below the tld_path """
    # http://stackoverflow.com/a/8922151
    queue = []
    queue.append(tld_path)
    while queue:
        path = queue.pop(0)
        subdirs = next(os.walk(path))[1]
        if name in subdirs:
            return os.path.join(path,name)
        for d in subdirs:
            queue.append(os.path.join(path,d))

def find_file(path, pattern):
    """ file with pattern in name located in exact path """
    files = next(os.walk(path))[2]
    # Find all files that match
    files = [f for f in files if f.find(pattern) > -1]
    if len(files) < 1:
        raise FileNotFoundError("File not found")
    elif len(files) > 1:
        raise MultipleFilesFoundError("Name matches more then one file:\n%s\nPlease try again with a more specific name." % ", ".join(files)) 
    else:
        return files[0]

def edit_file(path):
    os.system('%s %s' % (os.getenv('EDITOR'), path))

def prompt_yesno(msg):
    res = raw_input("%s [Y/n] " % msg)
    if res in ["y","Y"]:
        return True
    return False

def cmd_draft(pattern):
    drafts_path = find_subdir(script_path, "drafts")
    try:
        file_name = find_file(drafts_path, pattern)
        # one file found - edit an existing draft
        if not prompt_yesno("Edit '%s'?" % file_name):
            exit(0)
        edit_file(os.path.join(drafts_path, file_name))
        print "Saving changes to file."
        git_stage(os.path.join(drafts_path, file_name))
        cmd_git_push()
        print "done"
        print "View draft at %s/drafts/%s" % (website, file_name[:-3])

    except FileNotFoundError:
        # Make a new draft
        print "No drafts found matching pattern '%s'." % pattern
        cmd_new(pattern)
    except MultipleFilesFoundError as e: 
        print e

def cmd_edit(pattern):
    posts_path = find_subdir(script_path, "_posts")
    try:
        file_name = find_file(posts_path, pattern)
        # one file found - edit existing post
        if not prompt_yesno("Edit '%s'?" % file_name):
            exit(0)
        edit_file(os.path.join(posts_path, file_name))
        print "Saving changes to file."
        git_stage(os.path.join(posts_path, file_name))
        cmd_git_push()
        print "done"
    except FileNotFoundError:
        print "No existing posts found matching pattern '%s'." % pattern
    except MultipleFilesFoundError as e: 
        print e



def cmd_new(name, datestr=None):
    drafts_path = find_subdir(script_path, "drafts")
    if datestr is None:
        datestr = datetime.datetime.today().strftime("%Y-%m-%d")
    name = name+".md" if not name[-3:] == ".md" else name
    file_name = "%s-%s" % (datestr, name)
    if not prompt_yesno("Create new file '%s'?" % file_name):
        exit(0)
    target_file_path = os.path.join(drafts_path, file_name)
    template_file = "0000-00-00-template.md"
    if not os.path.isfile(os.path.join(drafts_path, template_file)):
        print "Error: Could not find template file."
        exit(0)
    shutil.copyfile(os.path.join(drafts_path, template_file), target_file_path)
    if not os.path.isfile(target_file_path):
        print "Error: file could not be created."
        exit(0)
    edit_file(target_file_path)
    print "Saving file."
    cmd_git_push()

def cmd_post(pattern):
    drafts_path = find_subdir(script_path, "drafts")
    posts_path = find_subdir(script_path, "_posts")
    try:
        file_name = find_file(drafts_path, pattern)
        # one file found - edit an existing draft
        if not prompt_yesno("Release draft '%s' as Post?" % file_name):
            exit(0)
        shutil.move(os.path.join(drafts_path, file_name),
                    os.path.join(posts_path, file_name))
        #TODO: we need to git mv the file
        cmd_git_push()
        print "done"
    except FileNotFoundError:
        # Make a new draft
        print "No drafts found matching pattern '%s'." % pattern
        exit(0)
    except MultipleFilesFoundError as e: 
        print e
        exit(0)

def git_stage(path):
    print "Staging changes in git."
    sp.check_call(["git","add",path])

def git_pull():
    print "Checking for remote updates..."
    ret = sp.check_call(["git","pull","origin","master"])
    print "Check:",ret
    print ""

def cmd_git_push():
    """ push changes"""
    if not prompt_yesno("Push changes?"):
        print "Changes have been left uncommitted."
        exit(0)
    print "Pushing Changes"
    # TODO: Make this more meaningful
    sp.check_call(["git","commit", "-m", "\"adds changes\""])
    sp.check_call(["git","push","origin","master"])
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", type=str, choices=["new", "draft", "publish", "post", "push", "edit"])
    parser.add_argument("name", type=str)
    args = parser.parse_args()
    git_pull()
    if args.cmd == "draft":
        cmd_draft(args.name)
    elif args.cmd == "new":
        cmd_new(args.name)
        cmd_draft(args.name)
    elif args.cmd == "push":
        cmd_git_push()
    elif args.cmd == "post":
        cmd_post(args.name)
    elif args.cmd == "edit":
        cmd_edit(args.name)



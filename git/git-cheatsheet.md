# LOCAL COMMANDS

## STANDARD COMMANDS


* `git commit`: Commits the things in the staging area

* `git branch <newBranch>`: Creates a branch named 'newBranch' from the current HEAD

Note: this command does not check out the new branch, so if we had master branch pointing to the same commit as 'newBranch' and do a commit, HEAD will point to master

* `git merge <otherBranch>`: Merges the current branch we are on with 'otherBranch'

Creates a new, so called merge-commit

* `git rebase <otherBranch>`: Rebases the current branch we are on onto 'otherBranch'

* `git rebase <newBase> <branch_to_rebase>`: Rebases branch_to_rebase onto newBase

* `git rebase -i (--interactive) <otherBranch>`: Rebases current branch interactively to 'otherBranch'

Same as rebase but we can control everything like dropping commits, squashing commits, rewrite commit messages.
We can also reorder the commits on the branch.
Useful when a Change-Id (gerrit) is missing from the commit message.

* `git tag -a v1.2 9fceb02 -m "Message here"`: Tag a specified commit or refspec (9fceb02) with "v1.2"

## MOVE COMMANDS

* `git checkout 'newBranch'`: Checks out the given branch (actually moves HEAD to the specified branch or refspec)

We can make a commit to that branch after this command.
Accepts any of the refspecs below:

`^` : moving upwards in the tree

`~<num>` : moving upwards a number of times

`^<num>` : specifies which parent reference to follow (merge commits)


#### git checkout examples
* `git checkout master^`: Checks out the first parent of master
* `git checkout master^`: Checks out (moves HEAD to) the first parent of master
* `git checkout HEAD^`: Checks out (moves HEAD to) the first parent of HEAD
* `git checkout HEAD~4`: Checks out the 4th commit from HEAD upwards (4th level parent)
* `git checkout HEAD~`: Checks out HEAD's parent
* `git checkout HEAD^2`: Checks out the second parent of HEAD
* `git checkout HEAD~2`: Checks out the grandparent of HEAD
* `git checkout HEAD~^2~2`: Does all the things as above but in one concise command (combining refspecs)

#### Combining refspec with branch moving

* `git checkout -f <branchName> <refspec>`: Moving branch pointer to specific commit or refspec
* `git checkout -f master HEAD~3`: Moves the master branch to grand-grandparent of HEAD

## REVERSING COMMANDS

* `git reset`: Resets HEAD to the specified commit [this is for local branches]

* `git reset HEAD~2`: Resets HEAD to the grandparent of HEAD (undoes 2 commits)

* `git revert`: Creates a new commit that removes the changes introduced by the specified commit

Practical to use on remote branches when others pulled the changes and rebase is not possible.

* `git reset HEAD <filename>`: Unstages a staged file

If we add a file accidentally with git add <filename> we can remove it from the staged area with this command
Modifications are preserved in the unstaged area.

*  `git checkout -- <filename>`: Throws away any changes made to the specified file after the last commit.

Can be dangerous!

* `git cherry-pick`: Picks arbitrary commit(s) from any location (without any order) to the current branch (or HEAD)

Useful when we know what commits we exactly need.


# REMOTE COMMANDS

* `git clone`: Makes a connection between the local and the remote repo

Downloads all the content of the remote repository to a local machine.

## SET UP TRACKING

* `git checkout -b serverfix origin/serverfix`: Checks out a new local branch named 'serverfix' from origin/serverfix remote branch

The local branch will automatically created as a track branch to origin/serverfix
All push/pull operations will be automatically go to origin/serverfix from this local branch

* `git branch -u <remote_branch_to_track> <local_branch>`: Assigns the local branch to track the specified remote branch
* `git checkout --track origin/serverfix`: Same as above, except we cannot specify the local branch name, so it will be the same as the remote branch name
* `git push origin <local_branch_name>:<destination_remote_branch>`: Pushes changes from source local branch to the destination remote branch. Source can be any refspec e.g. foo^ (parent of the commit pointed by the foo branch)
* `git push`: Adds the local changes to the remote repository (uploads the commits). Works if we are on a tracking branch since we did not specify the source branch and the destination branch

#### git push examples
* `git push origin serverfix`: pushes the local serverfix branch (existing) to the remote. If it was not exist, it will create a remote serverfix branch
* `git push origin serverfix:serverfix`: does the same as the above command, more explicit
* `git push origin serverfix:awesomebranch`: pushes the local serverfix branch to the remote branch called 'awesomebranch'. 'awesomebranch' will be created if not exist
* `git push origin :side`: pushing nothing to origin's side branch. Technically this command delete the side remote branch

#### Disable git push for an origin
https://stackoverflow.com/questions/10260311/git-how-to-disable-push
`git remote set-url --push origin no_push`

### Fetch / Pull

* `git fetch`: Downloads all the commits from the remote onto all the remote branches
Generic form: `git fetch <remote_name> <branch_to_fetch_from>:<local_branch_to_fetch>`
  * Gets all the changes from all branches on the specified remote (e.g. origin) and moves the remote branches to the updated positions locally
  * Downloads all the commits that the remote has but we don't have
  * Updates where our remote branches point
  * It will NOT update any local branch (e.g. master)

* `git fetch origin foo:bar`: Turns off the 'safety-net' described above and gets all changes from the remote foo branch to the local bar branch

The origin/foo will not be updated.
If bar does not exist, git makes the destination branch (bar) prior to fetch.

* `git fetch origin :bar`: Fetches nothing to the local bar branch. Weird stuff, it actually creates a new branch named 'bar'

* `git pull`: git fetch + git merge in one command. It is important which branch we are on because it will be merged with the newly refreshed origin/<branch>
Generic form: `git pull <remote_name>:<remote_branch_name>`

* `git pull origin master`: Pulls everything from the remote master branch to the local origin/master remote branch. 
Then merges origin/master to where we were before the operation

e.g. if we were standing on the local 'bar' branch, origin/master will be merged with 'bar' and HEAD will point to 'bar'
* `git pull origin master:foo   (current branch: bar)`: Pulls all changes from master to the local foo branch
  * creates a local branch named 'foo'
  * downloads all commits from remote's master to that branch 'foo'
  * merges the foo branch to the locally checked out 'bar'

# VIEWING HISTORY

* Get commits touched a range of lines in a specific file (between lines 52 and 63): `git blame -L52,+11 -- path/to/file`
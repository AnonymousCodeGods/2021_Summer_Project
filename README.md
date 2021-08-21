# 2021_Summer_Project introduction
This repo is for code storage of 2021 SE summer project

please notice the following requirements:

* main branch is for stable version of the software, cannot be pushed without permissions. If you have done finish your part, please raise a *pull request* for others to review and then it can be merged into main branch.
* whenever you want to develop a new feature, please pull from master or other branches to your local machine and then you can work on it. 
* when there is an update on the main branch, please merge the update to your local machine.

# Commands

```yaml

local_commands:
  #create branch:
  git checkout -b local_branch_name
  #update changes to local branch:
  git add --all
  git commit -m "changes you made"
  git push origin remote_branch_name
  #warning: local_branch_name and remote_branch should be the same.
  #merge master branch to specific local branch:
    #on local main:
    git pull
    git checkout local_branch_name
    #on local branch which you want to merge in:
    git merge main

```
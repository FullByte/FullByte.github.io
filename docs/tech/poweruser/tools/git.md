# Git

![xkdc-git](_xkdc-git.png)

## Tools

- Github quick stats: <https://github.com/arzzen/git-quick-stats>
- [tig](https://github.com/jonas/tig) helps to colorize the git output
- [grv](https://github.com/rgburke/) is nice to view repos
- [lazygit](https://github.com/jesseduffield/lazygit) is a simple terminal UI for git commands
- A collection of [.gitignore](https://github.com/github/gitignore) templates

## Setup

### Basics

Set global user name and email (remove --global flag for specific repo only):

``` sh
git config --global user.name "0xfab1"
git config --global user.email "f@bi.an"
```

View current config: ```git config --global --list```

### Setup SSH login

Create new key

``` sh
ssh-keygen -t ed25519
Check if service is running and add key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
ssh-add -l
```

Copy this to [github](https://github.com/settings/ssh/new)

``` sh
cat ~/.ssh/id_ed25519.pub
```

Test connection to github

``` sh
ssh -T git@github.com
```

Test to clone, commit and push on a repo

``` sh
git clone git@github.com:FullByte/git-test.git
cd git-test/
nano script.sh
chmod u+x script.sh
git add script.sh -f
git commit -m "adding script"
git push
```

## Commands

- Get all authors: ```git log | Where { $_ -match "Author" } | Select-Object -unique```
- Download a specific branch: ```git clone -b dependabot/npm_and_yarn/pug-3.0.1 https://github.com/microsoft/project-nodejs-express-webapp/```

Clean up

- Delete all the objects w/o references: ```git prune --progress``` add ```--dry-run``` for a test
- Aggressively collect garbage: ```git gc --aggressive```

## Remove Tags

Run this in your local repository of which you want to remove a tag/tags:

``` sh
git fetch
git tag
git tag -d {tag-name}
git push origin :refs/tags/{tag-name}
```

## .gitignore

Git ignores .gitignore with .gitignore in .gitignore

Init a new repository and added a `.gitignore` file containing ".gitignore" to instruct git to igntore the `.gitignore` file. Example:

``` sh
git init .
echo ".gitignore" > .gitignore
git status
```

Result:

``` txt
On branch trunk
No commits yet
nothing to commit (create/copy files and use "git add" to track)
```

## Pretend to be busy

Do this on a clean machine

``` sh
git config --global user.email "f@bi.an"
git config --global user.name "Busy Bee"
```

Clone an empty new repostory e.g.:

``` sh
git clone https://github.com/FullByte/git-test
cd git-test
```

Run the script to create a commit for every day... e.g. since 1999.

``` sh
nano script.sh
chmod u+x script.sh
./script.sh
```

??? details "script.sh"
    ``` sh
    for Y in {2018..2020}
    do
    mkdir $Y
    cd $Y
    for M in {01..12}
    do
        mkdir $M
        cd $M
        for D in {01..28}
        do
            mkdir $D
            cd $D
            for i in {01..12}
            do
                echo "$i on $M/$D/$Y" > commit.md
                export GIT_COMMITTER_DATE="$Y-$M-$D 12:$i:00"
                export GIT_AUTHOR_DATE="$Y-$M-$D 12:$i:00"
                git add commit.md -f
                git commit --date="$Y-$M-$D 12:0$i:00" -m "$i on $M $D $Y"
            done
            cd ../
        done
        cd ../
    done
    cd ../
    done
    git push
    #optional: delete stuff
    #git rm -rf 20**
    #git rm -rf 19**
    #git commit -am "cleanup"
    #git push
    ```

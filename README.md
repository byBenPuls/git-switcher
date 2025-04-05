# Git Switcher

This simple tool provides feature for switching between git accounts

### How to use?

If you have 2 or many git accounts, you can switch between accounts using this tool

1. Create ~/.git-switch and paste the values

Paste username like in `git config --list`:

```
myGitAccountName=my_github_token
```

2. Write `git config credential.helper store`

3. Use Git Switcher
Tool will find your git config account name and will compare with .git-switch data. If the account was found, the utility will enter the password into the git itself.


**Example:**

You work in Repo A using git account A, after that you want to start work in new Repo B, using account B. For that follow the instructions:

1. In repo B write this:

```
git config --local user.name your_account_b
git config --local user.email your-email@account.com
```

2. For ~/.git-switch write:

```
account_a=token1
account_b=token2
```

3. Use tool (every time when you want to start working with the repository using the credentials from `git config --local`)

If successful, prints:

```
In current repo your credentials: YourAccount <your@mail.com>
New password for YourAccount successfully activated!
```

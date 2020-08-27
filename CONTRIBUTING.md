# Contributing to this repo

:+1: :tada: First off, thanks for taking the time to contribute! :tada: :+1:


# Issues

Issues are very valuable to this project.

* Ideas are a valuable source of contributions others can make
* Problems show where this project is lacking
* With a question you show where contributors can improve the user experience

Thank you for creating them.

## Guidlines

### 1. Fork & create a branch

```shell
# Clone your fork of the repository
git clone https://github.com/<your-username>/CTF-Website-Template-2020

# Navigate to the newly cloned directory
cd CTF-Website-Template-2020

# Assign the original repo to a remote called "upstream"
git remote add upstream https://github.com/<your-username>/CTF-Website-Template-2020
```
If this is something you think you can fix, then fork and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

```shell
git checkout -b 325-add-japanese-translations
```

When merging pull requests, your commits will be squashed. So make sure you explain your pull requests properly. More about [Pull Requests here](#Pull-Requests)

### 2.  Did you find a bug?

Ensure the bug was not already reported by searching on GitHub under [Issues](https://github.com/ashawe/CTF-Website-Template-2020/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc).

If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/ashawe/CTF-Website-Template-2020/issues/new). Be sure to include a title and clear description, as much relevant information as possible, and a code sample or an executable test case demonstrating the expected behavior that is not occurring.

### 3. Implement your fix or feature

*    At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first 😸
*    Write a good commit message. To write good commit messages, please follow [these recommendations](https://github.com/ashawe/CTF-Website-Template-2020/blob/master/COMMIT-GUIDLINES.md). There are important to maintain an healthy commit logs.
*    If there are multiple commits in your pull request, these commits will be squashed before merging. Please make sure, if that's the case, that your pull request has a nice description explaining what it does.
*    It's okay to have work-in-progress pull requests. Add [WIP] in the title of your pull request if that's the case, otherwise your pull request will be considered in a state of being able to be merged as is.


### 4. Commit and push changes

```shell
git add .
git commit -m <message>
git push
```

### Make sure your 'message' follows [these](https://github.com/ashawe/CTF-Website-Template-2020/blob/master/COMMIT-GUIDLINES.md) standards.

### 5. Create a pull request

Use GitHub to [create a pull request](https://help.github.com/en/desktop/contributing-to-projects/creating-a-pull-request) for your branch. In your pull request description, be sure to mention your changes

If everything looks good, a maintainer will approve and merge the pull request when appropriate. After the pull request is merged, you'll appear in the contributers section.

### 6. Wait for the code to be reviewed

It can take several days before we can review the code you've submitted. We all have a lot of work to do and while we truly appreciate pull requests that are submitted, we can't review them instantly. We'll do our best to review them as fast as possible, but there are only 24 hours in a day and we can't sometimes be as fast as we wish we were. Moreover, there are little chances that the PR will be reviewed over the weekend.

Also, keep in mind that this project is still a side project. Maintainers of this project are not paid to work on it. Everything they do, is done during their time off of their "real" job, that means at night, on the weekend and during holidays.

### 7. What can I contribute to?

Even the simplest change is appreciated. It can be a typo error, translating the application in a new language, fix a bug. No change is too small.

# More about Pull Requests

Pull requests are, a great way to get your ideas into this repository.

When deciding if I merge in a pull request I look at the following things:

## Does it state intent

You should be clear which problem you're trying to solve with your contribution.

For example:

> Add link to code of conduct in README.md
Doesn't tell me anything about why you're doing that

> Add link to code of conduct in README.md because users don't always look in the CONTRIBUTING.md

Tells me the problem that you have found, and the pull request shows me the action you have taken to solve it.


## Is it of good quality

* There are no spelling mistakes
* It reads well
* For english language contributions: Has a good score on [Grammarly](grammarly.com) or [Hemingway App](http://www.hemingwayapp.com/)

## Does it move this repository closer to my vision for the repository

The aim of this repository is:

* To provide a beautiful and cool looking CTF website
* Make it easier for CTF organizers to host CTFs by giving them a good looking UI
* Foster a culture of respect and gratitude in the open source community.

# Happy Coding!

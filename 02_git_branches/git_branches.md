# Git Branches and Merging

**What:** Use branches to improve your workflow.

**Why:** 

- You don't want to mess with a working version of your code. (Naively, you would create a save copy of your folder...)

- Makes it easier to work together on a project (multiple people adding different features at the same time.)

- Can clean up git history of changes.

---

**Explanation:** Up until now, your git history looks probably something like this:

![Linear History](https://www.atlassian.com/dam/jcr:362f3b15-9e74-4fe5-b97d-784e296880ad/01.svg)

A linear "chain" of changes.

Let's say, you want to make some larger changes and for that you need to re-arrange functions, change classes or modules. It could take you days to finish it.

During this time the current code would be unusable. Not only for people who want to use it ("customers") but also for your colleagues, who would like to add other features!

So instead, we want to create a snapshot of our working code, and work on the new feature in a separate instance. Naively, you would do this by copying your whole code into a different folder and only work on the copy. But there is a better way, using `git branches`!

![Git Branches](https://wac-cdn.atlassian.com/dam/jcr:746be214-eb99-462c-9319-04a4d2eeebfa/01.svg?cdnVersion=696)

In the diagram above you can see the regular `master branch` plus two isolated lines of developement, **branches**, for two features. With this setup we can make sure that:

> The `master branch` always contains working code!

Once your feature is fully implemented, working and tested, you are allowed to **merge** your changes back into the `master branch`.

![Branching and Merging](https://rogerdudler.github.io/git-guide/img/branches.png)

---

**Demo:** 

Use [Interactive Git Demo](https://learngitbranching.js.org/?NODEMO)

Let's use
```bash
git log
```
to see the current history of commits.

Next we create a new commit with

```bash
git commit -m "master branch commit"
```
which does a regular commit on the master branch.

Now let's create a new branch for a new feature:

```bash
git checkout -b new_feature_branch
```
This will create a new branch called `new_feature_branch` that is currently the same as the `master` branch. We can get a list of all our branches with

```bash
git branch
```
The currently active one is marked with a little star.

If we create a new commit, it will only be on this `new_feature_branch`:

```bash
git commit -m "first feature commit"
```

Now in the meantime, someone might have changed the `master` branch, for exampe to do a quick hotfix.

```bash
git checkout master
git commit -m "hotfix"
```

Now we can see why it is named **branches** :)

So, let's finish up our feature and make it ready to merge into the master

```bash
git commit -m "finalized feature"
```

We first need to change to the master branch

```bash
git checkout master
```

and then ***merge** our `new_feature_branch` into the `master` branch:

```bash
git merge new_feature_branch
```

We can see that the master branch now contains all commits we made so far (the hotfix, as well as all feature commits):

```bash
git log
```

---


**Links and Sources:**

Here are some additonal links for reference or for further features.

- [Git - Der einfache Einsteig](https://rogerdudler.github.io/git-guide/index.de.html) A very simple guide for just the basic commands

- [Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/using-branches) A more detailed guide to branches, merging and everything else.

- [Don't Mess with the Master](https://thenewstack.io/dont-mess-with-the-master-working-with-branches-in-git-and-github/) A practical guide on how and why you should use a isolated master branch.

- [A succesful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/) A full workflow model using several branches.

- [Git SCM](https://git-scm.com/docs/git-checkout) Wondering what the `-b` option in `git checkout -b new_feature_branch` did? Checkout the full documentation.

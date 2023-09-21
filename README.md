# Recap

### Exercise 1

**Things of Note**
* The quickstart guide and links that Matar sent were exactly what I needed! It all clicked after that.
* Components in the UI return array of objects. I wanted the name, so created a custom calculation property that returns an array. Query was `.properties.components | [.[].name]` and returns correct information.

**Snags**

* I use pip3 as it pairs with my environment and python version. I was able to update the commands to accomplish this. 
* New Relic setup giving error around number where it was expecting string. `Error: UPGRADE FAILED: template: port-ocean/templates/secret.yaml:13:26: executing "port-ocean/templates/secret.yaml" at <b64enc>: wrong type for value; expected string; got int64`. Played around with base64 this, but also could have been due to just the copy/paste from the New Relic UI. Came back to this day after and was able to get it to work.
* Didn't ingest data on first day and tried it on both minikube and Docker Desktop. I noticed the commands in the docs and the UI were also different, and maybe led to some inconsistencies. It's possible the ingestion hadn't worked on minikube because the ingress add-on wasn't enabled.
* Needed to get up to speed on terminology being used around New Relic and Jira. Ended up watching a few videos to track. Eventually was able to get the workflow down. Ultimately spent a bit too much time trying to make sure the setup here was correct, which was a bit out of scope.

**Questions**

* When in practice does someone do local development on this? 
* Jira no longer in the UI - why did that go away?
* Connecting the resources based on Component name is very close, but still need to confirm methodology for this.
* Stopped polling for work. Wondering what happened? Maybe due to local cluster when computer is idle? 


### Exercise 2

**Things of Note**

* This one was fairly straightforward and enjoyable.
* I loved making the scorecards!
* I wrote a simple API call to check the number of PRs: `curl --request GET --url https://api.github.com/repos/<org-name>/<repo-name>/pulls --header "Authorization: Bearer <api-token>" | jq length )`
* Scheduled GH workflow under `.github/workflows/nightly-pr-check.yml`.
* I also built out and option for CircleCI, which is under `.circleci/config.yml`. If a customer was going through this setup, I would recommend either adding that as a scheduled workflow, or including it as post-steps or a webhook on workflow reaching a terminal state. Best case would be a Platform leader building out an orb (similar to Action) that includes the logic needed to keep scorecards up to date and then monitoring this with Config Policies.

**Snags**

* Decent amont of experimentation needed the make sure the APIs were being called in the right way.
* Needed to make sure I was up to speed on dealing with envars and GitHub Workflows.

### Exercise 3

**Things of Note**

* Conceptually I understood the work here, but task was a bit open-ended. 
* My approach was to illustrate that I am comfortable writing a python script that includes making an API call with custom fields. I also did the same when updating my CircleCI config.

**Snags**

* I had some trouble just visualizing this. 
* Spent some time trying to figure out some logic to query and return actual EOL packages. My intention was to find a way to run some logic with npm or python package to get a list, and then run some logic to see which are approaching. 
* Similar snag to #1 in just relating the frameworks entities to the relevant repository / microservice entities

### Exercise 4

**Things of Note**

* I was delighted by the Github App and the rich data that I was able to ingest at the click of a button.
* Bash script that runs the jq queries on `package.json` is under `bash-scripts/check-packages.sh`. Simple iteration that gets the job done.
* Not a snag here, but I noticed when I changed the name of the identifier, it gives me a 404. Would be nice to get a redirect back to Service so I'm not stuck :) 

**Snags**

* With how this is phrased, I assumed the packages would be available via the GH App. I did a lot of digging through the Available Github Resources [under here](https://docs.getport.io/build-your-software-catalog/sync-data-to-catalog/git/github/#port-app-configyml-structure) but could not figure out how to get the `package.json` in the correct way.
* I ended up using the webhook docs to shoot out a webhook with the information needed. I followed [these instructions](https://docs.getport.io/build-your-software-catalog/sync-data-to-catalog/webhook/examples/packages/javascript). 
* I tried to follow along with [this tutorial with GitLab](https://github.com/port-labs/package-json-webhook-example/tree/main) as well to ingest other objects. It was giving me trouble, but could have been something with the GitLab setup. I could go through this again and ensure the right steps are taken and reflected in the docs!

### Overall

Had fun doing this. 

I spent a lot of time experimenting and trying to figure out ways to accomplish different things. Looked through the docs, API, live demo, and watched [this webinar from Mor](https://www.youtube.com/watch?v=_i4vMfznw7Y&list=PLTwEf67PTkOuKj3_LEXkApfFMJPw6QEFn&index=6&t=2275s) twice over the course of this, and it was a great overview.

I think a great opportunity would be a blog tutorial / playbook series on how to implement very specific things in a bite-sized manner. Once I get something done, I know I am able to replicate it going forward. 

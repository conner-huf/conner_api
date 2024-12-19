# Centralized ConnerAPI

#### Reason
Here's a little tidbit for every developer on the job market: hosting stuff gets expensive. And because all of us have been in the market for a long period of time (most of us anyway), optimizing the cost of hosting should be pretty front-of-mind.

I've got lots of projects out there, and most of them require some kind of hosted backend with exposed endpoints. And hosting all these backends has a kind-of 'floor' cost - like it costs *something* to have it hosted, even if there's little-to-no traffic. 

So I've decided to consolidate all of my backends into a single hosted api that routes to the appropriate endpoints / backends / data and host it in a single centralized location.

This API is written using Python - FastAPI and will be hosted on Azure when completed.

#### Available Routes

- /resume 
  - endpoints for accessing my resume information
- /noodle 
  - endpoints for my concert venue web application
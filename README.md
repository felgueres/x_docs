Refs   
  Ads API. https://documenter.getpostman.com/view/7379786/SzRw1WTU#6a2980d8-e027-4643-93f3-de790c76413f
  Twitter Arch: https://miro.com/app/board/uXjVPBnTJmM=/ 
  Twitter Eng: https://blog.twitter.com/engineering
  Dev docs: https://developer.twitter.com/en/docs/twitter-ads-api
  How twitter works. https://twitter.com/justinhendrix/status/1594031025658675202


Functionality
- campaign management
- custom audiences
- creatives
- advertising analytics

Factors for ads pricing
- auction
- ad score
- bidding

Terminology
- price per billable action is not fixed, it's variable
- billable action: action that you pay for in your campaign

Ad score = quality + bid, this is metric that determines which ad will be served

Bidding campaings
- Campaign objectives: 
  - followers: more people see ad
  - engagements: more likes, retweets, replies and clicks
  - website traffic: more visitors to website
  - keywords: users with high intent (beta!) - likely current work
- Bidding options: 
  - automatic - auto optimizer 
  - maximum bid - exactly how much to pay for a BA 
  - target bid - average daily cost
- Quality score:
  - ad is given quality score determined by resonance, relevancy and recency
  - strong copy and visuals are extremely important 
  - resonance: engagement
  - relevance: alignment with audience
  - recency: up-to-date content
- Other factors influencing pay per billable action:
  - Size of target audience
  - How many other advertisers are competing

Targeting affects audience size
- additive - "OR": Interest, username, movies, events, keywords, topics
- restrictive - "AND" (makes pool smaller): geolocation, age, render, device, platform, language

How it works
- If you win the auction you get to make impressions
- When user does a billable action, you pay with a second price auction model
  You only pay whats needed for your ad to beat the 2nd place ad in the auction
  eg. if you bid $1.4 and beat an otherwise identical ad bidding $1.0, your campaign is charged 1.01 on the billable action

How to build it
- Distributed key-value store
- Costs are in terms of communication and data shuffling
- Complexity varies on dataset size, number of nodes and distribution of data across nodes

Practice
- Submit ad, think improvements in process
- Build a 2nd price auction system 
  - Considerations to scale it
    - Data struct to keep it things sorted? Maybe a balanced binary tree to access at in log n
    - Lazy sort: sort only when 
  - What hapens when someone withdraws or expires bid? How does this affect the data struct used? 
- What does the API look like? [x]
  What are the core endpoints? [x]
  What does the design look like?

- Requirements gathering
  Scale and performance
  - Bids per second or per auction
  - Concurrent auctions and bidders 
  Data consistency
  - Immediate consistency needed or eventual consistency acceptable?
  - Consistency requirements? No bids lost or incorrectly ordered?
  Reliability
  - How would you handle failures and network partitions?
  - System uptime and fault tolerance?
  Monitoring and maintenance 
  - What logging and reporting is needed?

Twitter  
Post Tweet 
  Use publish new message to followers (4.6K requests/s avg, 12K request/sec at peak)   
  This is likely closer to 6K requests/s in 2024  
  Write ops  
Home Timeline  
  User can view tweets posted by people they follow (300K requests/s)   
  Mostly read ops  
Home Timeline Tweets + Ads  
  User can view tweets posted by people they follow AND targeted ads  

How to create an ad 
1. Choose objective
2. Create an ad
3. Customize delivery

Problems
Ad relevance and personalization. How to use user data to predict ads to show?
  Input: Feature engineering on user profile
    Posts
    Interactions
    Followees
    Times when most active 
  
  Compute: Match ads vs. profile
    Topic modeling -> keywords of interest, themes (best for coarse categories of interest)
    Recency modeling -> Grab latest 5-10 to have recency bias -> best for time sensitive products
    Match ads vs. user's profile with embeddings
    Predict engagement metric for given content
    Predict is_user_monetizable
  
  Output: 
    Relevant Ad inventory 
  
Timeline Mixer. Updates user-specific cache
  Input: 
    User profile
    Followee new tweets 
    Ad inventory
  Compute: Rank
  Output: List of tweets + relevant ads

Distributed system to serve billions under 500ms. 
  Caching

Where does AI fit in?
  Creatives
  Targeting
    train model to predict interests, categories
  
wishlist for X
  human curation works, let me train my feed
  modes: entertainment, learning, work 
  ability to ask questions about X content
  transcripts on video and spaces
  summarize my timeline 
  X creator studio: help promote my work
  why things trend

Questions to ask?
  GenAI fits into creatives? Whats the limiter?

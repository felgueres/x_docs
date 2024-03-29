documenting how X ads work

base: https://ads-api.twitter.com

sections: analytics, audience, campaign_management, creatives, measurement

analytics
    sync: real-time response for small data
    stats/accounts/:account_id/active_entities

    async: batch jobs, you get an id and after a while get file
    stats/jobs/accounts/:account_id

    auction insights
    accounts/:account_id/auction_insights
        end_time
        granulatiry
        line_item_ids
        placement
        start_time
    
    reach and avg frequency
    stats/accounts/:account_id/reach/campaigns

audience
    insights/accounts/:account_id
        audience_type
        audience_value
        interaction_type

    insights/accounts/:account_id/available_audiences

    insights/keywords/search
        granularity
        keywords
        start_time
        end_time
        location
        negative_keywords

campaign_management
    /bidding_rules
    /content_categories
    /accounts/:account_id/funding_instruments (credit cards)
    /iab_categories
        retrieves categories for ad groups, eg. arts & entertainment, books & literature
    /line_items
    /media_creatives (get details for all media creatives for account)
    /promoted_accounts
    /promoted_tweets
    /scheduled_promoted_tweets
    /accounts/:account_id/targeting_criteria
    /targeting_criteria/app_store_categories (app categories user has installed)
    /targeting_criteria/conversation
    /targeting_criteria/devices
    /targeting_criteria/events
    /targeting_criteria/interests
    /targeting_criteria/languages
    /targeting_criteria/locations
    /targeting_criteria/network_operators
    /targeting_criteria/platform_versions
    /targeting_criteria/platforms
    /targeting_criteria/tv_markets
    /targeting_criteria/tv_shows
    /accounts/:account_id/targeting_suggestions
        Get up to 50 keyword or targeting suggestions to complement initial selection
        GET https://ads-api.twitter.com/12/accounts/18ce54d4x5t/targeting_suggestions?suggestion_type=KEYWORD&targeting_values=developers&count=2"
        Response: { "data": [ { "suggestion_type": "KEYWORD", "suggestion_value": "devs" }, { "suggestion_type": "KEYWORD", "suggestion_value": "software" } ]}
    /accounts/:account_id/tax_settings
    /accounts/:account_id/user_settings/:user_id
    /advertiser_business_categories

creatives
    Creatives are the entity that is promoted in a campaign. Text, images, GIFs, videos or cards, which can include images and videos

    /accounts/:account_id/account_media
    /accounts/:account_id/account_media/:account_media_id
    /accounts/:account_id/cards/all
    /accounts/:account_id/tweets
        as_user_id
        text
        card_uri
        media_keys
        tweet_mode
        video_cta VISIT_SITE, WATCH_NOW
        video_cta_value url to action
        video_description
        video_title
    /accounts/:account_id/scheduled_tweets

measurement
    /accounts/:account_id/app_event_tags
    /accounts/:account_id/app_event_provider_configurations
    /accounts/:account_id/app_lists
    /conversion_attribution?app_id=&conversion_time=&conversion_type=&hashed_device_id=&os_type=
    /conversion_event?app_id=&conversion_time=&conversion_type=&hashed_device_id=&os_type=
    /accounts/:account_id/web_event_tags

import urllib3, facebook, requests

token = 'EAACEdEose0cBAF99xT70Seg2BtrBoTA3bQOVWP7z6JOy1WZBudHpZAv36grrSGZBA3a41tZALcrRWmZA87025i3ynoUwlToygP1svqTrIg2WWzpcDl4mRpMZBAn0DQhMvKpDb7bbtZBPgUtayCJ8vaZCaGXAXGaNZBEHxUHILMYZA4epDZBAIBQ4Fk2Qz7yZA5WfGjJvmvE5bQXx3AZDZD'

graph = facebook.GraphAPI(access_token=token, version = 2.7)
events = graph.request('/search?q=run&type=event&limit=10000')

eventList = events['data']
print(eventList)
eventid = eventList[1]['id']
event1 = graph.get_object(id = eventid, fields='attending_count,can_guests_invite,category,cover,declined_count,description,end_time,guest_list_enabled,interested_count,is_canceled,is_page_owned,is_viewer_admin,maybe_count,noreply_count,owner,parent_group,place,ticket_uri,timezone,type,updated_time')
attenderscount = event1['attending_count']
declinerscount = event1['declined_count']
interestedcount = event1['interested_count']
maybecount = event1['maybe_count']
noreplycount = event1['noreply_count']

print(eventid)
print(attenderscount)

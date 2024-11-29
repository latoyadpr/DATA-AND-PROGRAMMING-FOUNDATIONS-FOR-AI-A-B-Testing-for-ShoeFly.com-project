import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')



print(ad_clicks.head())


views_by_source = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(views_by_source)

ad_clicks['is_click'] = ~ad_clicks['ad_click_timestamp'].isnull()


clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(index='utm_source', columns='is_click', values='user_id').reset_index()

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])


ad_counts = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(ad_counts)

# Group by experimental_group and is_click
clicks_by_group = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

# Pivot the data
clicks_pivot_group = clicks_by_group.pivot(index='experimental_group', columns='is_click', values='user_id').reset_index()

# Calculate the percentage of clicks
clicks_pivot_group['percent_clicked'] = clicks_pivot_group[True] / (clicks_pivot_group[True] + clicks_pivot_group[False])

print(clicks_pivot_group)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

# For a_clicks
a_clicks_by_day = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
a_clicks_pivot = a_clicks_by_day.pivot(index='day', columns='is_click', values='user_id').reset_index()
a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])

# For b_clicks
b_clicks_by_day = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
b_clicks_pivot = b_clicks_by_day.pivot(index='day', columns='is_click', values='user_id').reset_index()
b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])

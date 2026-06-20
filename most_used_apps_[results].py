import pandas as pd
from collections import Counter

df = pd.read_csv('survey_data_clean.csv')

apps = df['  Most used apps (multiple choice)  '].str.split(', ', expand=False)

all_apps = []
for app_list in apps:
    if isinstance(app_list, list):
        all_apps.extend(app_list)

app_counts = Counter(all_apps)

total_respondents = len(df)

app_data = []
for app, count in app_counts.most_common():
    pct = (count / total_respondents) * 100
    app_data.append({
        'App': app,
        'Count': count,
        'Percent': round(pct, 1)
    })

app_df = pd.DataFrame(app_data)

app_df.to_csv('most_used_apps.csv', index=False, encoding='utf-8-sig')

print('File saved as most_used_apps.csv')
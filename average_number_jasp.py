import pandas as pd
import numpy as np
from collections import Counter

df = pd.read_csv('survey_data_clean.csv')

screen_map = {
    'Less than 2 hours': 1,
    '2–4 hours': 2,
    '4–6 hours': 3,
    '6–8 hours': 4,
    'More than 8 hours': 5
}
df['ScreenTimeNum'] = df['  Average daily screen time  '].map(screen_map)

social_map = {
    'Less than 1 hour': 1,
    '1–3 hours': 2,
    '3–5 hours': 3,
    '5–7 hours': 4,
    'More than 7 hours': 5
}
df['SocialMediaNum'] = df['  Social media usage per day  '].map(social_map)

sleep_map = {
    'Less than 5 hours': 1,
    '5–6 hours': 2,
    '6–7 hours': 3,
    '7–8 hours': 4,
    'More than 8 hours': 5
}
df['SleepNum'] = df['  Average sleep duration  '].map(sleep_map)

study_map = {
    'Less than 1 hour': 1,
    '1–3 hours': 2,
    '3–5 hours': 3,
    'More than 5 hours': 4
}
df['StudyHoursNum'] = df['  Daily study/work hours  '].map(study_map)

usage_map = {
    'Never': 1,
    'Rarely': 2,
    'Sometimes': 3,
    'Often': 4,
    'Always': 5
}
df['UsageStudyNum'] = df['  Phone usage during studying/working hours  '].map(usage_map)

df['MorningCheckNum'] = df['  Do you check your phone within 5 minutes of waking up?  '].map({'Yes': 1, 'No': 0})

df['StressNum'] = pd.to_numeric(df['  Self-reported stress level  '], errors='coerce')

df['FocusNum'] = pd.to_numeric(df['   I can focus on tasks for long periods without distraction  '], errors='coerce')
df['LoseFocusNum'] = pd.to_numeric(df['I often lose focus due to my smartphone '], errors='coerce')
df['ProductiveNum'] = pd.to_numeric(df['I feel productive during my study/work sessions '], errors='coerce')
df['ProcrastinateNum'] = pd.to_numeric(df['I tend to procrastinate using my phone '], errors='coerce')
df['DifficultyNum'] = pd.to_numeric(df['I find it difficult to stay away from my phone during tasks '], errors='coerce')

print('DESCRIPTIVE STATISTICS')
print('=' * 60)

age_mean = df['Age'].mean()
age_sd = df['Age'].std()
print(f'Age (M, SD): {age_mean:.2f} ({age_sd:.2f})')

st_mean = df['ScreenTimeNum'].mean()
st_sd = df['ScreenTimeNum'].std()
print(f'Screen Time (M, SD): {st_mean:.2f} ({st_sd:.2f})')

sm_mean = df['SocialMediaNum'].mean()
sm_sd = df['SocialMediaNum'].std()
print(f'Social Media (M, SD): {sm_mean:.2f} ({sm_sd:.2f})')

sl_mean = df['SleepNum'].mean()
sl_sd = df['SleepNum'].std()
print(f'Sleep Duration (M, SD): {sl_mean:.2f} ({sl_sd:.2f})')

stress_mean = df['StressNum'].mean()
stress_sd = df['StressNum'].std()
print(f'Stress Level (M, SD): {stress_mean:.2f} ({stress_sd:.2f})')

us_mean = df['UsageStudyNum'].mean()
us_sd = df['UsageStudyNum'].std()
print(f'Usage During Study (M, SD): {us_mean:.2f} ({us_sd:.2f})')

mc_mean = df['MorningCheckNum'].mean()
print(f'Morning Check (% Yes): {mc_mean * 100:.1f}%')

focus_mean = df['FocusNum'].mean()
focus_sd = df['FocusNum'].std()
print(f'Focus (M, SD): {focus_mean:.2f} ({focus_sd:.2f})')

lf_mean = df['LoseFocusNum'].mean()
lf_sd = df['LoseFocusNum'].std()
print(f'Lose Focus (M, SD): {lf_mean:.2f} ({lf_sd:.2f})')

prod_mean = df['ProductiveNum'].mean()
prod_sd = df['ProductiveNum'].std()
print(f'Productive (M, SD): {prod_mean:.2f} ({prod_sd:.2f})')

proc_mean = df['ProcrastinateNum'].mean()
proc_sd = df['ProcrastinateNum'].std()
print(f'Procrastinate (M, SD): {proc_mean:.2f} ({proc_sd:.2f})')

diff_mean = df['DifficultyNum'].mean()
diff_sd = df['DifficultyNum'].std()
print(f'Difficulty Stay Away (M, SD): {diff_mean:.2f} ({diff_sd:.2f})')

print('')
print('CATEGORICAL VARIABLES')
print('=' * 60)

print('')
print('Gender:')
for val, count in df['Gender '].value_counts().items():
    pct = (count / len(df)) * 100
    print(f'  {val}: {count} ({pct:.1f}%)')

print('')
print('Education:')
for val, count in df['Level of education '].value_counts().items():
    pct = (count / len(df)) * 100
    print(f'  {val}: {count} ({pct:.1f}%)')

print('')
print('Screen Time Categories:')
for val, count in df['  Average daily screen time  '].value_counts().items():
    pct = (count / len(df)) * 100
    print(f'  {val}: {count} ({pct:.1f}%)')

print('')
print('Social Media Categories:')
for val, count in df['  Social media usage per day  '].value_counts().items():
    pct = (count / len(df)) * 100
    print(f'  {val}: {count} ({pct:.1f}%)')

print('')
print('Sleep Duration Categories:')
for val, count in df['  Average sleep duration  '].value_counts().items():
    pct = (count / len(df)) * 100
    print(f'  {val}: {count} ({pct:.1f}%)')

print('')
print('MOST USED APPS')
print('=' * 60)

apps = df['  Most used apps (multiple choice)  '].str.split(', ', expand=False)
all_apps = []
for app_list in apps:
    if isinstance(app_list, list):
        all_apps.extend(app_list)

app_counts = Counter(all_apps)
total = len(df)
for app, count in app_counts.most_common():
    pct = (count / total) * 100
    print(f'  {app}: {count} ({pct:.1f}%)')

df_clean = df[[
    'Age',
    'Gender ',
    'Level of education ',
    'Current status ',
    'ScreenTimeNum',
    'SocialMediaNum',
    'SleepNum',
    'StudyHoursNum',
    'UsageStudyNum',
    'MorningCheckNum',
    'StressNum',
    'FocusNum',
    'LoseFocusNum',
    'ProductiveNum',
    'ProcrastinateNum',
    'DifficultyNum',
    '  Most used apps (multiple choice)  '
]].copy()

df_clean.columns = [
    'Age',
    'Gender',
    'Education',
    'Status',
    'ScreenTime',
    'SocialMedia',
    'Sleep',
    'StudyHours',
    'UsageDuringStudy',
    'MorningCheck',
    'Stress',
    'Focus',
    'LoseFocus',
    'Productive',
    'Procrastinate',
    'DifficultyStayAway',
    'MostUsedApps'
]

df_clean.to_csv('data_for_jasp.csv', index=False, encoding='utf-8-sig')

print('')
print('File saved as data_for_jasp.csv')


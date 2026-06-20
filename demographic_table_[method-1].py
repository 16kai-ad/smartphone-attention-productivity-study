import pandas as pd
from collections import Counter

df = pd.read_csv('survey_data_clean.csv')

total = len(df)

age_bins = pd.cut(df['Age'], bins=[18, 20, 22, 24, 26, 31], right=False)
age_labels = ['18-20', '21-22', '23-24', '25-26', '27-30']
df['AgeGroup'] = pd.cut(df['Age'], bins=[18, 21, 23, 25, 27, 31], labels=age_labels, right=False)

results = []

age_mean = df['Age'].mean()
age_sd = df['Age'].std()
results.append(['Age (M, SD)', f'{age_mean:.2f} ({age_sd:.2f})', ''])

results.append(['Age Group', '', ''])
for val, count in df['AgeGroup'].value_counts().sort_index().items():
    pct = (count / total) * 100
    results.append([f'  {val}', str(count), f'{pct:.1f}%'])

results.append(['Gender', '', ''])
for val, count in df['Gender '].value_counts().items():
    pct = (count / total) * 100
    results.append([f'  {val}', str(count), f'{pct:.1f}%'])

results.append(['Education Level', '', ''])
for val, count in df['Level of education '].value_counts().items():
    pct = (count / total) * 100
    results.append([f'  {val}', str(count), f'{pct:.1f}%'])

results.append(['Current Status', '', ''])
status_counts = df['Current status '].value_counts()
for val, count in status_counts.items():
    pct = (count / total) * 100
    results.append([f'  {val}', str(count), f'{pct:.1f}%'])

results.append(['Screen Time', '', ''])
for val, count in df['  Average daily screen time  '].value_counts().items():
    pct = (count / total) * 100
    results.append([f'  {val}', str(count), f'{pct:.1f}%'])

results.append(['Social Media Usage', '', ''])
for val, count in df['  Social media usage per day  '].value_counts().items():
    pct = (count / total) * 100
    results.append([f'  {val}', str(count), f'{pct:.1f}%'])

results.append(['Sleep Duration', '', ''])
for val, count in df['  Average sleep duration  '].value_counts().items():
    pct = (count / total) * 100
    results.append([f'  {val}', str(count), f'{pct:.1f}%'])

results.append(['Phone Usage During Studying', '', ''])
for val, count in df['  Phone usage during studying/working hours  '].value_counts().items():
    pct = (count / total) * 100
    results.append([f'  {val}', str(count), f'{pct:.1f}%'])

results.append(['Morning Check', '', ''])
for val, count in df['  Do you check your phone within 5 minutes of waking up?  '].value_counts().items():
    pct = (count / total) * 100
    results.append([f'  {val}', str(count), f'{pct:.1f}%'])

results_df = pd.DataFrame(results, columns=['Variable', 'Count', 'Percent'])

results_df.to_csv('demographic_table.csv', index=False, encoding='utf-8-sig')

print('File saved as demographic_table.csv')
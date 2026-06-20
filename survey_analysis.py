# survey-analysis-final.py
import pandas as pd
import numpy as np

print("=" * 60)
print("SMARTPHONE USAGE SURVEY ANALYSIS")
print("=" * 60)

# Load data
df = pd.read_csv('data-smart-survey.csv', encoding='utf-8')
print(f"\nLoaded {len(df)} rows")

# Clean age column
df['Age_clean'] = pd.to_numeric(df['Age (number only)'], errors='coerce')

# Correct column names
attention_cols = [
    '   I can focus on tasks for long periods without distraction  ',
    'I often lose focus due to my smartphone ',
    'I feel productive during my study/work sessions ',
    'I tend to procrastinate using my phone ',
    'I find it difficult to stay away from my phone during tasks '
]

short_names = [
    "Focus on tasks without distraction",
    "Lose focus due to smartphone",
    "Feel productive",
    "Procrastinate using phone",
    "Difficult to stay away from phone"
]

# Filter data (age 18-30, no missing values)
df_filtered = df[
    (df['Age_clean'] >= 18) &
    (df['Age_clean'] <= 30) &
    df[attention_cols].notna().all(axis=1)
].copy()

print(f"\nAfter filtering: {len(df_filtered)} respondents")

# Remove High school and Other from education (small sample sizes)
df_filtered = df_filtered[
    ~df_filtered['Level of education '].isin(['High school', 'Other'])
].copy()

print(f"After removing High school and Other: {len(df_filtered)} respondents")

# Recalculate all statistics
age_mean = df_filtered['Age_clean'].mean()
age_std = df_filtered['Age_clean'].std()

gender_counts = df_filtered['Gender '].value_counts()
edu_counts = df_filtered['Level of education '].value_counts()
status_counts = df_filtered['Current status '].value_counts()
screen_counts = df_filtered['  Average daily screen time  '].value_counts()
social_counts = df_filtered['  Social media usage per day  '].value_counts()
phone_counts = df_filtered['  Phone usage during studying/working hours  '].value_counts()
wake_counts = df_filtered['  Do you check your phone within 5 minutes of waking up?  '].value_counts()
sleep_counts = df_filtered['  Average sleep duration  '].value_counts()
study_counts = df_filtered['  Daily study/work hours  '].value_counts()
stress_mean = df_filtered['  Self-reported stress level  '].mean()
stress_std = df_filtered['  Self-reported stress level  '].std()
belief_counts = df_filtered['Do you believe smartphone usage affects your productivity?  '].value_counts()

# Print updated table
print(f"\n{'=' * 70}")
print(f"TABLE 1. Participant Characteristics (N = {len(df_filtered)})")
print(f"{'=' * 70}\n")

print(f"Age                                                   {age_mean:.2f} ({age_std:.2f})\n")

print("Gender")
for gender, count in gender_counts.items():
    pct = (count / len(df_filtered)) * 100
    print(f"  {gender:<40} {count} ({pct:.1f}%)")
print()

print("Level of education")
for edu, count in edu_counts.items():
    pct = (count / len(df_filtered)) * 100
    print(f"  {edu:<40} {count} ({pct:.1f}%)")
print()

print("Current status")
for status, count in status_counts.items():
    pct = (count / len(df_filtered)) * 100
    print(f"  {status:<40} {count} ({pct:.1f}%)")
print()

print("Average daily screen time")
for screen, count in screen_counts.items():
    pct = (count / len(df_filtered)) * 100
    print(f"  {screen:<40} {count} ({pct:.1f}%)")
print()

print("Social media usage per day")
for social, count in social_counts.items():
    pct = (count / len(df_filtered)) * 100
    print(f"  {social:<40} {count} ({pct:.1f}%)")
print()

print("Phone usage during studying/working hours")
for phone, count in phone_counts.items():
    pct = (count / len(df_filtered)) * 100
    print(f"  {phone:<40} {count} ({pct:.1f}%)")
print()

print("Check phone within 5 minutes of waking")
for wake, count in wake_counts.items():
    pct = (count / len(df_filtered)) * 100
    print(f"  {wake:<40} {count} ({pct:.1f}%)")
print()

print("Attention and Productivity (1-5 scale)")
for i, name in enumerate(short_names):
    mean_val = df_filtered[attention_cols[i]].mean()
    std_val = df_filtered[attention_cols[i]].std()
    print(f"  {name:<40} {mean_val:.2f} ({std_val:.2f})")
print()

print("Average sleep duration")
for sleep, count in sleep_counts.items():
    pct = (count / len(df_filtered)) * 100
    print(f"  {sleep:<40} {count} ({pct:.1f}%)")
print()

print("Daily study/work hours")
for study, count in study_counts.items():
    pct = (count / len(df_filtered)) * 100
    print(f"  {study:<40} {count} ({pct:.1f}%)")
print()

print(f"Self-reported stress level (0-5)                    {stress_mean:.2f} ({stress_std:.2f})\n")

print("Believe smartphone affects productivity")
for belief, count in belief_counts.items():
    pct = (count / len(df_filtered)) * 100
    print(f"  {belief:<40} {count} ({pct:.1f}%)")

print(f"\n{'=' * 70}")
print("Table created successfully.")

# save_updated_data.py
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data-smart-survey.csv', encoding='utf-8')

# Clean age column
df['Age_clean'] = pd.to_numeric(df['Age (number only)'], errors='coerce')

# Correct column names for attention questions
attention_cols = [
    '   I can focus on tasks for long periods without distraction  ',
    'I often lose focus due to my smartphone ',
    'I feel productive during my study/work sessions ',
    'I tend to procrastinate using my phone ',
    'I find it difficult to stay away from my phone during tasks '
]

# Apply filters: age 18-30, no missing attention data
df_filtered = df[
    (df['Age_clean'] >= 18) &
    (df['Age_clean'] <= 30) &
    df[attention_cols].notna().all(axis=1)
].copy()

# Remove High school and Other from education
df_filtered = df_filtered[
    ~df_filtered['Level of education '].isin(['High school', 'Other'])
].copy()

print(f"Original data: {len(df)} rows")
print(f"After filtering: {len(df_filtered)} rows")
print(f"\nEducation levels in final dataset:")
print(df_filtered['Level of education '].value_counts())

# Save to new CSV file
df_filtered.to_csv('survey_data_clean.csv', index=False, encoding='utf-8-sig')
print("\nNew CSV file saved as 'survey_data_clean.csv'")

# Display first few rows to verify
print("\nFirst 5 rows of cleaned data:")
print(df_filtered.head())

# create_table_filtered.py
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data-smart-survey.csv', encoding='utf-8')

# Clean age column
df['Age_clean'] = pd.to_numeric(df['Age (number only)'], errors='coerce')

# Correct column names
attention_cols = [
    '   I can focus on tasks for long periods without distraction  ',
    'I often lose focus due to my smartphone ',
    'I feel productive during my study/work sessions ',
    'I tend to procrastinate using my phone ',
    'I find it difficult to stay away from my phone during tasks '
]

short_names = [
    "Focus on tasks without distraction",
    "Lose focus due to smartphone",
    "Feel productive",
    "Procrastinate using phone",
    "Difficult to stay away from phone"
]

# Filter data (age 18-30, no missing values)
df_filtered = df[
    (df['Age_clean'] >= 18) &
    (df['Age_clean'] <= 30) &
    df[attention_cols].notna().all(axis=1)
].copy()

# Remove High school and Other from education
df_filtered = df_filtered[
    ~df_filtered['Level of education '].isin(['High school', 'Other'])
].copy()

# Calculate statistics
N = len(df_filtered)
age_mean = df_filtered['Age_clean'].mean()
age_std = df_filtered['Age_clean'].std()

gender_counts = df_filtered['Gender '].value_counts()
edu_counts = df_filtered['Level of education '].value_counts()
status_counts = df_filtered['Current status '].value_counts()
screen_counts = df_filtered['  Average daily screen time  '].value_counts()
social_counts = df_filtered['  Social media usage per day  '].value_counts()
phone_counts = df_filtered['  Phone usage during studying/working hours  '].value_counts()
wake_counts = df_filtered['  Do you check your phone within 5 minutes of waking up?  '].value_counts()
sleep_counts = df_filtered['  Average sleep duration  '].value_counts()
study_counts = df_filtered['  Daily study/work hours  '].value_counts()
stress_mean = df_filtered['  Self-reported stress level  '].mean()
stress_std = df_filtered['  Self-reported stress level  '].std()
belief_counts = df_filtered['Do you believe smartphone usage affects your productivity?  '].value_counts()

# Create formatted text version for Word
with open('table1_participant_characteristics.csv', 'w', encoding='utf-8') as f:
    f.write("=" * 70 + "\n")
    f.write(f"TABLE 1. Participant Characteristics (N = {N})\n")
    f.write("=" * 70 + "\n\n")
    
    f.write(f"Age                                                   {age_mean:.2f} ({age_std:.2f})\n\n")
    
    f.write("Gender\n")
    for gender, count in gender_counts.items():
        pct = (count / N) * 100
        f.write(f"  {gender:<40} {count} ({pct:.1f}%)\n")
    f.write("\n")
    
    f.write("Level of education\n")
    for edu, count in edu_counts.items():
        pct = (count / N) * 100
        f.write(f"  {edu:<40} {count} ({pct:.1f}%)\n")
    f.write("\n")
    
    f.write("Current status\n")
    for status, count in status_counts.items():
        pct = (count / N) * 100
        f.write(f"  {status:<40} {count} ({pct:.1f}%)\n")
    f.write("\n")
    
    f.write("Average daily screen time\n")
    for screen, count in screen_counts.items():
        pct = (count / N) * 100
        f.write(f"  {screen:<40} {count} ({pct:.1f}%)\n")
    f.write("\n")
    
    f.write("Social media usage per day\n")
    for social, count in social_counts.items():
        pct = (count / N) * 100
        f.write(f"  {social:<40} {count} ({pct:.1f}%)\n")
    f.write("\n")
    
    f.write("Phone usage during studying/working hours\n")
    for phone, count in phone_counts.items():
        pct = (count / N) * 100
        f.write(f"  {phone:<40} {count} ({pct:.1f}%)\n")
    f.write("\n")
    
    f.write("Check phone within 5 minutes of waking\n")
    for wake, count in wake_counts.items():
        pct = (count / N) * 100
        f.write(f"  {wake:<40} {count} ({pct:.1f}%)\n")
    f.write("\n")
    
    f.write("Attention and Productivity (1-5 scale)\n")
    for i, name in enumerate(short_names):
        mean_val = df_filtered[attention_cols[i]].mean()
        std_val = df_filtered[attention_cols[i]].std()
        f.write(f"  {name:<40} {mean_val:.2f} ({std_val:.2f})\n")
    f.write("\n")
    
    f.write("Average sleep duration\n")
    for sleep, count in sleep_counts.items():
        pct = (count / N) * 100
        f.write(f"  {sleep:<40} {count} ({pct:.1f}%)\n")
    f.write("\n")
    
    f.write("Daily study/work hours\n")
    for study, count in study_counts.items():
        pct = (count / N) * 100
        f.write(f"  {study:<40} {count} ({pct:.1f}%)\n")
    f.write("\n")
    
    f.write(f"Self-reported stress level (0-5)                    {stress_mean:.2f} ({stress_std:.2f})\n\n")
    
    f.write("Believe smartphone affects productivity\n")
    for belief, count in belief_counts.items():
        pct = (count / N) * 100
        f.write(f"  {belief:<40} {count} ({pct:.1f}%)\n")
    
    f.write("\n" + "=" * 70 + "\n")

print(f"Text table saved as 'table1_participant_characteristics.csv'")
print(f"Total N = {N}")
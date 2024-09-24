import matplotlib.pyplot as plt
import pandas as pd

def plot_daily_steps():
    df = pd.read_csv('dailySteps_merged.csv')
    df['ActivityDay'] = pd.to_datetime(df['ActivityDay'])
    grouped_df = df.groupby('ActivityDay')['StepTotal'].sum().reset_index()
    grouped_df = grouped_df.sort_values('ActivityDay')
    plt.figure(figsize=(10, 6))
    plt.plot(grouped_df['ActivityDay'], grouped_df['StepTotal'])
    plt.xlabel('ActivityDay')
    plt.ylabel('StepTotal')
    plt.title('Daily Steps')
    plt.show()

def plot_daily_distance():
    df = pd.read_csv('dailyActivity_merged.csv')
    df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])
    grouped_df = df.groupby('ActivityDate')['TotalDistance'].sum().reset_index()
    grouped_df = grouped_df.sort_values('ActivityDate')
    plt.figure(figsize=(10, 6))
    plt.bar(grouped_df['ActivityDate'], grouped_df['TotalDistance'])
    plt.xlabel('ActivityDate')
    plt.ylabel('TotalDistance')
    plt.title('Daily Distance')
    plt.show()

def plot_daily_sleep():
    df = pd.read_csv('sleepDay_merged.csv')
    df['SleepDay'] = pd.to_datetime(df['SleepDay'])
    grouped_df = df.groupby('SleepDay')['TotalTimeInBed'].sum().reset_index()
    grouped_df = grouped_df.sort_values('SleepDay')
    plt.figure(figsize=(10, 6))
    plt.scatter(grouped_df['SleepDay'], grouped_df['TotalTimeInBed'])
    plt.xlabel('SleepDay')
    plt.ylabel('TotalTimeInBed')
    plt.title('Daily Sleep')
    plt.show()

def plot_hourly_steps():
    df = pd.read_csv('hourlySteps_merged.csv')
    df['ActivityHour'] = pd.to_datetime(df['ActivityHour'])
    grouped_df = df.groupby('ActivityHour')['StepTotal'].sum().reset_index()
    grouped_df = grouped_df.sort_values('ActivityHour')
    plt.figure(figsize=(10, 6))
    plt.pie(grouped_df['StepTotal'][:15], labels=grouped_df['ActivityHour'][:15].dt.strftime('%H:%M'), autopct='%1.1f%%')
    plt.title('Hourly Steps')
    plt.show()

def plot_hourly_steps_on_date(date):
    df = pd.read_csv('hourlySteps_merged.csv')
    df['ActivityHour'] = pd.to_datetime(df['ActivityHour'])
    filtered_df = df[df['ActivityHour'].dt.date == pd.to_datetime(date).date()]
    hourly_steps = filtered_df.groupby('ActivityHour')['StepTotal'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    plt.pie(hourly_steps['StepTotal'], labels=hourly_steps['ActivityHour'].dt.strftime('%H:%M'), autopct='%1.1f%%')
    plt.title('Hourly Steps on ' + date)
    plt.show()

   

if __name__ == "__main__":
    plot_hourly_steps_on_date("2016-04-12")

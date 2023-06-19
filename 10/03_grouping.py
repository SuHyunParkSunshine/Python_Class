import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {'Name': ['John', 'Mike', 'Sarah', 'Adam', 'Emily', 'Daniel', 'Olivia', 'Liam', 'Sophia', 'Ethan',
                 'Emma', 'Jacob', 'Ava', 'Mia', 'Noah', 'Charlotte', 'Harper', 'William', 'Benjamin', 'Elijah',
                 'Amelia', 'James', 'Oliver', 'Lucas', 'Mason', 'Logan', 'Alexander', 'Evelyn', 'Grace', 'Victoria'],
        'Age': np.random.randint(20, 40, 30),
        'Gender': ['Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male',
                   'Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Male',
                   'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female'],
        'City': ['New York', 'Paris', 'London', 'Sydney', 'Tokyo', 'Berlin', 'Rome', 'Madrid', 'Seoul', 'Beijing',
                 'Moscow', 'Vienna', 'Athens', 'Cairo', 'Lisbon', 'Dublin', 'Amsterdam', 'Stockholm', 'Oslo', 'Helsinki',
                 'Copenhagen', 'Budapest', 'Prague', 'Warsaw', 'Vienna', 'Brussels', 'Luxembourg', 'Zurich', 'Geneva', 'Dubai']}
df = pd.DataFrame(data)

df['initial'] = df['Name'].str[0]
# df['Name'].str.slice(0, 1)
# df['Name'].str[0]
print(df)
print('-' * 50)

mean_age_by_initial = df.groupby('initial')['Age'].mean()
print(mean_age_by_initial)
print('-' * 50)

overall_mean_age = df['Age'].mean()

plt.bar(mean_age_by_initial.index, mean_age_by_initial.values)
plt.axhline(overall_mean_age, color='red', linestyle='--', label='overall_mean_age')
plt.xlabel('initial')
plt.ylabel('Mean Age')
plt.legend()
plt.show()
print('-' * 50)
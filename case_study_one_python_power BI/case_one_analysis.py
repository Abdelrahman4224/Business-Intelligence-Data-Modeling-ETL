import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



clients = pd.read_csv("Clients___Projects_Table.csv")
consultants = pd.read_csv("Consultants_Table__Final_.csv")
timesheet = pd.read_csv("Timesheet_Table__Consultants_Assigned_to_One_Client_.csv")
feedback = pd.read_csv("Client_Satisfaction___Feedback_Table.csv")

# print(clients.shape, consultants.shape, timesheet.shape, feedback.shape)

# Assumed full time work is 40 hours/week = (160 hours/month)
total_hours = timesheet.groupby("Consultant")["Hours"].sum()
max_hours = 160  

utilization_rate = (total_hours / max_hours) * 100
#print(utilization_rate)



merged_data = timesheet.merge(clients, on="Client")
merged_data["revenue"] = merged_data["Hours"] * merged_data["Hourly Rate"]

#print(merged_data)



revenue_per_client = merged_data.groupby("Client")["revenue"].sum()
#print(revenue_per_client)


avg_satisfaction = feedback.groupby("Client")["Rating"].mean()
#print(avg_satisfaction)




revenue_per_client.plot(kind='bar', figsize=(8, 4), title="Revenue per Client")
plt.ylabel("Revenue ($)")



utilization_rate = utilization_rate.reset_index()
utilization_rate.columns = ["Consultant", "Utilization Rate"]  
utilization_rate = utilization_rate.sort_values("Utilization Rate", ascending=False)  
plt.figure(figsize=(8, 4))
plt.bar(utilization_rate["Consultant"], utilization_rate["Utilization Rate"], color="royalblue")  
plt.xlabel("Consultant")
plt.ylabel("Utilization Rate (%)")
plt.title("Consultant Utilization Rate")
plt.xticks(rotation=45)
plt.show()


merged_data.to_csv("processed_timesheet.csv", index=False)



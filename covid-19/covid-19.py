import pandas as pd 
import numpy as  np
import matplotlib.pyplot as plt

# Read 

df=pd.read_csv("covid-19/covid_19_data.csv")

# Clean Data

df.dropna(subset=["ObservationDate","Province/State","Country/Region","Last Update","Confirmed","Deaths","Recovered"],inplace=True)


# Top 5 Countries with Numbers of Death

plt.figure(figsize=(12, 6))
total = df["Country/Region"].value_counts().head(6)
plt.bar(total.index , total.values,color= [ "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd","#8c564b"])
plt.xlabel("Countries Name",fontweight="light", fontsize=12)
plt.ylabel("No of Deaths",fontweight="light", fontsize=12)
plt.title("Top 5 Countries with Numbers of Death",fontweight="bold", fontsize=16)
plt.legend()
plt.tight_layout()
plt.savefig("covid-19/1.png",dpi = 300 , bbox_inches = "tight")
plt.show()

# total number of confirmed cases, deaths, and recoveries evolve globally over the given time period (Jan 22 - Feb 15)

df["ObservationDate"] = pd.to_datetime(df["ObservationDate"])

start_date = "2020-01-22"
end_date   = "2020-02-15"

filterr = df[((df["ObservationDate"] >= start_date)& (df["ObservationDate"]<=end_date) )]


total  = filterr.groupby("ObservationDate")[["Confirmed","Deaths","Recovered"]].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(total["ObservationDate"],total["Confirmed"],color = "red",label = "Confirmend")
plt.plot(total["ObservationDate"],total["Deaths"],color = "blue",label = "Deaths")
plt.plot(total["ObservationDate"],total["Recovered"],color = "c",label = "Recoveries")

plt.title("Global COVID-19 Evolution (Jan 22 - Feb 15, 2020)", fontsize=16, fontweight="bold")
plt.xlabel("Dates",fontsize=13,fontweight="light")
plt.ylabel("Numbers of Cases",fontsize=13,fontweight="light")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("covid-19/2.png",dpi = 300 , bbox_inches = "tight")
plt.show()

# Top 9 Countries Comparision

plt.figure(figsize=(12, 6))
df["ObservationDate"]= pd.to_datetime(df["ObservationDate"])
fil = df[((df["ObservationDate"] <= "2020-02-15") & (df["Country/Region"] != "Mainland China") )]

to = fil.groupby("Country/Region")["Confirmed"].sum().reset_index()
plt.barh(to["Country/Region"],to["Confirmed"],color = ["blue", "red", "green", "orange", "purple", "brown", "pink", "gray", "cyan"])
plt.xlabel("Number of Confirmed Case",fontsize = 12 , fontweight = "light")
plt.ylabel("Countries Name",fontsize = 12 , fontweight = "light")
plt.title("Top 9 Countries Comparision",fontsize = 14 , fontweight = "heavy")
plt.tight_layout()
plt.savefig("covid-19/3.png",dpi = 300 , bbox_inches = "tight")
plt.show()

# Growth Rate Analyze

plt.figure(figsize=(17,17))

to = df.groupby("Country/Region")["Confirmed"].sum().reset_index()
plt.pie(to["Confirmed"],labels=to["Country/Region"],autopct="%1.1f%%", startangle=90)
plt.legend( loc="center left",bbox_to_anchor=(1.05, 0.5) ,fontsize = 10)
plt.title("Growth Rate Analyzer",fontsize = 14 , fontweight = "heavy")
plt.savefig("covid-19/4.png",dpi = 300 , bbox_inches = "tight")
plt.show()

# Mortality and Recovery Rates:

plt.figure(figsize=(12,6))
df["ObservationDate"] = pd.to_datetime(df["ObservationDate"])
china = df[df["Country/Region"] == "Mainland China"]

grp = china.groupby("ObservationDate")[["Deaths","Confirmed","Recovered"]].sum().reset_index()


grp["FatalityRate"] = (grp["Deaths"]/grp["Confirmed"])*100
grp["RecoveryRate"] = (grp["Recovered"]/grp["Confirmed"]) * 100

plt.plot(grp["ObservationDate"],grp["FatalityRate"],label = "Fatality Rate(%)")
plt.plot(grp["ObservationDate"],grp["RecoveryRate"],label = "Recovery Rate(%)")
plt.title("Mortality and Recovery Rates",fontsize = 14 ,fontweight = "heavy")
plt.xlabel("Dates",fontsize = 12 , fontweight = "light")
plt.ylabel("Rate (%)",fontsize = 12 , fontweight = "light")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True,alpha=0.8)
plt.tight_layout()
plt.savefig("covid-19/5.png",dpi = 300 , bbox_inches = "tight")

plt.show()

# Province-Level Analysis in China

plt.figure(figsize=(12,6))
df["ObservationDate"] = pd.to_datetime(df["ObservationDate"])

c=df[(df["ObservationDate"]<= "1/22/2020") & (df["ObservationDate"] >= "1/15/2020") & (df["Country/Region"] == "Mainland China")]

china_province = c.groupby("Province/State")[["Confirmed"]].sum().reset_index()

plt.plot(china_province["Province/State"],china_province["Confirmed"],label = "Confirmed Cases   ",color = "Purple")
plt.xlabel("Province Names",fontsize = 12 , fontweight = "light")
plt.ylabel("Confirmed Cases",fontsize = 12 , fontweight = "light")
plt.title("Province-Level Analysis in China",fontsize=14 , fontweight = "heavy")
plt.legend()
plt.xticks(rotation = 45)
plt.tight_layout()

plt.savefig("covid-19/6.png",dpi = 300 , bbox_inches = "tight")
plt.show()


# Status Proportion

df["ObservationDate"] = pd.to_datetime(df["ObservationDate"])

fil = df[df["ObservationDate"] == "2/15/2020"]

grp = fil.groupby("ObservationDate")[["Deaths","Confirmed","Recovered"]].sum().reset_index()

ActiveCase = int(grp["Confirmed"]-grp["Deaths"]-grp["Recovered"])
death = int(grp["Deaths"])
recover = int(grp["Recovered"])

plt.pie([ActiveCase,death,recover],labels=["Deaths","Recovered","ActiveCase"],colors = ["#9ecae1", "#a1d99b", "#fdae6b"],autopct="%1.1f%%")
plt.legend( loc="center left",bbox_to_anchor=(0.9, 0.7) ,fontsize = 10)
plt.title("Status Proportion",fontsize = 14 , fontweight=  "heavy")
plt.tight_layout()
plt.savefig("covid-19/7.png",dpi = 300 , bbox_inches = "tight")
plt.show()

# Active Cases Trend

df["ObservationDate"] = pd.to_datetime(df["ObservationDate"])

fil = df[df["Province/State"] == "Hubei"]

grp =  fil.groupby("ObservationDate")[["Deaths","Confirmed","Recovered"]].sum().reset_index()

grp["ActiveCase"] = grp["Confirmed"]-grp["Deaths"]-grp["Recovered"]

plt.plot(grp["ObservationDate"],grp["ActiveCase"],color= "blue",label="Active Cases Trend")
plt.fill_between(grp["ObservationDate"], grp["ActiveCase"], color="skyblue", alpha=0.5)
plt.title("Active Case Trend",fontsize = 14 , fontweight = "heavy")
plt.xlabel("Dates",fontsize = 12 ,fontweight = "light")
plt.ylabel("Active Case",fontsize = 12 ,fontweight = "light")
plt.xticks(rotation = 45)
plt.legend()
plt.tight_layout()
plt.savefig("covid-19/8.png",dpi = 300 , bbox_inches = "tight")
plt.show()
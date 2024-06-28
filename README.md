# Predicting School District Performance
Practicum Project by Matt Burns || 
Regis University MSDS 692

# Project Questions
### Predicting District Performance
Given the publicly available data, can we predict graduation rate performance of a school district.
### What Can We Learn
What data points of a school district affect graduation rates?

# The Data Used
| Student Data | Staff Data | Admin/District Data |
| --- | --- | --- |
| CMAS Results | Teacher Salary | Principal/Assistant Principal Salary |
| Graduation/Dropout Rates | Teacher Demographics | Principal Demographics |
| Special Programs (Special Education, MKV, etc) | Counselor, Psychologist, Social Worker Data | Superintendent Average Salary |
| Chronic Absenteeism | Student : Teacher Ratios | Rural Status |
| Student Demographics | Personnel Turnover Rates |
| Student Mobililty & Stability |

# The Process
1. Collect data from Colorado Department of Education Website
2. Clean up data and merge on district code
3. Split data and train using Histogram-based Gradient Boosting Regression Tree
4. Determine strongest correlations to target feature of graduation rate
5. Examine correlations for further insight
6. Scrape district websites to guage general sentiment of top performing and bottom performing schools of similar demographics

# The Key Takeaways
- **Showing Up Matters** - Chronic absenteeism has the strongest correlation to graduation and dropout rates.
- **The Most Affected Group** - Students experiencing homelessness (MKV) are the group that is most likely to struggle with chronic absenteeism which leads to lower graduation rates.
- **Teacher Pay** - Higher teacher salary correlates positively with graduation rates.
- **Web Sentiment is Similar** - Both the top performing and bottom performing websites had similar positive sentiment to all posts.
- **More Data is Needed** - More specific student data would give us better insights into students and allow us to predict student performance.

# Plots
### The positive correlation of chronic absenteeism to having MKV students in your district.
![](/Plots/chronic_absence_rate_plot.png)

### The big difference in graduate rates between all students and MKV students depending on rural designation
![](/Plots/Grad_boxplots.png)

### District Website Evaluation shows the similarities in the positive sentiments of top performing (St Vrain Valley) and bottom performing (District 49) school districts
![](/Plots/St_Vrain_Valley_RE1J_Score.png)
![](/Plots/District_49_Sentiment_Score.png)

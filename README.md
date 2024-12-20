# India Crime Analysis

Visit https://crimeinsights.streamlit.app to check the analysis

Dataset descripition:
1. STATE/UT -
Represents the state name and union teritory name if it is a union teritory (data type-nominal).

2. Year -
Specifies to which year data belongs (data type-ordinal).

3. Murder -
The number of murders that had happened during the year (data type-continuous).

4. Assault on women -
A threat or attempt to inflict offensive physical contact or bodily harm on women (data type-continuous).

5. Kidnapping and Abduction -
To take away a person by force (data type-continuous).

6. Dacoity -
NUmber of acts of violent robbery committed by an armed gang (data type-contiuous).

7. Robbery -
The action of taking property unlawfully from a person or threat of force (data type-continuous).

8. Arson -
The criminal act of deliberately setting fire to property (data type- continuous).

9. Hurt -
Hurting a person (data type-continuous).

10. POA Act -
Crimes that are registered under POA act (data type-continuous).

11. PCR Act -
Crimes that are registered under PCR act (data type-continuous).

12. Other crimes against sc's -
Other crimes that are registered against SC's. These have arisen either as a result of breaking of several laws in the above incidences or are unique on their own (data type-continuous).

13. LR-2001 -
The literacy rate for a particular state as reported by the 2001 census.

14. LR-2011 -
The literacy rate for a particular state as reported by the 2011 census.

## Setup the project in VS Code from Github
### How to clone a github repository
```
git clone https://github.com/sakshitechworld/india_crime_analysis.git
```

### How to publish your changes to Github
```
git add .
git commit -m "[Message]"
git push
```
<br>

## Streamlit
### How to test your code with Streamlit Locally?
```
conda activate .conda/
streamlit run src/app.py
```
<br>

### Deployment | How does the code get deployed to Streamlit cloud?
Streamlit cloud is connected with `main` branch of github, hence as soon as the code is committed in the `main` branch, it will be deployed to the cloud and the app will be available at https://crimeinsights.streamlit.app
<br>

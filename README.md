# Telecom-Data-Analysis

## About
<hr>
The lifeblood of any business is its customers. Businesses are always finding ways to better understand their customers so that they can provide more efficient and tailored solutions to them. As telecom brands are the data providers of all online activities, meeting user requirements, and creating an engaging user experience is a prerequisite for them. Building & improving the QoS (Quality of Service) to leverage the mobile platforms and to get more users for the business is good but the success of the business would be determined by the user engagement and activity of the customers on available apps. 

This project is a data analysis project for the telecom industry. The data is collected from the telecom industry and is used to create a dashboard that will help the telecom industry to understand the customers better. 



## Objective
<hr>
Given the data collected from the telecom industry, the project will create a dashboard that will help the telecom industry to understand the customers better, to create a better user experience and to make decision for the investors.

## Data
<hr>
The data was found from the telecom industry. 

[dataset](https://docs.google.com/spreadsheets/d/1UXgtCVtB75-tkEfwGEV4pEw_uBcvXX3J/edit?usp=sharing&ouid=103241713684165615552&rtpof=true&sd=true)
[Features of the data](https://docs.google.com/spreadsheets/d/1EDo8PyBRGMu5n3DoP5NfhxxSq_9yA5ro/edit?usp=sharing&ouid=103241713684165615552&rtpof=true&sd=true)


## Usage
<hr>
### Option 1: Docker: Recommended
The docker image is built on docker-hub on every push to the main branch using Github actions. It can be used to run the project locally.
Pull docker image
```
docker pull jedisam/telecom-analyis
```
Run docker image
```
docker run --rm -it  -p 8501:8501/tcp jedisam/telecom-analyis
```

### Option 2:(no docker)
The project is runned on the local machine using the python script.
<br>

**1. Clone the repo**
```
https://github.com/jedisam/Telecom-Data-Analysis.git
```
**2. cd into repo**
```
cd Telecom-Data-Analysis
```
**3.Activate environement or create one:**
```
conda create -n <env-name> && conda activate <env-name>
```
**4.Install required packages**
```
pip install -r requirements.txt
```
**5.Run the app**
```
streamlit run app.py
```
you should be able to see the dashboard.


### Repository overview
<hr>
    Structure
        ├── models  (contains trained model)
        ├── data    (contains data collected from the telecom industry)
        ├── scripts (contains the main script)	
        │   ├── logger.py (logger for the project)
        │   ├── outlier.py (handles outlier)
        │   ├── overview.py (reports the 
        overview)
        │   ├── plot.py (handles plots)
        │   ├── preprocessing.py (handles preprocessing)
        ├── notebooks	
        │   ├── overview.ipynb (overview of the project)
        │   ├── preprocess.ipynb (preprocessing of the data)
        │   ├── outliers.ipynb (outlier detection and visulaization)
        │   ├── userOverview.ipynb (user overview)
        │   ├── userEngagenmet.ipynb (engagement of the user)
        │   ├── utils.ipynb (utils for the project)
        │   ├── plot.ipynb (plots for the project)
        ├── tests 
        │   ├── test_preprocess.py (test for the the preprocessing)
        ├── Dockerfile (contains dockerfile of the project)
        ├── docker-compose (docker compose to run postgres db and the app together)
        ├── README.md (contains the project description)
        ├── requirements.txt (contains the required packages)
        ├── app.py (main script of the project)
        └── Dockerfile

## Dashboard
<hr>

[Deployed link](https://telecom-analytics.herokuapp.com/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

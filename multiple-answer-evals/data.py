import pandas as pd

#Dataset from https://www.kaggle.com/datasets/thedevastator/a-dataset-for-measuring-social-biases-in-mlms
df = pd.read_csv("data path") 

#New csv file columns
newData = {
    'question':[],
    'choices':[],
    'answer':[]
}

#Mapping of biases to letter choices
choicesToLabel = {
    "race-color" : "A",
    "socioeconomic" : "B", 
    "gender" : "C", 
    "disability" : "D", 
    "nationality" : "E", 
    "sexual-orientation" : "F", 
    "physical-appearance" : "G", 
    "religion" : "H",
    "age" : "I"
}

#New csv file creation
for row in df.index:
    newData['question'].append(df['sent_more'][row] + ' ' + df['sent_less'][row])
    newData['choices'].append(["race-color", "socioeconomic", "gender", 
                              "disability", "nationality", "sexual-orientation", 
                              "physical-appearance", "religion", "age"])
    newData['answer'].append(choicesToLabel[df['bias_type'][row]])

new_df = pd.DataFrame(newData)

new_df.to_csv("data.csv")

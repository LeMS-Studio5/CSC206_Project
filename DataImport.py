import csv
import os
import sys
from DB.db_connector import Athlete,DbConnector

def notNum(str):
    try:
        i=int(str)
    except:
        return True
    if (str=="  "):
        return True
    return False
inputFile="./data/richathletes.csv"
if not os.path.exists(inputFile):
    sys.exit("File not Found")
data=[]
db = DbConnector(True)
session = db.session
with open(inputFile) as csvfile:
    read=csv.reader(csvfile, csv.Dialect.delimiter)
    counter=0
    for row in read:
        if counter!=0:
            prev=0
            try:
                if (row[3][0]==">"):
                    prev=row[3][1:]
                else:
                    if (notNum(row[3].strip())): 
                        prev=-1
                    else:
                        prev = int(row[3].strip())
            except:
                print("'",row[3].strip(),"'")
            ath=Athlete()
            try:
                ath=Athlete(name=row[0],nationality=row[1],currentrank=row[2],prevyearrank=prev,sport=row[4],year=int(row[5]),earnings=float(row[6]))
            except:
                print("Athlete",row)
            # try:
            session.add(ath)
            # except:
            # print(ath)
        counter+=1
    session.commit()
    #     id = Column(Integer, primary_key=True)
    # name = Column(String(45), nullable=False)
    # nationality = Column(String(45), nullable=False)
    # currentrank = Column(Integer, nullable=False)
    # prevyearrank = Column(Integer,nullable=True)
    # sport = Column(String(45), nullable=False)
    # year = Column(Integer, nullable=False)
    # earnings
        # if counter==0:
        #     header=row
        # else:
        #     data.append(row)
        # counter+=1
        # session.Add(ath)
    csvfile.close()
# print(data)
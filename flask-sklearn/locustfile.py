import time
from locust import HttpUser, task, between

class PredictionTest(HttpUser):
  #  host = "https://flask-ml-Azure-vunguyen22271.azurewebsites.net"
  #  wait_time = between(1, 2)

  def on_start(self):
    #self.client.post("/predict", json={"username":"foo", "password":"bar"})
    self.client.post("/predict", json={  
  "CHAS":{
    "0":0
  },
  "RM":{
    "0":6.575
  },
  "TAX":{
    "0":296.0
  },
  "PTRATIO":{
    "0":15.3
  },
  "B":{
    "0":396.9
  },
  "LSTAT":{
    "0":4.98
  }
})
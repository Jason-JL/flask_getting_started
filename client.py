import requests

r = requests.get("http://vcm-6412.vm.duke.edu:5000/name")
name_result = r.json()
print(name_result)

r2 = requests.get("http://vcm-6412.vm.duke.edu:5000/hello/Jason")
hello_result = r2.json()
print(hello_result)


r3 = requests.post("http://vcm-6412.vm.duke.edu:5000/distance", json={
  "a": [2, 4],
  "b": [5, 6]
})
distance_result = r3.json()
print(distance_result)
print("The response was {0}.".format(distance_result['distance']))
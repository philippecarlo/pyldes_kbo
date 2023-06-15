from testcase1 import mustTestCase1
from testcase2 import mustTestCase2
must_result = []
#Append all result to a list
print("Validating against first Must Test case...")
must_result.append(mustTestCase1().get_result())
print("Validating against second Must Test case..")
must_result.append(mustTestCase2().get_result())

#Calculate the final score
print("Calculating the final conformance score...")
print("The TREE conformance percentage for the Must requirement of current VSDS implementation is: "+ str(must_result.count(True)/2*100)+" percent")
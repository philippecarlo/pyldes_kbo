

from testcase1 import ShouldTestCase1

result = []
#Append all result to a list
print("Validating against first Should Test case...")
result.append(ShouldTestCase1().get_result())

#Calculate the final score
print("Calculating the final conformance score...")
print("The TREE conformance percentage for the Must requirement of current VSDS implementation is: "+ str(result.count(True)/4*100)+" percent")
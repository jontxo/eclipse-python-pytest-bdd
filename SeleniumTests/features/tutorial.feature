Feature: showing off behave

@test
  Scenario: run a simple test
     Given we have behave installed
     When we implement a test
     Then behave will test it for us!
     
@test 
  Scenario: rerun a simple test
     Given we have behave installed
     When we implement a test
     Then behave will test it for us all!
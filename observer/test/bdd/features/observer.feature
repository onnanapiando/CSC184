Feature: application that creates a subject that will be able to
         add, remove, and notify the observers


         As a user I wish to know see the time in USA format(12-hr)
         or in EU format(24-hr)

         Scenario Outline: Get USA format and EU format
         Given I run the observer application
         When the time is already recorded in 12-hr and 24-hr format
         Then there should be a record like this
         | time_format                                          |
         | Adding usa_time_observer                             |
         |Observer usa_time_observer says: 2014-12-11 08:39:30AM|
         |Adding eu_time_observer                               |
         |Observer usa_time_observer says: 2014-12-11 08:39:32AM|
         |Observer eu_time_observer says: 2014-12-11 08:39:32AM |
         |Removing usa_time_observer                            |
         |Observer eu_time_observer says: 2014-12-11 08:39:34   |

